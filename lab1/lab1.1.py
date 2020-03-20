from PIL import Image


def upload_file(path):
    image = Image.open(path)
    image.save()


def decimation(path, ratio):
    interpolation(path, 1 / ratio)


def interpolation(path, ratio):
    try:
        original = Image.open(path)
        original.save("scenery-original.bmp")
        width, height = original.size
        pix_original = original.load()
        new_width = int(width / ratio)
        new_height = int(height / ratio)
        proc_image = Image.new(original.mode, (new_width, new_height))
        print(proc_image.size)
        pix_proc = proc_image.load()
        for i in range(new_width):
            for j in range(new_height):
                pix_proc[i, j] = pix_original[int(i * ratio), int(j * ratio)]
        proc_image.show()
        proc_image.save("scenery-resize.bmp")
        return "scenery-resize.bmp"
    except FileNotFoundError:
        print("Файл не найден")


def oversampling(path, stretch_ratio, comp_ratio):
    decimation(interpolation(path, comp_ratio), stretch_ratio)


def oversampling(path, ratio):
    interpolation(path, ratio)


interpolation("C:\\Users\\user\\Desktop\\оави\\s1200.bmp", 3)
decimation("C:\\Users\\user\\Desktop\\оави\\s1200.bmp", 2)
oversampling("C:\\Users\\user\\Desktop\\оави\\s1200.bmp", 5.5)
