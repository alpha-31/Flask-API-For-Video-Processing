from flask import Flask, request, jsonify
import os
import cv2
import filetype

app = Flask(__name__)

@app.route('/' , methods=['GET'])
def mainroute():
    return "Flask API For Video Processing"


if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.secret_key = os.urandom(24)
    app.run(host=host, port=port)
