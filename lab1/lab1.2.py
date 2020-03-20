from PIL import Image, ImageDraw


def semitone(path):
    try:
        original = Image.open(path)
        original.save("poppy.bmp")
        print("The size of the Image is: ")
        print(original.format, original.size, original.mode)
        #draw = ImageDraw.Draw(original)
        pix = original.load()
        for i in range(original.size[0]):
            for j in range(original.size[1]):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                S = (a + b + c) // 3
                original.putpixel((i, j), (S, S, S))
        original.save("grey-poppy.bmp")
        original.show()
    except FileNotFoundError:
        print("Файл не найден")


semitone("C:\\Users\\user\\Desktop\\оави\\poppy.bmp")