from TTS.api import TTS

def generate_speech(text, file_path="output/output.wav", speaker="Ana Florence", language="en", split_sentences=True):
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

    # generate speech by cloning a voice using default settings
    tts.tts_to_file(text=text,
                    file_path=file_path,
                    speaker=speaker,
                    language=language,
                    split_sentences=split_sentences)
