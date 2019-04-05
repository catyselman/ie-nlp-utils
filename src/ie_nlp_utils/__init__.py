def tokenize(sentence, lower=True):
    if(lower == True):
        return sentence.lower().split()
    else:
        return sentence.split()
