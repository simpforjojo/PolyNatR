import random
import time
import requests

SERVER_URL = 'http://localhost:5000/data'

# Video files in sample_data/videos/
video_files = [
    './sample_data/videos/bbf.mp4',
    './sample_data/videos/bbf1.mp4',
    './sample_data/videos/bbpol.mp4',
    './sample_data/videos/bbpol1.mp4',
    './sample_data/videos/bbpol2.mp4',
    './sample_data/videos/bfpol.mp4',
    './sample_data/videos/dragonfly.mp4',
    './sample_data/videos/hbf.mp4',
    './sample_data/videos/hbf1.mp4',
    './sample_data/videos/none.mp4'
]

# Audio files in sample_data/audio/
audio_files = [
    './sample_data/audio/beebuzz.wav',
    './sample_data/audio/beebuzz1.wav',
    './sample_data/audio/beeland.wav',
    './sample_data/audio/hbflap.wav',
    './sample_data/audio/hbflap1.wav',
    './sample_data/audio/none.wav'
]

def generate_data():
    """
    Generates a random sensor payload simulating an IoT node.
    """
    return {
        'device_id': 'node_1',
        'temperature': round(random.uniform(20, 35), 2),
        'humidity': round(random.uniform(30, 80), 2),
        'light': random.randint(100, 1000),
        'gps_lat': 12.9716 + random.uniform(-0.001, 0.001),
        'gps_long': 77.5946 + random.uniform(-0.001, 0.001),
        'video_path': random.choice(video_files),
        'audio_path': random.choice(audio_files)
    }

def send_data(data):
    """
    Sends data to the backend server.
    """
    try:
        requests.post(SERVER_URL, json=data)
        print(f"Sent data: {data['video_path']} + {data['audio_path']}")
    except Exception as e:
        print(f"Failed to send data: {e}")

if __name__ == '__main__':
    while True:
        data = generate_data()
        send_data(data)
        time.sleep(5)  # Sends data every 5 seconds

