import json

with open('nlu/etc/model/data.json') as file:
    data = json.load(file)
    
training_sentences = []
training_labels = []
labels = []
responses = []

def prep_data():
    """
    :returns: training_sentences, training_labels, responses(list), labels, num_classes
    """
    for intent in data['intents']:
        for pattern in intent['patterns']:
            training_sentences.append(pattern)
            training_labels.append(intent['tag'])
        responses.append(intent['responses'])
        
        if intent['tag'] not in labels:
            labels.append(intent['tag'])

    num_classes = len(labels)

    return training_sentences, training_labels, responses, labels, num_classes
            

#training_sentences, training_labels, responses, labels, num_classes = prep_data()

def add_reddit_data(corpus):
    pass

"""
print(training_sentences[0])
print(training_labels[0])
print(responses[0][0])
print(labels[0])
print(num_classes)
"""
