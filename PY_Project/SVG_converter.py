import cv2
import numpy as np
import svgwrite
from skimage import measure

# Load the image
image_path = r"C:\Users\himan\Downloads\Earth.png"  # Replace with your image file path
output_svg = r"C:\Users\himan\Downloads\output.svg"

# Read the image and convert it to grayscale
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Convert the image to binary (black and white)
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Find contours in the binary image
contours = measure.find_contours(binary_image, 0.8)

# Create SVG file
dwg = svgwrite.Drawing(output_svg)

# Convert contours to SVG path
for contour in contours:
    path_data = []
    for point in contour:
        path_data.append(f"L {point[1]} {point[0]}")  # Convert (y, x) to (x, y)
    path_data[0] = f"M {path_data[0][2:]}"

    # Draw path in SVG
    dwg.add(dwg.path(d=" ".join(path_data), fill="black", stroke="none"))

# Save the SVG
dwg.save()
print(f"SVG file saved to {output_svg}")
