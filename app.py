import os
import subprocess
import hashlib

# Hardcoded secret
API_KEY = "1234567890abcdef"

# Insecure file permissions
filename = "sensitive_data.txt"
os.chmod(filename, 0o777)

# Command injection vulnerability
user_input = input("Enter a command: ")
subprocess.run(user_input, shell=True)  # Dangerous usage

# Use of weak cryptographic function (MD5)
password = "mypassword"
hashed_password = hashlib.md5(password.encode()).hexdigest()
print("Hashed password:", hashed_password)
