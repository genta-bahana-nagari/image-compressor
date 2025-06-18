# 🗜️ Image Compression Script

## 📖 About the Project
This is a Python script to compress images within a specified folder using the `Pillow` library. It helps reduce file size without significantly compromising quality. Useful for web optimization and storage management.

---

## 🧰 Tech Stack
- **Language:** Python 3.x
- **Library:** Pillow
- **Supported Formats:** `.jpg`, `.jpeg`, `.png`

---

## ✨ Features
- 🔄 Compress all images in a given folder
- 📂 Automatically creates an output folder if not present
- ⚙️ Adjustable compression quality (1–100)
- 📏 Displays file sizes before and after compression
- ✅ Supports `.jpg`, `.jpeg`, `.png`

---

## 📦 Installation & Setup

1. **Install Python**  
   Make sure Python is installed on your system. Check with:
   ```bash
   python --version
   ```

2. **Install Pillow**  
   Use pip to install the required library:
   ```bash
   pip install pillow
   ```

3. **Save the Script**  
   Save the Python script as `compress_images.py`.

---

## 🚀 Usage

1. Open a terminal and navigate to the script's directory.
2. Run the script:
   ```bash
   python compress_images.py
   ```
3. Follow the prompts:
   - Enter the path of the folder containing the original images
   - Enter the path of the folder to save the compressed images
   - Enter the compression quality (1–100). Leave blank for default `85`.

---

## 💡 Sample Output

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

---

## ⚠️ Notes

- Only images with extensions `.jpg`, `.jpeg`, or `.png` will be processed.
- Ensure input/output folders have appropriate read/write permissions.
- Lower quality results in smaller files, but may affect image clarity.

---

## 👤 Author
- **Genta Bahana Nagari** – [LinkedIn](https://www.linkedin.com/in/genta-bahana-nagari/) | [GitHub](https://github.com/genta-bahana-nagari)

---

## 🌟 Show Your Support
If you find this script helpful, feel free to ⭐ the repository and share it with others!

---

## 📜 License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---
