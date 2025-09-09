# ml/audio_classifier.py
import os

# Mapping from filenames to sound classes
AUDIO_LABELS = {
    'beebuzz.wav': 'bee_sound',
    'beebuzz1.wav': 'bee_sound',
    'beeland.wav': 'bee_sound',
    'hbflap.wav': 'hummingbird_sound',
    'hbflap1.wav': 'hummingbird_sound',
    'none.wav': 'no_sound'
}

def classify_audio(audio_path):
    filename = os.path.basename(audio_path)
    return AUDIO_LABELS.get(filename, 'no_sound')  # Default to 'no_sound'

