
import subprocess
import re
import sys

try:
    import wmi
except ImportError:
    print("wmi module not found. Please run: pip install wmi")
    sys.exit(1)

def check_antivirus_status():
    print("\n[+] Checking Antivirus Status...\n")
    try:
        w = wmi.WMI(namespace="root\\SecurityCenter2")
        antivirus_found = False
        for av in w.AntiVirusProduct():
            print(f"Name: {av.displayName}")
            print(f"Path: {av.pathToSignedProductExe}")
            print(f"State: {av.productState}\n")
            antivirus_found = True
        if not antivirus_found:
            print("No antivirus found!")
    except Exception as e:
        print(f"Error checking antivirus: {e}")

def check_firewall_status():
    print("\n[+] Checking Firewall Status...\n")
    try:
        result = subprocess.run(
            ['netsh', 'advfirewall', 'show', 'allprofiles'],
            capture_output=True, text=True
        )
        print(result.stdout)
    except Exception as e:
        print(f"Error checking firewall: {e}")

def check_open_ports():
    print("\n[+] Checking Open Ports...\n")
    try:
        result = subprocess.run(
            ['netstat', '-an'],
            capture_output=True, text=True
        )
        print(result.stdout)
    except Exception as e:
        print(f"Error checking open ports: {e}")

def check_windows_update_status():
    print("\n[+] Checking Windows Update Status...\n")
    try:
        cmd = 'powershell "Get-Service -Name wuauserv"'
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
        if out:
            print(out.decode())
        if err:
            print("Error:", err.decode())
    except Exception as e:
        print(f"Error checking updates: {e}")

def check_password_strength():
    print("\n[+] Password Strength Checker\n")
    password = input("Enter a password to check: ")
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[ @!#$%^&*()<>?/\\|}{~:]", password) is None

    if length_error:
        print("Password must be at least 8 characters long.")
    if digit_error:
        print("Password should include at least one digit.")
    if uppercase_error:
        print("Password should include at least one uppercase letter.")
    if lowercase_error:
        print("Password should include at least one lowercase letter.")
    if symbol_error:
        print("Password should include at least one special character.")
    if not (length_error or digit_error or uppercase_error or lowercase_error or symbol_error):
        print("✅ Password looks strong!")

def main_menu():
    while True:
        print("\n=== Personal Cyber Hygiene Checker ===")
        print("1. Check Antivirus Status")
        print("2. Check Firewall Status")
        print("3. Check Open Ports")
        print("4. Check Windows Update Status")
        print("5. Password Strength Checker")
        print("6. Exit")
        choice = input("Select an option (1-6): ")

        if choice == '1':
            check_antivirus_status()
        elif choice == '2':
            check_firewall_status()
        elif choice == '3':
            check_open_ports()
        elif choice == '4':
            check_windows_update_status()
        elif choice == '5':
            check_password_strength()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-6.")

if __name__ == "__main__":
    main_menu()

