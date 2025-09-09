def check_and_trigger(video_class, audio_class, humidity):
    # Trigger aroma dispenser only if no pollinator detected in video AND no sound detected AND humidity is low
    if video_class == 'none' and audio_class == 'no_sound' and humidity < 40:
        return 'Activate Aroma Dispenser'
    return 'No Action'
