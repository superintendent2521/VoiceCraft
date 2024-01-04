from TTS.api import TTS
import random
import io

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

def generate_speech(tts, text, speaker="Ana Florence", language="en", split_sentences=True):
    # generate speech by cloning a voice using default settings
    wav_data = tts.tts(text=text,
                       speaker=speaker,
                       language=language,
                       split_sentences=split_sentences)
    
    # convert numpy array to bytes
    wav_bytes = io.BytesIO()
    wavfile.write(wav_bytes, tts.sample_rate, wav_data)

    return wav_bytes.getvalue()
