from PIL import Image
import numpy as np
import os, csv


def letter_processing(path):
    list_data = []
    original = Image.open(path)
    thresh = 200
    #original.show()
    fn = lambda x: 255 if x > thresh else 0
    proc = original.convert('L').point(fn)
    width, height = proc.size
    blackWeight = 0
    pix = proc.load()
    for i in range(width):
        for j in range(height):
            blackWeight += pix[i, j]
    list_data.append(blackWeight)
    blackWeightNorm = blackWeight / (width * height)
    list_data.append(blackWeightNorm)
    print("вес черного нормированный:", blackWeightNorm)
    xsr = 0
    ysr = 0
    for i in range(width):
        for j in range(height):
            xsr += i * pix[i, j]
            ysr += j * pix[i, j]
    xsr = xsr / blackWeight
    ysr = ysr / blackWeight
    list_data.append(xsr)
    list_data.append(ysr)
    xsrNorm = xsr / (width - 1)
    ysrNorm = ysr / (height - 1)
    list_data.append(xsrNorm)
    list_data.append(ysrNorm)
    print("x норм: ", xsrNorm)
    print("y норм: ", ysrNorm)
    Ix, Iy = 0, 0
    for i in range(width):
        for j in range(height):
            Ix += pix[i, j] * ((j - ysr) ** 2)
            Iy += pix[i, j] * ((i - xsr) ** 2)
    list_data.append(Ix)
    list_data.append(Iy)
    IxNorm = Ix / (width ** 2 + height ** 2)
    print("осевой момент по горизонтали: ", IxNorm)
    IyNorm = Iy / (width ** 2 + height ** 2)
    print("осевой момент по вертикали:", IyNorm)
    list_data.append(IxNorm)
    list_data.append(IyNorm)
    ProjX = np.zeros(width)
    for i in range(width):
        for j in range(height):
            ProjX[i] += pix[i, j]
    ProjY = np.zeros(height)
    for j in range(height):
        for i in range(width):
            ProjY[j] += pix[i, j]
    return list_data


path = "C:\\Users\\user\\Desktop\\оави\\буквы"
list_cols = ["Вес", "Удельный вес", "X центра тяжести", "Y центра тяжести", "X нормированный", "Y нормированный",
                 "Осевой момент инерции по горизонтали", "Осевой момент инерции по вертикали",
                 "Нормированный осевой момент по горизонтали", "Нормированный осевой момент по вертикали"]
files = os.listdir(path)
with open(path + "\\output.csv", "w", newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=';')
    writer.writerow(list_cols)
    for file in files:
        writer.writerow(letter_processing(path+"\\"+file))