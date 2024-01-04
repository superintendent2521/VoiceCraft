
import json
import inference
import random
import io
from scipy.io import wavfile

#Used for stats to count total letters generated
def counter(text):
    count = len(text)
    try:
        with open('letter_count.json', 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = {'letter_count': 0}

    data['letter_count'] += count

    with open('letter_count.json', 'w') as json_file:
        json.dump(data, json_file)

    return data
#actually generates the stuff,
def speech(text, voice="v2/en_speaker_3"):
    counter(text)
    # Call text_to_speech and return its result
    return inference.text_to_speech(text, "output.wav", voice=voice)

