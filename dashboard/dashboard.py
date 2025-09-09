from flask import Flask, jsonify, render_template_string
import requests
import pandas as pd
from datetime import datetime
import plotly.express as px

app = Flask(__name__)
DATA_URL = 'http://localhost:5000/data_log'

def get_graphs():
    """Fetch data and generate Plotly figures as HTML divs"""
    response = requests.get(DATA_URL)
    data = pd.DataFrame(response.json())

    if data.empty:
        return "<h2>No data available yet. Run the simulator.</h2>", "", ""

    # Video histogram (dark template)
    fig_video = px.histogram(
        data, x='video_class',
        title='Video-based Pollinator Detections',
        color='video_class',
        color_discrete_map={
            'bee': 'gold',
            'butterfly': 'orange',
            'hummingbird': 'lime',
            'dragonfly': 'cyan',
            'none': 'gray'
        },
        template='plotly_dark'
    )

    # Audio histogram (dark template)
    fig_audio = px.histogram(
        data, x='audio_class',
        title='Audio-based Pollinator Detections',
        color='audio_class',
        color_discrete_map={
            'bee_sound': 'gold',
            'hummingbird_sound': 'lime',
            'no_sound': 'gray'
        },
        template='plotly_dark'
    )

    # Humidity line chart (dark template)
    fig_humidity = px.line(
        data, x='timestamp', y='humidity',
        title='Humidity Over Time',
        markers=True,
        template='plotly_dark'
    )

    return fig_video.to_html(full_html=False), fig_audio.to_html(full_html=False), fig_humidity.to_html(full_html=False)

@app.route('/')
def dashboard():
    fig_video, fig_audio, fig_humidity = get_graphs()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Pollinator Monitoring Dashboard</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@5.3.1/dist/darkly/bootstrap.min.css">
        <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
        <style>
            body { background-color: #121212; color: #f1f1f1; }
            .card { background-color: #1e1e1e; color: #f1f1f1; }
            .card-title { font-weight: bold; }
            h1 { color: #f1f1f1; }
            #last-updated { color: #cccccc; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1 class="text-center mt-4 mb-2">Pollinator Monitoring Dashboard</h1>
            <p class="text-center text-muted" id="last-updated">Last updated: {{ current_time }}</p>

            <div class="row">
                <div class="col-md-6 mb-4">
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-title text-center">Video Detections</h5>
                            <div id="video-graph">{{ fig_video|safe }}</div>
                        </div>
                    </div>
                </div>

                <div class="col-md-6 mb-4">
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-title text-center">Audio Detections</h5>
                            <div id="audio-graph">{{ fig_audio|safe }}</div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="row">
                <div class="col-md-12 mb-4">
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-title text-center">Humidity Over Time</h5>
                            <div id="humidity-graph">{{ fig_humidity|safe }}</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <script>
        function refreshGraphs() {
            $.get("/graphs_data", function(data) {
                $("#video-graph").html(data.video);
                $("#audio-graph").html(data.audio);
                $("#humidity-graph").html(data.humidity);
                $("#last-updated").text("Last updated: " + data.timestamp);
            });
        }

        // Refresh every 5 seconds
        setInterval(refreshGraphs, 5000);
        </script>
    </body>
    </html>
    """
    return render_template_string(template,
                                  fig_video=fig_video,
                                  fig_audio=fig_audio,
                                  fig_humidity=fig_humidity,
                                  current_time=current_time)

@app.route('/graphs_data')
def graphs_data():
    fig_video, fig_audio, fig_humidity = get_graphs()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({
        'video': fig_video,
        'audio': fig_audio,
        'humidity': fig_humidity,
        'timestamp': timestamp
    })

if __name__ == '__main__':
    app.run(port=8000)
