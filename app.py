# app.py

from flask import Flask, Response, jsonify
from camera import get_stream, move_camera

app = Flask(__name__)

@app.route('/stream')
def stream():
    def generate():
        response = get_stream()
        for chunk in response.iter_content(chunk_size=1024):
            yield chunk
    return Response(generate(), content_type='multipart/x-mixed-replace; boundary=frame')

@app.route('/ptz/<direction>')
def ptz(direction):
    result = move_camera(direction)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
