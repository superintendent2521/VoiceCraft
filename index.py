import sys
import base64
import time
sys.path.insert(0, './src')

import inference
import generate


#en_speaker_3 is a nice brittish voice, set as default, can find the voice list here
#https://suno-ai.notion.site/8b8e8749ed514b0cbf3f699013548683?v=bc67cff786b04b50b3ceb756fd05f68c
voice = "v2/en_speaker_3"

generate.speech("Kobold is pretty neat huh!", voice=voice)

