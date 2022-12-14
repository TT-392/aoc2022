from PIL import Image

def genImage(pixArray, filename):
    pixels = [x for sublist in pixArray for x in sublist]

    height = len(pixArray)
    width = len(pixArray[0])
    image = Image.new('RGB', (width, height))

    image.putdata(pixels)

    image.save(filename)







