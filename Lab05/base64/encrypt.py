import base64

def main():
    input_string = input("Nhập thông tin cần mã hóa: ")

    # Mã hóa chuỗi sang base64
    encoded_bytes = base64.b64encode(input_string.encode("utf-8"))
    encoded_string = encoded_bytes.decode("utf-8")

    # Ghi chuỗi đã mã hóa vào file
    with open("data.txt", "w") as file:
        file.write(encoded_string)

    print("Đã mã hóa và ghi vào file data.txt")

# Kiểm tra nếu là chương trình chính thì gọi hàm main
if __name__ == "__main__":
    main()