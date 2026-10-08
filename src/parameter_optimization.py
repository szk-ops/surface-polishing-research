#!/usr/bin/env python3
"""Quality assessment based on extracted image features."""

import argparse

import numpy as np

from feature_extraction import extract_features


def surface_quality_score(features):
    # A simple scoring heuristic for research prototype.
    contrast = features.get("contrast", 0)
    std = features.get("std", 0)
    edge_density = features.get("edge_density", 0)
    homogeneity = features.get("homogeneity", 0)

    score = 10.0
    score -= 0.02 * contrast
    score -= 0.05 * std
    score += 1.5 * homogeneity
    score -= 0.03 * edge_density
    score = max(0.0, min(10.0, score))
    return float(score)


def classify_quality(score):
    if score >= 8.0:
        return "优" 
    elif score >= 6.0:
        return "良"
    elif score >= 4.0:
        return "合格"
    return "不合格"


def main():
    parser = argparse.ArgumentParser(description="Assess polishing quality")
    parser.add_argument("--input", type=str, required=True, help="Input image path")
    args = parser.parse_args()

    features = extract_features(args.input)
    score = surface_quality_score(features)
    quality = classify_quality(score)

    print({
        "quality_score": round(score, 4),
        "quality_label": quality,
        "features": features,
    })


if __name__ == "__main__":
    main()
