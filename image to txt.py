import cv2
import numpy as np


def image2text(img, characters):
    height, width = img.shape

    numCharacters = len(characters)

    text = ""

    step = 256 // numCharacters

    for i in range(height):
        for j in range(width):

            pixel = img[i][j]

            index = pixel // step - 1

            if pixel % step != 0:
                index += 1

            text += characters[index]

        text += "\n"

    return text

def main():
    path = "C:/Users/sabir/Downloads/Qrcode_wikipedia_fr_v2clean.png"

    image = cv2.imread(path)

    gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    characters = list("#m^. ")


    text = image2text(gray_scale, characters)

    cv2.imshow("hello", gray_scale)

    print(text)

main()