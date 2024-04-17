from PIL import Image


def galaxy(name, *ls, light=0):
    im = Image.open(name)
    im.transpose(Image.FLIP_TOP_BOTTOM)
    pixels = im.load()  # список с пикселями
    x, y = im.size  # ширина (x) и высота (y) изображения
    for i in range(x):
        for j in range(y):
            p = pixels[i, j]
            if sum(p) < 255:
                out = []
                for q in p:
                    out.append(min(255, q + light))
                pixels[i, j] = tuple(out)

    out = []
    for x, y in ls:
        out.append(im.crop((x, y, x + 200, y + 200)))

    new_img = Image.new('RGB', (600, 400))
    for y in range(0, 400, 200):
        for x in range(0, 600, 200):
            print(x, y, len(out))
            new_img.paste(out.pop(0), (x, y))

    return new_img


galaxy(
    'galaxy.png',
    (100, 824), (824, 824), (0, 400),
    (624, 0), (300, 500), (600, 624),
    light=30
).show()
