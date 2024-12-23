from PIL import Image
import os

def compress_image(input_image_path, output_image_path, quality=85):
    with Image.open(input_image_path) as img:
        img.save(output_image_path, 'JPEG', optimize=True, quality=quality)

def compress_images_in_folder(input_folder, output_folder, quality=85):
    if not os.path.exists(output_folder):
        print(f"Create output directory: {output_folder}")
        os.makedirs(output_folder)
    
    supported_formats = (".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG")
    
    for filename in os.listdir(input_folder):
        if filename.endswith(supported_formats):
            input_image_path = os.path.join(input_folder, filename)
            output_image_path = os.path.join(output_folder, filename)
            
            compress_image(input_image_path, output_image_path, quality)
            
            print(f"{filename}:")
            print(f"  Size before compression: {os.path.getsize(input_image_path) / 1024:.2f} KB")
            print(f"  Size after compression: {os.path.getsize(output_image_path) / 1024:.2f} KB\n")

input_folder = input("Enter the folder path to the original image.: ")
output_folder = input("Enter the folder path to the compressed image: ")

try:
    quality = int(input("Enter compression quality (1-100, default 85): ") or 85)
except ValueError:
    quality = 85

compress_images_in_folder(input_folder, output_folder, quality)
