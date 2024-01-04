import json
import inference

#Used for stats to count total letters generated
def counter(text):
    count = len(text)
    data = {'letter_count': count}

    with open('letter_count.json', 'w') as json_file:
        json.dump(data, json_file)

    return data
#actually generates the stuff,
def speech(text):
    counter(text)
