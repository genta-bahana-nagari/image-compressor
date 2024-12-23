<p align="center">
  <a href="https://www.python.org" target="_blank">
    <img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png" width="400" alt="Python Logo">
  </a>
</p>


# Image Compression Script

## Description
This script is used to compress images in a specific folder using the Python `Pillow` library. By utilizing this script, you can reduce the size of image files without significantly reducing their quality. The script supports popular image formats such as JPEG and PNG.

## Features
- Compress images in a specific folder.
- Supports image formats: `.jpg`, `.jpeg`, `.png`.
- Provides the option to set the compression quality level.
- Creates an output folder automatically if it does not exist.
- Shows the file size before and after compression.

## System Requirements
- Python 3.x
- `Pillow` Library

## Installation
1. Make sure you have Python installed on your computer.
2. Install the `Pillow` library using the following command:
```bash
pip install pillow
```

## Usage
1. Save the Python code in a file, for example `compress_images.py`.
2. Run the script using the following command:
```bash
python compress_images.py
```
3. Follow these steps when prompted:
- Enter the path of the folder containing the original images.
- Enter the path of the folder to save the compressed images.
- Enter the compression quality level (1-100). If left blank, the default value is 85.

## Sample Output
When the script is run, here is a sample output that is generated:
```text
Enter the path of the folder containing the original images: /path/to/input
Enter the path of the folder to save the compressed images: /path/to/output
Enter the compression quality (1-100, default 85): 75

Create output directory: /path/to/output
image1.jpg:
Size before compression: 1200.50 KB
Size after compression: 800.25 KB

image2.png:
Size before compression: 950.00 KB
Size after compression: 700.00 KB
```

## Important Notes
- The script only compresses files with the extension `.jpg`, `.jpeg`, or `.png`.
- Make sure the input and output folders have the appropriate read/write permissions.
- Lower compression quality results in smaller file sizes but may reduce image quality.

## License
This project is licensed under the [MIT License](LICENSE).

---

Enjoy using this script to manage your image sizes more efficiently!
