#!/usr/bin/env python

"""Tests for `combinepatches` package."""

from cmath import pi
import unittest 
from combinepatches import get_canvas, combine_patches
import numpy as np 


class TestCombinePatches(unittest.TestCase):
    def test_get_canvas(self):
        det_size = (1023, 1024)
        positions = [[0.0, 1.0]]
        pixel_size = 55E-3
        canvas, x_min, z_min = get_canvas(positions, pixel_size, det_size)
        self.assertEqual(x_min, 0)
        self.assertEqual(z_min, 1.0)
        self.assertEqual(canvas.shape, det_size)

    def test_get_canvas_2(self):
        det_size = (1000, 1000)
        pixel_size = 55E-3
        positions = [[0.0, 1.0], [pixel_size * 100, 1 + pixel_size * 200]]
        canvas, x_min, z_min = get_canvas(positions, pixel_size, det_size)
        self.assertEqual(x_min, 0)
        self.assertEqual(z_min, 1.0)
        self.assertEqual(canvas.shape[1], det_size[1] + 100)
        self.assertEqual(canvas.shape[0], det_size[0] + 200)

    def test_combine_images_2(self):
        det_size = (100, 100) 
        ground_truth = np.random.randint(0, 255, size=(200, 200))   # int64 
        pixel_size = 55E-3
        positions = []
        images = []

        for n in range(11):
            for m in range(11):
                sl_v = slice(n * 10, n * 10 + det_size[0])
                sl_h = slice(m * 10, m * 10 + det_size[0])
                img = ground_truth[sl_v, sl_h]
                images.append(img)
                positions.append([m * 10 * pixel_size, n * 10 * pixel_size])

        result = combine_patches(images, positions, pixel_size)
        self.assertEqual(result.shape, ground_truth.shape)
        self.assertTrue(np.allclose(result, ground_truth))
