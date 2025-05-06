# CTF@CIT 2025

---

Contributed by A.Tao

# Rotten - 304 / Crypto

---

> PVG{LxxdJwAXJGcsDoncKfRctddA}  
> Flag Format: CIT{example_flag}  
> by **ronnie**  
> 

## Solution

---

- PVG{LxxdJwAXJGcsDoncKfRctddA}看起來像是對字母進行ROT的加密。
- 將PVG{LxxdJwAXJGcsDoncKfRctddA}用 dcode的ROT Cipher ([https://www.dcode.fr/rot-cipher](https://www.dcode.fr/rot-cipher)) 進行Brute-Force方式的解密。
- 在 [A-Z]+13 (ROT13)的結果可得 flag: CIT{YkkqWjNKWTpfQbapXsEpgqqN}。
- Done.

# XOR - 942 / Crypto

---

> PFFUQYTUONPSK5LAMNDXGJ35ER4CM5C7ORETY3A=  
> Flag Format: CIT{example_flag}  
> by ronnie  
> 

## Solution

- 因字串末有”=”，且所有字元皆在[A-Z,2-7]範圍內，故以base32解碼”PFFUQYTUONPSK5LAMNDXGJ35ER4CM5C7ORETY3A=”，得”yKHbts_%u`cGs'}$x&t_tI<l”。
    
    ```python
    import base64
    data_b32 = "PFFUQYTUONPSK5LAMNDXGJ35ER4CM5C7ORETY3A="
    decoded_b32 = base64.b32decode(data_b32)
    print(decoded_b32.decode(errors="ignore"))
    ```
    
- 因字串””yKHbts_%u`cGs'}$x&t_tI<l”所有字元皆在ASCII[!-~] (即 33 ~ 126 )範圍內，故以ROT47解碼，得”Jzw3ED0TF14vDVNSIUE0Exk=”。
    
    ```python
    def rot47(text):
        result = ''
        for char in text:
            c = ord(char)
            if 33 <= c <= 126:
                result += chr(33 + ((c - 33 + 47) % 94))
            else:
                result += char
        return result
    
    decoded_rot47 = rot47(decoded.decode(errors="ignore"))
    print(decoded_rot47)
    ```
    
- 對”Jzw3ED0TF14vDVNSIUE0Exk=”做 base64 decode，可得bytes字串 b"'<7\x10=\x13\x17^/\rSR!A4\x13\x19”
    
    ```python
    decoded_b64 = base64.b64decode(decoded_rot47)
    print("BASE64解碼:", decoded_b64)
    ```
    
- 因題目為XOR，應有XOR加密步驟，但進行單一字元的XOR，找不到CIT{開頭的明文。
- 反推XOR加密的key，將已知明文字首”CIT{”與前步base64解碼後的前4個字元進行XOR運算，可得key: “duck”
    
    ```python
    # XOR recircle-key calculation
    known_plaintext = "CIT{"
    partial_key = []
    
    for i in range(len(known_plaintext)):
        k = decoded_b64[i] ^ ord(known_plaintext[i])
        partial_key.append(k)
    
    # Print key (byte values and ASCII if printable)
    print("XOR Key Bytes:", partial_key)
    print("XOR ASCII Key:", "".join(chr(k) if 32 <= k < 127 else "." for k in partial_key))
    ```
    
- 進行 XOR+key的循環解密，得明文(flag) CIT{Yft5Kx09E4Wx}
    
    ```python
    # full decryption
    def xor_decrypt(text, key_bytes):
        result = ""
        for i, char in enumerate(text):
            result += chr(char ^ key_bytes[i % len(key_bytes)])
        return result
    
    final_plaintext = xor_decrypt(decoded_b64, partial_key)
    print("最終明文結果:", final_plaintext)
    ```
    
- 完整Python程式碼
    
    [CTFCIT2025_xor.py](CTFCIT2025_xor.py)
    
- Done.

# Reference

---

- [XOR - 942 / Crypto Reference 1](https://yocchin.hatenablog.com/entry/2025/04/28/084224) ([https://yocchin.hatenablog.com/entry/2025/04/28/084224](https://yocchin.hatenablog.com/entry/2025/04/28/084224))
- [XOR - 942 / Crypto Reference 2](https://chatgpt.com/share/68103787-42b4-800f-b393-952a182488e0) ([https://chatgpt.com/share/68103787-42b4-800f-b393-952a182488e0](https://chatgpt.com/share/68103787-42b4-800f-b393-952a182488e0))
