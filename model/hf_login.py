from getpass import getpass
from huggingface_hub import login

token = getpass("Enter token: ")
login(token=token)

print("Login successful!")