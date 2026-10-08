#!/usr/bin/env python3
"""Synthetic surface polishing data generator.

This script creates mock surface images with simulated defects and polished textures.
It is intended for research prototypes when no real dataset is available.
"""

import argparse
import random
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

from config import SYNTHETIC_DIR, IMAGE_SIZE, DEFAULT_SEED


def generate_surface_texture(shape, roughness=0.35, brightness=180):
    """Generate a grayscale surface texture with noise and weak periodic patterns."""
    rng = np.random.default_rng(DEFAULT_SEED)
    y, x = np.mgrid[0:shape[0], 0:shape[1]]
    base = np.sin(x * 0.08) + np.cos(y * 0.07)
    noise = rng.normal(0, roughness, size=shape)
    texture = brightness + 25 * base + 70 * noise
    texture = np.clip(texture, 0, 255)
    return texture.astype(np.uint8)


def add_defects(image, defect_count=6):
    """Add scratches, pits, and uneven spots to simulate imperfect polishing."""
    img = image.copy()
    h, w = image.shape[:2]
    rng = np.random.default_rng(DEFAULT_SEED + 1)

    for _ in range(defect_count):
        x = rng.integers(0, w)
        y = rng.integers(0, h)
        radius = rng.integers(3, 25)
        rr, cc = np.ogrid[:h, :w]
        mask = (rr - y) ** 2 + (cc - x) ** 2 <= radius ** 2
        strength = rng.integers(20, 80)
        img[mask] = np.clip(img[mask] - strength, 0, 255)

    # add scratches
    for _ in range(defect_count // 2):
        x0 = rng.integers(0, w)
        y0 = rng.integers(0, h)
        x1 = rng.integers(0, w)
        y1 = rng.integers(0, h)

        for i in range(max(abs(x1 - x0), abs(y1 - y0))):
            t = i / max(1, abs(x1 - x0) + abs(y1 - y0))
            px = int(round(x0 + (x1 - x0) * t))
            py = int(round(y0 + (y1 - y0) * t))
            if 0 <= px < w and 0 <= py < h:
                img[py:py + 2, px:px + 2] = np.clip(img[py:py + 2, px:px + 2] - 30, 0, 255)

    return img


def save_image(img, path):
    image = Image.fromarray(img.astype(np.uint8), mode='L')
    image = image.filter(ImageFilter.SMOOTH)
    image.save(path)


def generate_dataset(count=20, out_dir=None):
    out_dir = Path(out_dir) if out_dir else SYNTHETIC_DIR
    out_dir.mkdir(parents=True, exist_ok=True)

    for idx in range(count):
        roughness = 0.15 + (idx % 5) * 0.08
        texture = generate_surface_texture(IMAGE_SIZE, roughness=roughness)
        defected = add_defects(texture, defect_count=4 + idx % 8)
        save_image(defected, out_dir / f"surface_{idx:03d}.png")

    print(f"Generated {count} synthetic surface images under {out_dir}")


def main():
    parser = argparse.ArgumentParser(description="Generate synthetic polishing surface data")
    parser.add_argument("--count", type=int, default=20, help="Number of images to generate")
    parser.add_argument("--output", type=str, default=str(SYNTHETIC_DIR), help="Output directory")
    args = parser.parse_args()
    generate_dataset(args.count, args.output)


if __name__ == "__main__":
    main()
