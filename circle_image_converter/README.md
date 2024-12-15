# Circle Image Converter

This script processes an image to create a circular version of it, centers the circular crop within the largest possible square area, resizes it to 240x240 pixels, and saves the result as a `.png` file.

## Features

- Takes an image input and crops it into a circular shape.
- Centers the circular crop within the largest square area of the original image.
- Resizes the result to 240x240 pixels.
- Saves the modified image as a new `.png` file.

## Prerequisites

Before using the script, make sure you have the following installed:

- Python 3.6 or later
- [Pillow](https://pillow.readthedocs.io/en/stable/) (Python Imaging Library):
  ```bash
  pip install pillow

Usage
Clone or Download the Repository:
Clone this repository or download the script to your local machine.

Provide the Path to Your Image:
Update the ruta_imagen variable in the script with the full path to your image file:

python
Copiar código


ruta_imagen = "/path/to/your/image.jpeg"


Run the Script:
Execute the script in your Python environment:

python circle_image_converter.py


Output:
The script will generate a circular image saved as imagen_circular_recortada_240x240.png in the current working directory. You will also see a confirmation message:

Imagen circular recortada creada y guardada en imagen_circular_recortada_240x240.png

How It Works
Open the Original Image:
The script loads the image specified by the ruta_imagen variable.

Calculate the Largest Square Area:
Determines the size of the largest square that fits within the original image dimensions.

Crop the Image to a Square:
Centers the square area within the original image and crops it.

Create a Circular Mask:
Generates a circular mask with a transparent background.

Apply the Mask:
Applies the circular mask to the square image, resulting in a circular crop.

Resize to 240x240 Pixels:
The circular image is resized to 240x240 pixels using high-quality resampling.

Save the Final Image:
The final image is saved as imagen_circular_recortada_240x240.png in the working directory.


