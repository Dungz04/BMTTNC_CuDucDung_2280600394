import sys
from PIL import Image

def decode_image(encoded_image_path):
    img = Image.open(encoded_image_path)
    width, height = img.size

    binary_message = ""

    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))

            for color_channel in range(3):  # RGB
                binary_message += format(pixel[color_channel], '08b')[-1]

    # Tách thành các ký tự 8-bit và tìm ký tự kết thúc '\0'
    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        char = chr(int(byte, 2))
        if char == '\0':
            break
        message += char

    return message

def main():
    if len(sys.argv) != 2:
        print("Cách sử dụng: python decrypt.py <ảnh_đã_mã_hóa>")
        return

    encoded_image_path = sys.argv[1]
    decoded_message = decode_image(encoded_image_path)
    print("📩 Thông điệp đã giải mã:", decoded_message)

if __name__ == "__main__":
    main()