
from transformers import pipeline, set_seed, BarkModel, AutoProcessor
import random
import torch
from scipy.io.wavfile import write


model = BarkModel.from_pretrained("suno/bark")
processor = AutoProcessor.from_pretrained("suno/bark")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

def generate_speech(model, text, voice, nb_loops = 5):
    inputs = processor(text, voice_preset=voice).to(device)
    seed = random.randint(0, 10000)
    set_seed(seed)
    output = model.generate(**inputs, do_sample = True, fine_temperature = 0.4, coarse_temperature = 0.8)
    return output

def save_audio_to_wav(output, filename):
    sampling_rate = model.generation_config.sample_rate
    speech = output[0].cpu().numpy()
    write(filename, sampling_rate, speech)


def text_to_speech(text, filename, voice):
    output = generate_speech(model, text, voice)
    save_audio_to_wav(output, f"output/{filename}")

