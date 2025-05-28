
class PlayFairCipher:
    def __init__(self) -> None:
        pass  # Hàm khởi tạo, có thể thêm các thuộc tính nếu cần

    def create_playfair_matrix(self, key: str) -> list:
        # Chuyển đổi key: thay "J" thành "I" và viết hoa
        key = key.replace("J", "I").upper()
        key_set = set(key)  # Tạo tập hợp các ký tự duy nhất từ key
        
        # Tạo bảng chữ cái, bỏ qua "J"
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        # Lấy các chữ cái còn lại không có trong key
        remaining_letters = [letter for letter in alphabet if letter not in key_set]
        
        # Tạo ma trận 5x5
        matrix = list(key)
        for letter in remaining_letters:
            if len(matrix) < 25:  # Đảm bảo ma trận có đúng 25 ký tự
                matrix.append(letter)
            else:
                break
        
        # Chuyển danh sách thành ma trận 5x5
        playfair_matrix = [matrix[i:i+5] for i in range(0, len(matrix), 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix: list, letter: str) -> tuple:
        # Tìm tọa độ của chữ cái trong ma trận
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col
        return None  # Trả về None nếu không tìm thấy

    def decrypt(self, cipher_text: str, matrix: list) -> str:
        cipher_text = cipher_text.upper().replace("J", "I")
        decrypted_text = ""
        
        # Giải mã từng cặp ký tự
        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            if len(pair) < 2:  # Bỏ qua nếu cặp không đủ 2 ký tự
                continue
            
            # Tìm tọa độ của từng ký tự trong cặp
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            
            # Quy tắc giải mã Playfair
            if row1 == row2:  # Cùng hàng
                decrypted_text += matrix[row1][(col1 - 1) % 5]
                decrypted_text += matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:  # Cùng cột
                decrypted_text += matrix[(row1 - 1) % 5][col1]
                decrypted_text += matrix[(row2 - 1) % 5][col2]
            else:  # Hình chữ nhật
                decrypted_text += matrix[row1][col2]
                decrypted_text += matrix[row2][col1]
        
        # Loại bỏ ký tự 'X' được thêm vào khi mã hóa
        result = ""
        i = 0
        while i < len(decrypted_text):
            if i < len(decrypted_text) - 2 and decrypted_text[i+1] == 'X':
                result += decrypted_text[i]
                i += 2
            else:
                result += decrypted_text[i]
                i += 1
        
        # Xử lý ký tự cuối cùng
        if len(decrypted_text) % 2 == 0 or decrypted_text[-1] != 'X':
            result += decrypted_text[-1]
        
        return result