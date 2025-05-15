from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization
from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/generate', methods=['GET'])
def generate_keys():
    private_key = ed25519.Ed25519PrivateKey.generate()
    public_key = private_key.public_key()

    # Serialize the private key in PEM (PKCS8 format)
    private_key_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.OpenSSH,
        encryption_algorithm=serialization.NoEncryption()
    )

    # Serialize the public key in OpenSSH format
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.OpenSSH,
        format=serialization.PublicFormat.OpenSSH
    )

    return jsonify({
        "private_key": private_key_bytes.decode('utf-8'),
        "public_key": public_key_bytes.decode('utf-8')
    })

if __name__ == '__main__':
    app.run(debug=True)
