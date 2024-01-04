
from TTS.api import TTS
import random

def generate_speech(text, file_path="output/output.wav", speaker="Ana Florence", language="en", split_sentences=True):
    random_file_name = random.randint(1, 1000000)
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

    # generate speech by cloning a voice using default settings
    tts.tts_to_file(text=text,
                    file_path=f"output/{random_file_name}.wav",
                    speaker=speaker,
                    language=language,
                    split_sentences=split_sentences)
