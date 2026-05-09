import base64

# Encoded flag recovered from removed commit
encoded_data = "Q1NDQ1RGe0ZyNG1lXzI3X1c0c19OM3Zlcl9DdXRfRnIwbV9UaDNfU3Qwcnl9"

def decode_base64(encoded: str) -> str:
    decoded_bytes = base64.b64decode(encoded)
    return decoded_bytes.decode("utf-8")

if __name__ == "__main__":
    flag = decode_base64(encoded_data)
    print(f"[*] Encoded  : {encoded_data}")
    print(f"[+] Decoded  : {flag}")
