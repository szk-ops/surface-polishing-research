#!/usr/bin/env python3
"""Feature extraction module for polishing quality analysis."""

import argparse
from pathlib import Path

import numpy as np
from sklearn.feature_extraction import image as sk_image
from skimage.feature import graycomatrix, graycoprops

from preprocessing import preprocess_image


def basic_statistics(img):
    mean = float(np.mean(img))
    std = float(np.std(img))
    min_val = float(np.min(img))
    max_val = float(np.max(img))
    return {
        "mean": mean,
        "std": std,
        "min": min_val,
        "max": max_val,
    }


def glcm_features(img):
    img = img.astype(np.uint8)
    glcm = graycomatrix(img, distances=[1], angles=[0, np.pi / 4, np.pi / 2, 3 * np.pi / 4], levels=256, symmetric=True, normed=True)
    props = {
        "contrast": float(np.mean(graycoprops(glcm, 'contrast'))),
        "dissimilarity": float(np.mean(graycoprops(glcm, 'dissimilarity'))),
        "homogeneity": float(np.mean(graycoprops(glcm, 'homogeneity'))),
        "energy": float(np.mean(graycoprops(glcm, 'energy'))),
        "asm": float(np.mean(graycoprops(glcm, 'ASM'))),
    }
    return props


def edge_density(img):
    sobel_x = np.abs(np.gradient(img, axis=1))
    sobel_y = np.abs(np.gradient(img, axis=0))
    edges = np.hypot(sobel_x, sobel_y)
    return float(np.mean(edges))


def extract_features(image_path):
    processed = preprocess_image(image_path)
    stats = basic_statistics(processed)
    texture = glcm_features(processed)
    edges = edge_density(processed)
    features = {**stats, **texture, "edge_density": edges}
    return features


def main():
    parser = argparse.ArgumentParser(description="Extract polishing surface features")
    parser.add_argument("--input", type=str, required=True, help="Input image path")
    args = parser.parse_args()
    features = extract_features(args.input)
    print(features)


if __name__ == "__main__":
    main()
