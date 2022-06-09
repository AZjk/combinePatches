import numpy as np


def get_canvas(positions, pixel_size, det_size):
    ccdx = [x[0] for x in positions]
    ccdz = [x[1] for x in positions]

    x_min = np.min(ccdx)
    z_min = np.min(ccdz)

    x_range = np.max(ccdx) - x_min
    z_range = np.max(ccdz) - z_min 

    x_range = int(x_range / pixel_size + 0.5) + det_size[1] 
    z_range = int(z_range / pixel_size + 0.5) + det_size[0] 

    canvas = np.zeros((z_range, x_range), dtype=np.float64)

    return canvas, x_min, z_min


def combine_patches(images, positions, pixel_size):
    '''
    combine images obtained with an area detector at different camera
    positions.
    
    Parameters
    ----------
    images: list
        a list of of 2d image patches. the images must have the same dimension
    positions: list
        a list of camera positions [(x0, z0), (x1, z1), ...]. The unit must
        be the same as pixel_size.
    pixel_size: the pixel size of the area detector.

    Returns
    -------
    ret: 2d numpy array representing the combined image.

    Examples
    --------
    >>> images = [np.ones((100, 100)) for _ in range(100)]
        pixel_size = 75E-3
        positions = np.random.randint(-10, 10, size=(100, 2)) * pixel_size
        positions = list(positions)
        a = combine_patches(images, positions, pixel_size)
    '''
    assert len(images) == len(positions), \
        'images and position must have the same length'
    det_size = images[0].shape[-2:]

    canvas, x_min, z_min = get_canvas(positions, pixel_size, det_size)
    norm_factor = np.zeros_like(canvas, dtype=np.uint32)

    for image, position in zip(images, positions):
        assert image.ndim == 2, 'images must be 2d arrays'
        assert image.shape == det_size, 'images must have the same shape'
        col = int((position[0] - x_min) / pixel_size + 0.5)
        row = int((position[1] - z_min) / pixel_size + 0.5)
        sl_v = slice(row, row + det_size[0])
        sl_h = slice(col, col + det_size[1])
        canvas[sl_v, sl_h] += image
        norm_factor[sl_v, sl_h] += 1

    # avoid zero division
    norm_factor[norm_factor == 0] = 1    
    return canvas / norm_factor


if __name__ == '__main__':
    pass