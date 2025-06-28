def xor_bytes(data: bytes, key: int) -> bytes:
    return bytes([b ^ key for b in data])

key = 123  # Your XOR key (keep this in your app, not obvious)

# Read original model
with open("loan.pkl", "rb") as f:
    model_data = f.read()

# XOR encrypt
encrypted_data = xor_bytes(model_data, key)

# Save to encoded file
with open("loan_encoded.pkl", "wb") as f:
    f.write(encrypted_data)

print("Model encrypted and saved as loan_encoded.pkl")
