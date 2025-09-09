# ml/video_classifier.py
import os

# Mapping from filenames to pollinator types
VIDEO_LABELS = {
    'bbf.mp4': 'butterfly',
    'bbf1.mp4': 'butterfly',
    'bbpol.mp4': 'bee',
    'bbpol1.mp4': 'bee',
    'bbpol2.mp4': 'bee',
    'bfpol.mp4': 'bee',
    'dragonfly.mp4': 'dragonfly',
    'hbf.mp4': 'hummingbird',
    'hbf1.mp4': 'hummingbird',
    'none.mp4': 'none'
}

def classify_video(video_path):
    filename = os.path.basename(video_path)
    return VIDEO_LABELS.get(filename, 'none')  # Default to 'none'

