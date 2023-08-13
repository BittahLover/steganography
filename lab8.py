from PIL import Image, ImageDraw
from random import randint
from re import findall


def encSteganograf(text_inp):
    img = Image.open("img.jpg")
    draw = ImageDraw.Draw(img)
    width = img.size[0]
    height = img.size[1]
    pix = img.load()

    f = open('keys.txt', 'w')
    for elem in ([ord(elem) for elem in text_inp]):
        key = (randint(1, width - 10), randint(1, height - 10))
        g, b = pix[key][1:3]
        draw.point(key, (elem, g, b))
        f.write(str(key) + '\n')
    print('keys were written to the keys.txt file')
    img.save("newimage.png", "PNG")
    f.close()


def decSteganograf():
    a = []
    keys = []
    img = Image.open('newimage.png')
    pix = img.load()
    f = open('keys.txt', 'r')
    y = str([line.strip() for line in f])

    for i in range(len(findall(r'\((\d+)\,', y))):
        keys.append((int(findall(r'\((\d+)\,', y)[i]), int(findall(r'\,\s(\d+)\)', y)[i])))
    for key in keys:
        a.append(pix[tuple(key)][0])
    return ''.join([chr(elem) for elem in a])


if __name__ == '__main__':
    text = 'Some sort of text that would be taken from picture'
    print('Result of encrypt: ')
    encSteganograf(text)
    print('\nResult of decrypt: ')
    print("You message: ", decSteganograf())