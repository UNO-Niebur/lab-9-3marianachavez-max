# Lab 9 – Image Processing
# Name: Mariana Chavez
# Date: 04.05.2026
# Assignment: Lab 9

from PIL import Image


def swapGreenBlue(img):
    """Swap the green and blue values for every pixel in the image."""
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            pixel = pixels[x, y]
            r, g, b = pixel[:3]
            a = pixel[3:] if len(pixel) > 3 else ()
            pixels[x, y] = (r, b, g) + a

    img.save("swapGB.png")
    print("swapGreenBlue complete! Saved as swapGB.png")


def darken(img, amount):
   """Darken the image by reducing RGB values by the given amount."""
   pixels = img.load()
   width, height = img.size

   for x in range(width):
        for y in range(height):
            pixel = pixels[x, y]
            r, g, b = pixel[:3]
            a = pixel[3:] if len(pixel) > 3 else ()
            r = max(0, r - amount)
            g = max(0, g - amount)
            b = max(0, b - amount)
            pixels[x, y] = (r, g, b) + a

   img.save("darkImg.png")
   print(f"darken complete! Saved as darkImg.png")


def bwFilter(img):
    """Example function: converts image to grayscale."""
    
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            pixel = pixels[x, y]
            red, green, blue = pixel[:3]
            a = pixel[3:] if len(pixel) > 3 else ()
            avg = (red + green + blue) // 3
            pixels[x, y] = (avg, avg, avg) + a

    img.save("bwImg.png", 'png')
    print(f"bwFilter complete! Saved as bwImg.png")


def main():
    #Open the image file
    myImg = Image.open("durango.png")

    # Example (already completed)
    # bwFilter(myImg)

    # Uncomment each function as you complete it
    #bwFilter(myImg)
    #swapGreenBlue(myImg)
    darken(myImg, 20)


if __name__ == "__main__":
    main()
