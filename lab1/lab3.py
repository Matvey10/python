from PIL import Image
import numpy as np
import math

def foo(m):
    tresh = 40
    # x = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    # y = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    width, height = m.size
    m = m.load()
    Gx = np.zeros((width, height), np.float)
    Gy = np.zeros((width, height), np.float)
    F = np.zeros((width, height), np.float)
    for i in range(2, width-2, 1):
        for j in range(2, height-2, 1):
            Gx[i, j] = m[i+1, j-1] + m[i+1, j]*2 + m[i+1, j+1] - m[i-1, j-1] - m[i-1, j]*2 - m[i-1, j+1]
            Gy[i, j] = m[i-1, j+1] + m[i, j+1]*2 + m[i+1, j+1] - m[i-1, j-1] - m[i, j-1]*2 - m[i+1, j-1]
    maxf = 0
    for i in range(2, width-2, 1):
        for j in range(2, height-2, 1):
            F[i, j] = math.sqrt(Gx[i, j]**2 + Gy[i, j]**2)
            if F[i, j] > maxf:
                maxf = F[i, j]
    for i in range(2, width-2, 1):
        for j in range(2, height-2, 1):
            F[i, j] = F[i, j]*255//maxf
    for i in range(2, width-2, 1):
        for j in range(2, height-2, 1):
            if F[i, j] > tresh:
                F[i, j] = 255
            else:
                F[i, j] = 0
    im = Image.fromarray(F.transpose())
    return im

def testLab3(path):
    original = Image.open(path)
    original.save(path)
    original.show()
    proc = original.convert('L')
    proc.show()
    image = foo(proc)
    image.show()

testLab3("C:\\Users\\user\\Desktop\\оави\\people.bmp")
testLab3("C:\\Users\\user\\Desktop\\оави\\picture.bmp")

