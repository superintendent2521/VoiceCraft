
from transformers import pipeline, set_seed, BarkModel, AutoProcessor
import random
import torch
from scipy.io.wavfile import write


model = BarkModel.from_pretrained("suno/bark", torch_dtype=torch.float16)
processor = AutoProcessor.from_pretrained("suno/bark")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
#currently no batching because im slow
#will invest later
#it is suppost to be a batching engine after all, gotta get the rest of the code to not die when i do batching
#and i dont know if it makes it use double the vram even if its the same model
#though batching might only work with the same model, its pretty fast (ish) to hotswap them


def generate_speech(model, text, voice, nb_loops = 5):
    inputs = processor(text, voice_preset=voice).to(device)
    seed = random.randint(0, 10000)
    set_seed(seed)
    output = model.generate(**inputs, do_sample = True, fine_temperature = 0.4, coarse_temperature = 0.8)
    return output

def save_audio_to_wav(output, filename):
    sampling_rate = model.generation_config.sample_rate
    speech = output[0].cpu().numpy()
    # convert the data type to float32
    speech = speech.astype('float32')
    write(filename, sampling_rate, speech)


def text_to_speech(text, filename, voice):
    randomid = random.randint(0, 10000)
    output = generate_speech(model, text, voice)
    save_audio_to_wav(output, f"output/save+{randomid}.wav")
    filepath = f"output/save+{randomid}.wav"
    print(filepath)
    return filepath
