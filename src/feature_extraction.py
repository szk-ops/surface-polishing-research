#!/usr/bin/env python3
"""Image preprocessing utilities for polishing surface analysis."""

from pathlib import Path

import cv2
import numpy as np
from PIL import Image


def load_image(path):
    img = cv2.imread(str(path), cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"Cannot read image: {path}")
    return img


def normalize_image(img):
    img = img.astype(np.float32)
    img = (img - img.min()) / (img.max() - img.min() + 1e-8)
    return img * 255.0


def denoise_image(img, kernel_size=3):
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)


def enhance_contrast(img):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    return clahe.apply(img.astype(np.uint8))


def resize_image(img, size=(256, 256)):
    return cv2.resize(img, size, interpolation=cv2.INTER_AREA)


def preprocess_image(path, size=(256, 256)):
    img = load_image(path)
    img = resize_image(img, size)
    img = denoise_image(img)
    img = enhance_contrast(img)
    return normalize_image(img).astype(np.uint8)
