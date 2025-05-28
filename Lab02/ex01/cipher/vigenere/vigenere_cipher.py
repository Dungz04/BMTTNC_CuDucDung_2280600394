class VigenereCipher:
    
    def __init__(self):
        pass

    def vigenere_encrypt(self, plain_text, key):
        encrypted_text = ""
        key_index = 0

        for char in plain_text:
            if char.isalpha():
                # Tính toán độ dịch của key (chuyển sang chữ hoa và tính theo chữ cái)
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')

                if char.isupper():
                    # Mã hóa chữ hoa
                    encrypted_text += chr((ord(char) - ord('A') + key_shift) % 26 + ord('A'))
                else:
                    # Mã hóa chữ thường
                    encrypted_text += chr((ord(char) - ord('a') + key_shift) % 26 + ord('a'))

                key_index += 1
            else:
                # Giữ nguyên ký tự không phải là chữ cái
                encrypted_text += char

        return encrypted_text

    def vigenere_decrypt(self, encrypted_text, key):
        decrypted_text = ""
        key_index = 0

        for char in encrypted_text:
            if char.isalpha():
                # Tính toán độ dịch của key (chuyển sang chữ hoa và tính theo chữ cái)
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')

                if char.isupper():
                    # Giải mã chữ hoa
                    decrypted_text += chr((ord(char) - ord('A') - key_shift) % 26 + ord('A'))
                else:
                    # Giải mã chữ thường
                    decrypted_text += chr((ord(char) - ord('a') - key_shift) % 26 + ord('a'))

                key_index += 1
            else:
                # Giữ nguyên ký tự không phải là chữ cái
                decrypted_text += char

        return decrypted_text