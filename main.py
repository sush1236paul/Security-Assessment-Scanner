import subprocess

def show_menu():
    print("\n===== NMAP AUTOMATION TOOL =====")
    print("1. Stealth Scan (-sS)")
    print("2. Service Version Detection (-sV)")
    print("3. OS Detection (-O)")
    print("4. Aggressive Scan (-A)")
    print("5. UDP Scan (-sU)")
    print("6. Vulnerability Scripts (--script vuln)")
    print("7. Custom Nmap Option")
    print("0. Start Scan")

def main():
    target = input("Enter target IP/Domain: ")

    options = []

    while True:
        show_menu()
        choice = input("Select option: ")

        if choice == "1":
            options.append("-sS")

        elif choice == "2":
            options.append("-sV")

        elif choice == "3":
            options.append("-O")

        elif choice == "4":
            options.append("-A")

        elif choice == "5":
            options.append("-sU")

        elif choice == "6":
            options.extend(["--script", "vuln"])

        elif choice == "7":
            custom = input("Enter custom Nmap option: ")
            options.append(custom)

        elif choice == "0":
            break

        else:
            print("Invalid choice!")

    command = ["nmap"] + options + [target]

    print("\nRunning:")
    print(" ".join(command))
    print("-" * 50)

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        print(result.stdout)

        if result.stderr:
            print("\nErrors:")
            print(result.stderr)

    except FileNotFoundError:
        print("Nmap is not installed or not in PATH.")

if __name__ == "__main__":
    main()
