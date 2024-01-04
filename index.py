import sys
import base64
import time
sys.path.insert(0, './src')

import inference
import generate


#en_speaker_3 is a nice brittish voice, set as default
voice = "v2/en_speaker_3"

generate.speech("Kobold is pretty neat huh!", voice=voice)

