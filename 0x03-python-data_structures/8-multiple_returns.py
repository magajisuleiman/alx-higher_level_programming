#!/usr/bin/python3
def multiple_returns(sentence):
    counter = 0
    for i in sentence:
        counter += 1
    return (counter, sentence[0])
