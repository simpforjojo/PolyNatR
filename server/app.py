from flask import Flask, request, jsonify
import pandas as pd
from ml.video_classifier import classify_video
from ml.audio_classifier import classify_audio
from .actuator_logic import check_and_trigger

app = Flask(__name__)

# In-memory data log
data_log = pd.DataFrame(columns=[
    'timestamp', 'device_id', 'temperature', 'humidity', 'light',
    'gps_lat', 'gps_long', 'video_class', 'audio_class', 'intervention'
])

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    video_class = classify_video(data['video_path'])
    audio_class = classify_audio(data['audio_path'])

    intervention = check_and_trigger(video_class, audio_class, data['humidity'])

    record = {
        'timestamp': pd.Timestamp.now(),
        'device_id': data['device_id'],
        'temperature': data['temperature'],
        'humidity': data['humidity'],
        'light': data['light'],
        'gps_lat': data['gps_lat'],
        'gps_long': data['gps_long'],
        'video_class': video_class,
        'audio_class': audio_class,
        'intervention': intervention
    }

    global data_log
    data_log = pd.concat([data_log, pd.DataFrame([record])], ignore_index=True)

    return jsonify({'status': 'success'}), 200

@app.route('/data_log', methods=['GET'])
def get_data_log():
    return data_log.to_json(orient='records')

if __name__ == '__main__':
    app.run(debug=True)
