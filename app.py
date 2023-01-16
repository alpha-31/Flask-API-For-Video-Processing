from flask import Flask, request, jsonify
import os
import cv2
import filetype

app = Flask(__name__)

@app.route('/' , methods=['GET'])
def mainroute():
    return "Flask API For Video Processing"


@app.route('/process_video/', methods=['POST'])
def process_video():
    file_path = request.json.get('file_path')

    # validate the file path
    if not os.path.isfile(file_path):
        return jsonify({"error": "Invalid file path"}), 400

    # validate the file extension
    if not file_path.endswith(('.mp4')):
        return jsonify({"error": "Invalid file extension are supported"}), 400

    # validate the file format
    try:
        kind = filetype.guess(file_path)
        if kind is None or kind.extension not in ('mp4'):
            return jsonify({"error": "Invalid file format. Only mp4 is supported"}), 400
    except:
        return jsonify({"error": "Invalid video file"}), 400

    # read the video file
    try:
        video = cv2.VideoCapture(file_path)
        total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        video.release()
        return jsonify({"message": "Video processing complete.", "total_frames": total_frames})

    except:
        return jsonify({"error": "Invalid video file"}), 400

if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.secret_key = os.urandom(24)
    app.run(host=host, port=port)
