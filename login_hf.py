# Quick Login Helper for Hugging Face
import sys
from huggingface_hub import login

if len(sys.argv) < 2:
    print("Usage: python login_hf.py YOUR_TOKEN")
    sys.exit(1)

token = sys.argv[1]
try:
    login(token=token)
    print("[SUCCESS] Successfully logged in to Hugging Face!")
except Exception as e:
    print(f"[FAIL] Login failed: {e}")
