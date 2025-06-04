from flask import Flask, request, jsonify
import logging
from cipher.rsa import RSACipher

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# RSA CIPHER ALGORITHM
rsa_cipher = RSACipher()

@app.route('/api/rsa/generate_keys', methods=['GET'])
def rsa_generate_keys():
    rsa_cipher.generate_keys()
    return jsonify({'message': 'Keys generated successfully'})

@app.route("/api/rsa/encrypt", methods=["POST"])
def rsa_encrypt():
    data = request.json
    message = data['message']
    key_type = data['key_type']

    private_key, public_key = rsa_cipher.load_keys()

    if key_type == 'public':
        key = public_key
    elif key_type == 'private':
        key = private_key
    else:
        return jsonify({'error': 'Invalid key type'})

    encrypted_message = rsa_cipher.encrypt(message, key)
    encrypted_hex = encrypted_message.hex()

    return jsonify({'encrypted_message': encrypted_hex})

@app.route("/api/rsa/decrypt", methods=["POST"])
def rsa_decrypt():
    data = request.json
    ciphertext_hex = data['ciphertext']
    key_type = data['key_type']

    private_key, public_key = rsa_cipher.load_keys()

    if key_type == 'public':
        key = public_key
    elif key_type == 'private':
        key = private_key
    else:
        return jsonify({'error': 'Invalid key type'})

    ciphertext = bytes.fromhex(ciphertext_hex)
    decrypted_message = rsa_cipher.decrypt(ciphertext, key)

    return jsonify({'decrypted_message': decrypted_message})

@app.route('/api/rsa/sign', methods=['POST'])
def rsa_sign_message():
    try:
        logger.debug("Received request to sign message")
        data = request.json
        message = data.get('message')

        if not message:
            logger.warning("No message provided")
            return jsonify({'error': 'No message provided'}), 400

        private_key, _ = rsa_cipher.load_keys()  # Fixed here
        logger.debug("Private key loaded successfully")

        signature = rsa_cipher.sign(message, private_key)
        signature_hex = signature.hex()
        logger.debug("Message signed successfully")

        return jsonify({'signature': signature_hex})
    except ValueError as e:
        logger.error(f"ValueError during signing: {str(e)}")
        return jsonify({'error': f'Data format error: {str(e)}'}), 500
    except Exception as e:
        logger.error(f"Unexpected error during signing: {str(e)}")
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500

@app.route('/api/rsa/verify', methods=['POST'])
def rsa_verify_signature():
    try:
        logger.debug("Received request to verify signature")
        data = request.json
        message = data.get('message')
        signature_hex = data.get('signature')

        if not message:
            logger.warning("No message provided")
            return jsonify({'error': 'No message provided'}), 400
        if not signature_hex:
            logger.warning("No signature provided")
            return jsonify({'error': 'No signature provided'}), 400

        _, public_key = rsa_cipher.load_keys()  # Fixed here
        logger.debug("Public key loaded successfully")

        signature = bytes.fromhex(signature_hex)
        is_verified = rsa_cipher.verify(message, signature, public_key)
        logger.debug(f"Verification result: {is_verified}")

        return jsonify({'is_verified': is_verified})
    except ValueError as e:
        logger.error(f"ValueError during verification: {str(e)}")
        return jsonify({'error': f'Data format error: {str(e)}'}), 500
    except Exception as e:
        logger.error(f"Unexpected error during verification: {str(e)}")
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500

# Main function
if __name__ == "__main__":
    logger.info("Starting Flask application")
    app.run(host="0.0.0.0", port=5000, debug=True)