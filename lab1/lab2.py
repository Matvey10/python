from PIL import Image
import numpy as np

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


def foo(m, i, j):
    ap = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
    count = 0
    for i1 in range(3):
        for j1 in range(3):
            if m[i - 1 + i1, j - 1 + j1] == 0:
                count += ap[i1, j1]
    return count


#original = Image.open("C:\\Users\\user\\Desktop\\оави\\1929.bmp")
original = Image.open("C:\\Users\\user\\Desktop\\оави\\h1.bmp")
thresh = 200
original.show()
fn = lambda x: 255 if x > thresh else 0
proc = original.convert('L').point(fn)
width, height = proc.size
image_array = np.asarray(proc)
pix = proc.load()
im = proc.copy()
pix1 = im.load()
for i in range(2, width - 2, 1):
    for j in range(2, height - 2, 1):
        if foo(pix1, i, j) >= 8:
            pix[i, j] = 0
        else:
            pix[i, j] = 255
print(image_array)
proc.show()
