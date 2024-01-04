import sys
import base64
import time
import inference
import generate
from flask import Flask, jsonify, request

sys.path.insert(0, './src')

app = Flask(__name__)

#Generate speech route
@app.route('/generate_speech', methods=['POST'])
def generate_speech():
    #Messure time
    start_time = time.time()
    text = request.json.get('text')
    speeches = []
    for i in range(2):
        speech = generate.speech(text, cuda=False)
        # convert bytes to base64 string
        speech_base64 = base64.b64encode(speech).decode('utf-8')
        speeches.append(speech_base64)
    end_time = time.time()
    #Messure time aswell
    execution_time = end_time - start_time
    print(f"The code executed in {execution_time} seconds")
    return jsonify(speeches=speeches), 200

if __name__ == "__main__":
    app.run(debug=True)
