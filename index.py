from flask import Flask, jsonify, request
import sys
sys.path.insert(0, './src')
import inference
import generate

app = Flask(__name__)

@app.route('/generate_speech', methods=['POST'])
def generate_speech():
    text = request.json.get('text')
    speeches = []
    for i in range(10):
        speech = generate.speech(text, cuda=False)
        speeches.append(speech)
    return jsonify(speeches), 200

if __name__ == "__main__":
    app.run(debug=True)
