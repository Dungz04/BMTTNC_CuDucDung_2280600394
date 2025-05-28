class TranspositionCipher:
    
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encrypted_text = ""

        # Đọc từng cột trong bảng
        for col in range(key):
            pointer = col

            # Lặp qua tất cả các dòng của cột hiện tại
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key  # Di chuyển chỉ mục để lấy ký tự trong cột tiếp theo

        return encrypted_text

    def decrypt(self, text, key):
        # Tạo một list rỗng để chứa các giá trị giải mã
        decrypted_text = [''] * key

        row, col = 0, 0

        for symbol in text:
            decrypted_text[col] += symbol  # Thêm ký tự vào đúng cột

            col += 1

            # Khi đã đi hết một cột, reset cột và tăng dòng
            if col == key or (col == key - 1 and row >= len(text) % key):
                col = 0
                row += 1

        # Kết hợp các cột lại thành chuỗi hoàn chỉnh
        return ''.join(decrypted_text)