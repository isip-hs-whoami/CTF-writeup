# Problem: CTF@CIT 2025 XOR - 942 / Crypto
# Version: 20250429
# Coder: A.Tao

import base64


## ROT47 function
def rot47(text):
    result = ""
    for char in text:
        c = ord(char)
        if 33 <= c <= 126:
            result += chr(33 + ((c - 33 + 47) % 94))
        else:
            result += char
    return result


# base32 decoding
data_b32 = "PFFUQYTUONPSK5LAMNDXGJ35ER4CM5C7ORETY3A="
decoded_b32 = base64.b32decode(data_b32)
print("BASE32解碼:", decoded_b32.decode(errors="ignore"))

# ROT47 decoding
decoded_rot47 = rot47(decoded_b32.decode(errors="ignore"))
print("ROT47解碼:", decoded_rot47)

# base64 decoding
decoded_b64 = base64.b64decode(decoded_rot47)
print("BASE64解碼:", decoded_b64)

# XOR recircle-key calculation
known_plaintext = "CIT{"
partial_key = []

for i in range(len(known_plaintext)):
    k = decoded_b64[i] ^ ord(known_plaintext[i])
    partial_key.append(k)

# Print key (byte values and ASCII if printable)
print("XOR Key Bytes:", partial_key)
print("XOR ASCII Key:", "".join(chr(k) if 32 <= k < 127 else "." for k in partial_key))


# full decryption
def xor_decrypt(text, key_bytes):
    result = ""
    for i, char in enumerate(text):
        result += chr(char ^ key_bytes[i % len(key_bytes)])
    return result


final_plaintext = xor_decrypt(decoded_b64, partial_key)
print("最終明文結果:", final_plaintext)
