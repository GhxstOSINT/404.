import base64
import codecs

def vigenere_decrypt(text, key):
    key = key.upper()
    result = []
    key_idx = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_idx % len(key)]) - 65
            if char.islower():
                result.append(chr((ord(char) - 97 - shift) % 26 + 97))
            else:
                result.append(chr((ord(char) - 65 - shift) % 26 + 65))
            key_idx += 1
        else:
            result.append(char)
    return "".join(result)

def vigenere_encrypt(text, key):
    key = key.upper()
    result = []
    key_idx = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_idx % len(key)]) - 65
            if char.islower():
                result.append(chr((ord(char) - 97 + shift) % 26 + 97))
            else:
                result.append(chr((ord(char) - 65 + shift) % 26 + 65))
            key_idx += 1
        else:
            result.append(char)
    return "".join(result)

# 1. Your current ciphertext
ciphertext = "P1EZy2oiLjy1oI_j4GuK_gE4i3ea4y_3koo01gD=="

# --- PHASE 1: DECRYPT ---
rot13_reversed = codecs.decode(ciphertext, 'rot_13')
vigenere_reversed = vigenere_decrypt(rot13_reversed, "MAGIC")
# Handle any URL-safe Base64 quirks
clean_b64 = vigenere_reversed.replace('_', '/').replace('-', '+')
original_flag = base64.b64decode(clean_b64).decode()

# --- PHASE 2: SWAP CTF FOR Cruxhunt ---
new_flag = original_flag.replace("CTF", "Cruxhunt")

# --- PHASE 3: RE-ENCRYPT ---
# Note: Using standard Base64 encoding for the new payload
b64_encoded = base64.b64encode(new_flag.encode()).decode()
vigenere_encoded = vigenere_encrypt(b64_encoded, "MAGIC")
final_ciphertext = codecs.encode(vigenere_encoded, 'rot_13')

print(f"[*] Extracted Old Flag: {original_flag}")
print(f"[*] Generated New Flag: {new_flag}")
print("\n=== PASTE THIS NEW CIPHERTEXT INTO disciplinary_log.txt ===")
print(final_ciphertext)