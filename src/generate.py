
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
def speech(text, cuda):
    #counter(text)
    #unused rn
    tts = inference.TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=cuda)    
    # generate speech by cloning a voice using default settings
    inference.generate_speech(text, cuda) 
    # convert numpy array to bytes
    wav_bytes = io.BytesIO()
    wavfile.write(wav_bytes, tts.sample_rate, wav_data)

    return wav_bytes.getvalue()
