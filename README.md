# Pollinator Monitoring Simulation

A real-time pollinator monitoring simulation system built with Python, Flask, and Plotly.
This project simulates IoT nodes sending environmental, video, and audio data to a backend server and visualizes pollinator activity and environmental conditions on an interactive dashboard.

## Features

* Simulated video and audio data streams from pollinator environments.
* Dummy classifiers for video and audio detection (bee, hummingbird, none).
* Real-time dashboard with Plotly charts: pollinator detections and environmental readings.
* Dark-themed UI with auto-refresh every 5 seconds.
* Extensible structure for integrating real ML models and actuator logic.

## Folder Structure

```
pollinator_monitoring_simulation/
│
├── data_simulator.py       # Simulates IoT node data
├── iot_node_simulator.py   # Future expansions
├── server/
│   ├── app.py              # Flask backend
│   ├── actuator_logic.py   # Rules for interventions
│   └── models.py           # Placeholder for ML models
├── ml/
│   ├── __init__.py
│   ├── video_classifier.py # Classifier for video
│   └── audio_classifier.py # Classifier for audio
├── dashboard/
│   └── dashboard.py        # Plotly dashboard
└── sample_data/
    ├── videos/
    └── audio/
```

## Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/pollinator-monitoring-simulation.git
cd pollinator-monitoring-simulation
```

2. Create a virtual environment and activate it:

```
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows
```

3. Install required packages:

```
pip install flask pandas numpy scikit-learn plotly requests opencv-python librosa
```

## Usage

1. Start the backend server:

```
python server/app.py
```

2. Start the dashboard:

```
python dashboard/dashboard.py
```

3. Run the data simulator:

```
python data_simulator.py
```

4. Open your browser at [http://localhost:8000](http://localhost:8000) to view the dashboard.
