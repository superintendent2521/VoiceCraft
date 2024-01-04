import json
import inference
def counter(text):
    count = len(text)
    data = {'letter_count': count}

    with open('letter_count.json', 'w') as json_file:
        json.dump(data, json_file)

    return data

def speech(text):
    counter(text)
