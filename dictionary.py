import json
from difflib import get_close_matches
dataset=json.load(open("original.json"))
key=dataset.keys()
def translate(word):
    word=word.lower()
    if word in dataset:
        return dataset[word]
    elif word.title() in dataset:
        return dataset[word.title()]
    elif word.upper() in dataset:
        return dataset[word.upper()]
    elif len(get_close_matches(word,dataset.keys()[0])):
        print("Did you mean [%s] in lieu of [%s]",get_close_matches(word,dataset.keys()[0]),word)
        decision=input('Press Y if yes or else press N')
        if(decision==Y):
            return get_close_matches(word,dataset.keys()[0])
        else:
            print("The word is not found")

    else:
        print("Word not found !try again")



word=input('Enter the word to know:')
output=translate(word)
if type(output)== list:
    for i in output:
        print(output)
else:
    print(output)
