from base64 import b64encode

from flask import Flask, request, jsonify

import ai_descr_vit_gpt2

app = Flask(__name__)


@app.route('/ai_descr_vit_gpt2', methods=['POST'])
def get_exif_timestamp():
    if 'file' not in request.files:
        return jsonify({"error": "missing 'file' form data"}), 400
    file = request.files['file']

    description = ai_descr_vit_gpt2.describe(file)

    return jsonify({
        "description": description,
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
