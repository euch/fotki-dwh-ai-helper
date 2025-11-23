from flask import Flask, request, jsonify

from ai_descr_blip import describe_blip
from ai_descr_blip_2 import describe_blip2
from ai_descr_git import describe_git
from ai_descr_vit_gpt2 import describe_vit_gpt2

app = Flask(__name__)


@app.route('/ai_descr_blip', methods=['POST'])
def get_exif_timestamp():
    if 'file' not in request.files:
        return jsonify({"error": "missing 'file' form data"}), 400

    return jsonify({
        "description": describe_blip(request.files['file']),
    })


@app.route('/ai_descr_blip2', methods=['POST'])
def get_exif_timestamp():
    if 'file' not in request.files:
        return jsonify({"error": "missing 'file' form data"}), 400

    return jsonify({
        "description": describe_blip2(request.files['file']),
    })


@app.route('/ai_descr_git', methods=['POST'])
def get_exif_timestamp():
    if 'file' not in request.files:
        return jsonify({"error": "missing 'file' form data"}), 400

    return jsonify({
        "description": describe_git(request.files['file']),
    })


@app.route('/ai_descr_vit_gpt2', methods=['POST'])
def get_exif_timestamp():
    if 'file' not in request.files:
        return jsonify({"error": "missing 'file' form data"}), 400

    return jsonify({
        "description": describe_vit_gpt2(request.files['file']),
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
