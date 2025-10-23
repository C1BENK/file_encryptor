🚀 FILE CRYPTO ULTIMATE

Advanced File Encryption Tool - Protect your files with military-grade AES-256 encryption

✨ FEATURES

· 🔐 AES-256 Encryption - Military-grade encryption for all file types
· 📁 Universal File Support - Encrypt APK, MP4, PDF, EXE, ZIP, and ANY file format
· 🚀 Batch Processing - Encrypt multiple files/folders at once
· 🛡️ Password Tools - Password strength checker and generator
· 💾 Large File Support - Optimized for files up to several GB
· 🎯 User-Friendly Beautiful terminal interface with progress bars

# front view
![alt text](https://github.com/C1BENK/file_encryptor/blob/main/screenshot/foto1.png?raw=true)

🛠️ INSTALLATION

Prerequisites

· Python 3.8 or higher
· pip package manager

Quick Install

```bash
# Clone repository
git clone https://github.com/C1BENK/file_encryptor
cd file_encryptor

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

Manual Install

```bash
pip install pyaes rich pyfiglet
python main.py
```

📋 REQUIREMENTS

```txt
pyaes>=1.6.1
rich>=13.0.0
pyfiglet>=0.8.post1
```

🎮 USAGE

Basic Encryption

```bash
python main.py

# Select menu 1 (Encrypt File)
[+] Enter file path: /path/to/your/file.apk
[+] Enter encryption password: ********
✅ File encrypted successfully!
📁 Output: /path/to/your/file.apk.encrypted
```

Basic Decryption

```bash
python main.py

# Select menu 2 (Decrypt File)  
[+] Enter encrypted file path: /path/to/your/file.apk.encrypted
[+] Enter decryption password: ********
✅ File decrypted successfully!
📁 Output: /path/to/your/file.apk_decrypted
```

📊 SUPPORTED FILE TYPES

Category File Types Examples
📱 Apps APK, EXE, DMG, DEB app.apk, program.exe
🎬 Media MP4, AVI, MKV, MP3, WAV video.mp4, music.mp3
📄 Documents PDF, DOC, XLS, PPT, TXT document.pdf, data.xlsx
🖼️ Images JPG, PNG, GIF, BMP, WEBP photo.jpg, image.png
📦 Archives ZIP, RAR, 7Z, TAR backup.zip, files.rar
💾 Other ANY binary file database.db, config.bin

✅ Supports ALL file types - No limitations!

# example
![alt text](https://github.com/C1BENK/file_encryptor/blob/main/screenshot/foto.png?raw=true)

🔧 TECHNICAL DETAILS

Encryption Algorithm

· AES-256 in CBC mode
· PBKDF2 key derivation with 100,000 iterations
· Random salt (16 bytes) for each file
· Random IV (16 bytes) for each encryption
· Chunk-based processing for large files

Security Features

· ✅ Military-grade AES-256 encryption
· ✅ Salted password hashing
· ✅ Protection against brute force attacks
· ✅ Secure random number generation
· ✅ No data size limitations

💡 EXAMPLES

Encrypt Android APK

```bash
python main.py
# Menu 1 → /sdcard/app.apk → mypassword
# Output: app.apk.encrypted
```

Encrypt Video File

```bash
python main.py
# Menu 1 → /videos/movie.mp4 → videopass123
# Output: movie.mp4.encrypted
```

Batch Encrypt Folder

```bash
python main.py
# Menu 3 → /sdcard/Documents → folderpass
# Encrypts all files in the folder
```

Check Password Strength

```bash
python main.py
# Menu 4 → Option 1 → Enter password
# Provides detailed security analysis
```

⚡ PERFORMANCE

File Size Encryption Time Decryption Time
< 1 MB < 1 second < 1 second
1-10 MB 1-3 seconds 1-3 seconds
10-100 MB 3-10 seconds 3-10 seconds
100+ MB 10-30 seconds 10-30 seconds

Times may vary based on system performance

🛡️ SECURITY WARNING

⚠️ IMPORTANT SECURITY NOTES:

· Never lose your password - Encrypted files cannot be recovered without it
· Backup original files before encryption
· Use strong passwords with mix of characters, numbers, and symbols
· Keep passwords secure and never share encrypted files without passwords

🐛 TROUBLESHOOTING

Common Issues

"File not found"

· Check file path spelling
· Ensure file permissions allow reading

"Decryption failed"

· Verify correct password
· Ensure file was encrypted with this tool
· Check file integrity

"Permission denied"

· Run with appropriate permissions
· Check file/folder access rights

Performance Tips

· Close other applications during large file encryption
· Use SSD storage for better performance
· For very large files, consider batch processing

🤝 CONTRIBUTING

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

Development Setup

```bash
git clone https://github.com/C1BENK/file_encryptor
cd file_encryptor
pip install -r requirements.txt
```

📄 LICENSE

This project is licensed under the MIT License - see the LICENSE file for details.

Educational Purpose Only - Use responsibly and ethically.

👨‍💻 DEVELOPER

C1BENK/Wh04ami
---

<div align="center">

⭐ Star this repo if you find it useful!

</div>

🆘 NEED HELP?

If you encounter any issues:

1. Check the troubleshooting section above
2. Open an issue on GitHub
3. Ensure you're using the latest version

Remember: With great power comes great responsibility. Always use encryption tools ethically! 🔐
