import sys
sys.path.insert(0, './src')
from flask import Flask, jsonify, request
import time
import inference
import generate

app = Flask(__name__)
#Generate speech route
@app.route('/generate_speech', methods=['POST'])
def generate_speech():
    #Messure time
    start_time = time.time()
    text = request.json.get('text')
    speeches = []
    for i in range(10):
        speech = generate.speech(text, cuda=False)
        end_time = timeit.default_timer()
        #Messure time aswell
        execution_time = end_time - start_time
        print(f"The code executed in {execution_time} seconds")
        speeches.append(speech)
    return jsonify(speeches), 200

if __name__ == "__main__":
    app.run(debug=True)
