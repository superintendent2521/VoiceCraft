import sys
import base64
import time
from flask import Flask, request, send_file

sys.path.insert(0, './src')

import inference
import generate


#en_speaker_3 is a nice brittish voice, set as default, can find the voice list here
#https://suno-ai.notion.site/8b8e8749ed514b0cbf3f699013548683?v=bc67cff786b04b50b3ceb756fd05f68c

app = Flask(__name__)

@app.route('/speech', methods=['POST'])
def speech():
    data = request.get_json()
    text = data['text']
    voice = data.get('voice', "v2/en_speaker_3")  # Use default voice if not provided
    filepath = generate.speech(text, voice)
    return send_file(filepath, mimetype='audio/wav')  # Send the generated audio file

if __name__ == '__main__':
    app.run(debug=True)
