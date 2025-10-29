# 🧩 pyQRX CLI QR Code Generator

A simple and efficient **Python-based command-line tool** to generate QR codes instantly from any link or text string.  
Easily create and save your QR codes directly from your terminal!

---

## 🚀 Features
- Generate QR codes from **links or plain text**
- Save QR codes to custom file names and directories
- Lightweight and easy-to-use CLI interface
- Fully written in Python 🐍

---

## ⚙️ Setup

### 1️⃣ Clone or Download the Project
```bash
git clone [https://github.com/yourusername/cli-qr-generator.gi](https://github.com/itzTron/pyQRX.git
cd pyQRX
```
## 2️⃣ Create a Virtual Environment (Recommended)
```bash
python -m venv venv
```
## Activate it:

### Windows
```powershell
.\venv\Scripts\activate
```
### MacOS / Linux
```bash
source venv/bin/activate
```
## 3️⃣ Install Requirements
```bash
pip install -r requirements.txt
```
## 🧠 How to Use

# Run the script from your terminal using python or python3.

## 📜 Syntax
```
python pyQRX.py "Your_Data_Here" [options]
Arguments:

"Your_Data_Here" (Required):
The link, text, or data you want to encode.
(Wrap it in quotes if it contains spaces or special characters.)

[options] (Optional):

-o <filename.png> or --output <filename.png> → Specify a custom name or path for the output image.
Defaults to qrcode.png in the current directory.
```
## 💡 Examples
## 1️⃣ Basic Usage (Default Filename)

## Generate a QR code for a website:
```
python pyQRX.py "https://www.google.com"
```

## ✅ Output:
```
Successfully generated QR code and saved it to: qrcode.png
```
## 2️⃣ Specifying an Output Filename
```
python qr_generator.py "https://www.my-website.com" -o "my_website_qr.png"
```

## ✅ Output:
```
Successfully generated QR code and saved it to: my_website_qr.png
```
## 3️⃣ Encoding Plain Text
```
python qr_generator.py "Hello World!" --output "hello.png"
```

## ✅ Output:
```
Successfully generated QR code and saved it to: hello.png
```
## 4️⃣ Saving to a Different Directory
```
python qr_generator.py "Some data" -o "images/my_qr.png"
```

## ✅ Output:
```
Successfully generated QR code and saved it to: images/my_qr.png
```
## 📦 Requirements
```
 Python 3.7+

 qrcode library

 Install manually (if needed):

 pip install qrcode[pil]
```
 
## 🤝 Contributing

### Feel free to fork this repository, make improvements, and submit pull requests!
Suggestions and enhancements are always welcome 🙌

## 🪪 License

## This project is licensed under the MIT License — you’re free to use, modify, and distribute it.

## ✨ Author
```
Tanmoy Naskar
```

“Generate. Encode. Share — all from your command line.” 🚀
