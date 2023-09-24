from PIL import Image
import os


path = './imgs'
pathOut = './resizedImgs'

# make dir if not exist
os.makedirs(pathOut, exist_ok=True)


def resize_image(sizeX, sizeY):
    for filename in os.listdir(path):
        # os.path.join a function to construct paths in
        # a platform-independent way.
        image = Image.open(os.path.join(path, filename))

        print(f'Current size: {image.size}')

        resized_image = image.resize((sizeX, sizeY))

        clean_name = os.path.splitext(filename)[0]

        resized_image.save(os.path.join(
            pathOut, f'{clean_name}_{sizeX}x{sizeY}_resized.jpg'))

        print(f'New size size: {resized_image.size}')


print("Enter the desired size")

desired_sizeX = int(input("Enter Width: "))
desired_sizeY = int(input("Enter height: "))

resize_image(desired_sizeX, desired_sizeY)
