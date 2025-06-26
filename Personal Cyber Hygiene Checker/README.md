# 🛡️ Personal Cyber Hygiene Checker

A Python-based command-line utility that helps Windows users evaluate their cybersecurity hygiene. It provides quick checks for antivirus, firewall, open ports, Windows updates, and password strength — all from one interactive menu.

---

## 📋 Features

- ✅ Check Antivirus Status  
- 🔥 Check Firewall Profiles  
- 🌐 List Open Network Ports  
- 🛠️ Verify Windows Update Service  
- 🔐 Password Strength Tester

---

## 🖥️ Getting Started

These instructions will get your copy of the project up and running on your local machine for development and testing.

---

## 🚀 Step-by-Step Setup

### 1. Clone the Repository

```bash
git clone https://github.com/JeganFM/Personal-Cyber-Hygiene-Checker.git
cd Personal-Cyber-Hygiene-Checker
```

### 2. Initialize Git (if needed)

If starting fresh:

```bash
git init
git remote add origin https://github.com/JeganFM/Personal-Cyber-Hygiene-Checker.git
```

### 3. Clean Unwanted Files (optional)

If you added extra files/folders to the repo by mistake:

```bash
git rm --cached -r "Folder Name/"
git rm --cached filename.py
```

Then:

```bash
git commit -m "Removed unnecessary files"
git push
```

Example:

```bash
git rm --cached -r "Cash Power Calculator/"
git rm --cached test.py
```

---

## 📦 Install Dependencies

Install the required module:

```bash
pip install wmi
```

💡 Only required for the antivirus check (Windows only).

---

## ▶️ Run the Tool

```bash
python main.py
```

---

## 📸 Interactive Menu

```text
=== Personal Cyber Hygiene Checker ===
1. Check Antivirus Status
2. Check Firewall Status
3. Check Open Ports
4. Check Windows Update Status
5. Password Strength Checker
6. Exit
```

---

## 📁 File Structure

```
main.py              # Core script with all features
README.md            # Documentation
```

---

## 🧰 Requirements

- Python 3.x  
- Windows OS  
- Administrator privileges (for full diagnostics)  
- Internet access (optional)

---

## 📌 Notes

- Only tested on Windows 10/11  
- May not work as expected on Linux or macOS  
- Developed for personal cybersecurity awareness

---

## 📄 License

This project is open-source and free to use. You can modify or expand it as needed.

---

## 🤝 Contributions

Pull requests are welcome! Feel free to open an issue for feature suggestions or bugs.
