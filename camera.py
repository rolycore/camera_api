# camera.py

import requests
from config import CAMERA_IP, CAMERA_PORT, USERNAME, PASSWORD

def get_stream():
    url = f"http://{CAMERA_IP}:{CAMERA_PORT}/video"
    response = requests.get(url, auth=(USERNAME, PASSWORD), stream=True)
    return response

def ptz_control(command):
    url = f"http://{CAMERA_IP}:{CAMERA_PORT}/ptz?cmd={command}"
    response = requests.get(url, auth=(USERNAME, PASSWORD))
    return response.json()

# Ejemplo de comando PTZ (mover cámara)
def move_camera(direction):
    commands = {
        "left": "ptz_move_left",
        "right": "ptz_move_right",
        "up": "ptz_move_up",
        "down": "ptz_move_down"
    }
    return ptz_control(commands[direction])
