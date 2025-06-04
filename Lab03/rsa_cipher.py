import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.rsa import Ui_RSACipher
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_RSACipher()
        self.ui.setupUi(self)

        # Connect buttons to their respective functions
        self.ui.btn_gen_keys.clicked.connect(self.call_api_gen_keys)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
        self.ui.btn_sign.clicked.connect(self.call_api_sign)
        self.ui.btn_verify.clicked.connect(self.call_api_verify)

    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5000/api/rsa/generate_keys"

        try:
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText(data["message"])
                msg.exec_()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText(f"API error: Status code {response.status_code}")
                msg.exec_()

        except requests.exceptions.RequestException as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(f"Error: {str(e)}")
            msg.exec_()

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/encrypt"
        payload = {
            "message": self.ui.txt_plain_text.toPlainText(),
            "key_type": "public"
        }

        try:
            if not payload["message"]:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Please enter a message to encrypt")
                msg.exec_()
                return

            response = requests.post(url, json=payload)

            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setPlainText(data["encrypted_message"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted successfully")
                msg.exec_()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText(f"API error: Status code {response.status_code}")
                msg.exec_()

        except requests.exceptions.RequestException as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(f"Error: {str(e)}")
            msg.exec_()

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/decrypt"
        payload = {
            "ciphertext": self.ui.txt_cipher_text.toPlainText(),
            "key_type": "private"
        }

        try:
            if not payload["ciphertext"]:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Please enter a ciphertext to decrypt")
                msg.exec_()
                return

            response = requests.post(url, json=payload)

            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setPlainText(data["decrypted_message"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted successfully")
                msg.exec_()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText(f"API error: Status code {response.status_code}")
                msg.exec_()

        except requests.exceptions.RequestException as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(f"Error: {str(e)}")
            msg.exec_()

    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/rsa/sign"
        payload = {
            "message": self.ui.txt_info.toPlainText(),
        }

        try:
            if not payload["message"]:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Please enter a message to sign")
                msg.exec_()
                return

            response = requests.post(url, json=payload)

            if response.status_code == 200:
                data = response.json()
                self.ui.txt_sign.setPlainText(data["signature"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Signed successfully")
                msg.exec_()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText(f"API error: Status code {response.status_code}")
                msg.exec_()

        except requests.exceptions.RequestException as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(f"Error: {str(e)}")
            msg.exec_()

    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/rsa/verify"
        payload = {
            "message": self.ui.txt_info.toPlainText(),
            "signature": self.ui.txt_sign.toPlainText()
        }

        try:
            if not payload["message"]:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Please enter a message to verify")
                msg.exec_()
                return
            if not payload["signature"]:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Please enter a signature to verify")
                msg.exec_()
                return

            response = requests.post(url, json=payload)

            if response.status_code == 200:
                data = response.json()
                if data["is_verified"]:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Verified successfully")
                    msg.exec_()
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Verification failed")
                    msg.exec_()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText(f"API error: Status code {response.status_code}")
                msg.exec_()

        except requests.exceptions.RequestException as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(f"Error: {str(e)}")
            msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())