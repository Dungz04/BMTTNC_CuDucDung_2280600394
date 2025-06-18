import sys
from PIL import Image

def encode_image(image_path, message):
    img = Image.open(image_path)
    width, height = img.size

    # Chuyển thông điệp sang nhị phân và thêm ký tự kết thúc '\0'
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += format(0, '08b')  # '\0' kết thúc

    data_index = 0

    for row in range(height):
        for col in range(width):
            pixel = list(img.getpixel((col, row)))

            for color_channel in range(3):  # RGB
                if data_index < len(binary_message):
                    pixel[color_channel] = int(
                        format(pixel[color_channel], '08b')[:-1] + binary_message[data_index],
                        2
                    )
                    data_index += 1

            img.putpixel((col, row), tuple(pixel))

            if data_index >= len(binary_message):
                break
        if data_index >= len(binary_message):
            break

    encoded_image_path = 'encoded_image.png'
    img.save(encoded_image_path)
    print("✅ Ẩn thông điệp thành công! Ảnh đã lưu dưới tên:", encoded_image_path)

def main():
    if len(sys.argv) != 3:
        print("Cách sử dụng: python encrypt.py <đường_dẫn_ảnh> <thông_điệp>")
        return

    image_path = sys.argv[1]
    message = sys.argv[2]
    encode_image(image_path, message)

if __name__ == "__main__":
    main()