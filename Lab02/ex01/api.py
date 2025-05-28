from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.playfair import PlayFairCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)
caesar_cipher = CaesarCipher()
playfair_cipher = PlayFairCipher()
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()
transposition_cipher = TranspositionCipher()

#-----------------------------Caesar----------------------------
@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.get_json()
    if not data or 'plain_text' not in data or 'key' not in data:
        return jsonify({'error': 'Missing plain_text or key'}), 400
    plain_text = data['plain_text']
    try:
        key = int(data['key'])
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid key. Please provide a valid integer.'}), 400
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.get_json()
    if not data or 'cipher_text' not in data or 'key' not in data:
        return jsonify({'error': 'Missing cipher_text or key'}), 400
    cipher_text = data['cipher_text']
    try:
        key = int(data['key'])
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid key. Please provide a valid integer.'}), 400
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

#-----------------------------Vigenere----------------------------
@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.get_json()
    if not data or 'plain_text' not in data or 'key' not in data:
        return jsonify({'error': 'Missing plain_text or key'}), 400
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.get_json()
    if not data or 'cipher_text' not in data or 'key' not in data:
        return jsonify({'error': 'Missing cipher_text or key'}), 400
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

#-----------------------------Playfair----------------------------
@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    data = request.get_json()
    if not data or 'key' not in data:
        return jsonify({'error': 'Missing key'}), 400
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({"playfair_matrix": playfair_matrix})

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.get_json()
    if not data or 'plain_text' not in data or 'key' not in data:
        return jsonify({'error': 'Missing plain_text or key'}), 400
    plain_text = data['plain_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.encrypt(plain_text, playfair_matrix)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.get_json()
    if not data or 'cipher_text' not in data or 'key' not in data:
        return jsonify({'error': 'Missing cipher_text or key'}), 400
    cipher_text = data['cipher_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.decrypt(cipher_text, playfair_matrix)
    return jsonify({'decrypted_text': decrypted_text})

#-----------------------------Railfence----------------------------
@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = request.get_json()
    if not data or 'plain_text' not in data or 'key' not in data:
        return jsonify({'error': 'Missing plain_text or key'}), 400
    plain_text = data['plain_text']
    try:
        key = int(data['key'])
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid key. Please provide a valid integer.'}), 400
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = request.get_json()
    if not data or 'cipher_text' not in data or 'key' not in data:
        return jsonify({'error': 'Missing cipher_text or key'}), 400
    cipher_text = data['cipher_text']
    try:
        key = int(data['key'])
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid key. Please provide a valid integer.'}), 400
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

#-----------------------------Transposition----------------------------
@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    data = request.get_json()
    if not data or 'plain_text' not in data or 'key' not in data:
        return jsonify({'error': 'Missing plain_text or key'}), 400
    plain_text = data['plain_text']
    try:
        key = int(data['key'])
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid key. Please provide a valid integer.'}), 400
    encrypted_text = transposition_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    data = request.get_json()
    if not data or 'cipher_text' not in data or 'key' not in data:
        return jsonify({'error': 'Missing cipher_text or key'}), 400
    cipher_text = data['cipher_text']
    try:
        key = int(data['key'])
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid key. Please provide a valid integer.'}), 400
    decrypted_text = transposition_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)