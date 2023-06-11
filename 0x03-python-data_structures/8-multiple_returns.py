#!/usr/bin/python3
def multiple_returns(sentence):
    counter = 0
    for i in sentence:
        counter += 1
        if sentence == "":
            sentence = None
        else:
            sentence = sentence[0] 
       
    return (counter, sentence)
