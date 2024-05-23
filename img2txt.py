import cv2
import sys
import os
import re

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

            if index >= numCharacters:
                index -= 1

            if index <= 0:
                index = 0

            text += characters[index]

        text += "\n"

    return text

def printMenu():
    print(f"Usage    : python {sys.argv[0]} [OPTIONS] image_path\n")
    print("OPTIONS  : ")
    print("     --row <number>  : Rows number")
    print("     --col <number>  : Columns number")

def main():
    
    try:
        
        pattern = r"^((((--row [0-9]+) (--col [0-9]+))|--row [0-9]+|--col [0-9]+|((--col [0-9]+) (--row [0-9]+))|) [^-]{1}\S*)| (--help|-h)$"
    
        if re.match(pattern, " ".join(sys.argv[1:-1]) + " " + sys.argv[-1]) is None:
            print(f"Bad Syntax. Use \"python {sys.argv[0]} --help\" to see help menu.")
            return
    
        if sys.argv[-1] in ("--help", "-h") and len(sys.argv) == 2:
            printMenu()
            return
    
        if not os.path.exists(sys.argv[-1]):
            print("File not found !!!")
            return
        
        path = os.path.basename(sys.argv[-1])
    
        image = cv2.imread(path)
    
        row, col = -1, -1
    
        if "--col" in sys.argv:
            col = int(sys.argv[sys.argv.index("--col") + 1])
    
        if "--row" in sys.argv:
            row = int(sys.argv[sys.argv.index("--row") + 1])
    
        if row < 0:
            if col >= 0:
                image = cv2.resize(image, None, fx=col/image.shape[1], fy=1, interpolation=cv2.INTER_CUBIC)
    
        else:
            if col >= 0:
                image = cv2.resize(image, None, fx=col/image.shape[0], fy=row/image.shape[1], interpolation=cv2.INTER_CUBIC)
            else:
                image = cv2.resize(image, None, fx=1, fy=row/image.shape[1], interpolation=cv2.INTER_CUBIC)
    
        
        gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    
        characters = list("#m~. ")
    
    
        text = image2text(gray_scale, characters)
    
        print(text)
        
    except:
        printMenu()

main()
