
import json
import inference

#Used for stats to count total letters generated
def counter(text):
    count = len(text)
    try:
        with open('letter_count.json', 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = {'letter_count': 0}

    data['letter_count'] += count

    with open('letter_count.json', 'w') as json_file:
        json.dump(data, json_file)

    return data
#actually generates the stuff,
def speech(text):
    counter(text)
    inference.generate_speech(text)
