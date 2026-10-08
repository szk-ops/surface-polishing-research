#!/usr/bin/env python3
"""Simple defect detection for polished surface images.

This version uses a lightweight heuristic model based on image entropy,
edge density, and local variance. It is suitable as a baseline prototype.
"""

import argparse
import cv2
import numpy as np

from preprocessing import preprocess_image


def detect_defects(img):
    gray = preprocess_image(img) if isinstance(img, str) else img.astype(np.uint8)
    edges = cv2.Canny(gray, 50, 150)
    edge_ratio = np.mean(edges > 0)
    variance = float(np.var(gray))
    entropy = float(-np.sum((np.histogram(gray, bins=256)[0] / max(1, gray.size)) * np.log2(np.histogram(gray, bins=256)[0] / max(1, gray.size) + 1e-8)))

    defect_score = 0.5 * edge_ratio + 0.3 * (variance / 255.0) + 0.2 * (entropy / 10.0)
    mask = edges > 0
    return mask, defect_score


def main():
    parser = argparse.ArgumentParser(description="Detect potential defects on a polished surface")
    parser.add_argument("--input", type=str, required=True, help="Input image path")
    args = parser.parse_args()

    mask, score = detect_defects(args.input)
    print({
        "defect_score": round(float(score), 4),
        "edge_ratio": round(float(np.mean(mask)), 4),
        "status": "defect likely" if score > 0.4 else "surface looks acceptable",
    })


if __name__ == "__main__":
    main()
