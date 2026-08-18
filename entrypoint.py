#!/usr/bin/env python3
"""Stack Smasher — overflow to win() leaks the decryption seed (fernet delivery)."""
import os, sys
sys.path.insert(0, "/challenge/_shared")
from fetch_material import fetch_material

CHALLENGE_KEY = os.environ.get("CHALLENGE_KEY", "ret2win-canary")

def main():
    mat = fetch_material()
    with open("/challenge/flag.enc", "w") as f:
        f.write(mat["delivery_blob"])
    with open("/challenge/core.dump", "w") as f:
        f.write(f"[fault] saved return address overwritten\n[win] recovered seed: {CHALLENGE_KEY}\n")
    print('flag.enc is Fernet ciphertext. core.dump shows the seed win() prints.')
    print('Derive the Fernet key from the seed and decrypt flag.enc.')

if __name__ == "__main__":
    main()
