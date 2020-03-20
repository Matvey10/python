from PIL import Image, ImageDraw
import numpy as np
import sys

sys.path.append("C:\\Users\\user\\PycharmProjects\\lab1\\lab1.3")

def christian_method(pix):
    window_size = 15
    k = 0.5
    rows, cols = pix.shape
    i_rows, i_cols = rows + 1, cols + 1
    integrated_image = np.zeros((i_rows, i_cols), np.float)
    sqr_integrated_image = np.zeros((i_rows, i_cols), np.float)
    integrated_image[1:, 1:] = np.cumsum(np.cumsum(pix.astype(np.float), axis=0), axis=1)
    sqr_img = np.square(pix.astype(np.float))
    sqr_integrated_image[1:, 1:] = np.cumsum(np.cumsum(sqr_img, axis=0), axis=1)
    x, y = np.meshgrid(np.arange(1, i_cols), np.arange(1, i_rows))
    half_window_size = window_size // 2
    x1 = (x - half_window_size).clip(1, cols)
    x2 = (x + half_window_size).clip(1, cols)
    y1 = (y - half_window_size).clip(1, rows)
    y2 = (y + half_window_size).clip(1, rows)
    l_size = (y2 - y1 + 1) * (x2 - x1 + 1)
    sums = (integrated_image[y2, x2] - integrated_image[y2, x1 - 1] - integrated_image[y1 - 1, x2] + integrated_image[
        y1 - 1, x1 - 1])
    sqr_sums = (sqr_integrated_image[y2, x2] - sqr_integrated_image[y2, x1 - 1] - sqr_integrated_image[y1 - 1, x2] +
                sqr_integrated_image[y1 - 1, x1 - 1])
    means = sums / l_size
    stds = np.sqrt(sqr_sums / l_size - np.square(means))
    max_std = np.max(stds)
    min_v = np.min(pix)
    threshold_values = ((1.0 - k) * means + k * min_v + k * stds / max_std * (means - min_v))
    return processing_method(pix, threshold_values)


def processing_method(pix, threshold_values):
    return ((pix >= threshold_values) * 255).astype(np.uint8)


original = Image.open("C:\\Users\\user\\Desktop\\оави\\text.bmp")
#original = Image.open("C:\\Users\\user\\Desktop\\оави\\text2.bmp")
original.show()
w, h = original.size
pix = original.convert('L')
pix.show()
pix = np.array(list(pix.getdata()))
pix = pix.reshape(h, w)
pix = christian_method(pix)
im = Image.fromarray(pix)
im.show()
