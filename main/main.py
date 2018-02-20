fooLetters = ["r", "t", "c", "d", "b"]
alphabet = ["t", "w", "h", "z", "k", "d", "f", "v", "c", "j", "x", "l", "r", "n", "q", "m", "g", "p", "s", "b"]

vocabulary = []

prepositions = 0; verbSubjunctive = 0; verbs = 0

def order(vocabulary, aphabet):
    for word in vocabulary:



text = input().split()

for words in text:
    if(len(words) == 5):
        if("l" not in words and words[4] not in fooLetters):
            prepositions += 1

    elif(len(words) == 7 and words[-1] not in fooLetters): # check if the last letter is a bar letter
        verbs += 1
        if(words[0] not in fooLetters): # if the first letter is a bar letter
            verbSubjunctive += 1

    if(words not in vocabulary):
        vocabulary.append(words)


print("There are " + str(prepositions) + " prepositions in Text B")
print("There are " + str(verbs) + " verbs in Text B")
print("There are " + str(verbSubjunctive) + " subjunctive verbs in Text B")
print(vocabulary)

