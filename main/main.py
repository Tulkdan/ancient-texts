fooLetters = ["r", "t", "c", "d", "b"]
alphabet = ["t", "w", "h", "z", "k", "d", "f", "v", "c", "j", "x", "l", "r", "n", "q", "m", "g", "p", "s", "b"]

vocabulary = []



def order(vocabulary):
    ordenado = []
    for letter in alphabet:
        arr = []
        for word in vocabulary:
            if(word[0] == letter):
                arr.append(word)

        if(len(arr) != 0): ordenado.append(orderResto(arr));

    return ordenado

def orderResto(arr):
    arrOrder = []
    for word in arr: # will check the array with all the first letter equal
        if (len(arrOrder) == 0):
            arrOrder.append(word)
        else:
            for index, palavra in enumerate(arrOrder):
                aux = 1
                if(word in arrOrder): break

                if (word[aux] == palavra[aux]):
                    if (aux + 1 < len(palavra)):
                        if(something(palavra, word, aux + 1, index) == 1): arrOrder.insert(index, word)
                    else:
                        arrOrder.insert(index, word)
                        break
                elif (alphabet.index(word[aux]) < alphabet.index(palavra[aux])):
                    arrOrder.insert(index, word)
                    break

            if(word not in arrOrder): arrOrder.append(word)


    return arrOrder


def something(palavra, word, aux, index):
    if(word[aux] == palavra[aux]):
        if(aux+1 < len(palavra)):
            something(palavra, word, aux+1, index)
            return
        else:
            return 1
    if (alphabet.index(word[aux]) < alphabet.index(palavra[aux])):
        return 1

    return 0



text = input().split()

prepositions = 0; verbSubjunctive = 0; verbs = 0; numbers = []; prettyNumbers = []

for words in text:
    if(len(words) == 5):
        if("l" not in words and words[-1] not in fooLetters):
            prepositions += 1

    elif(len(words) > 7 and words[-1] not in fooLetters): # check if the last letter is a bar letter and the word is >= 7
        verbs += 1
        if(words[0] not in fooLetters):
            verbSubjunctive += 1

    if(words not in vocabulary):
        vocabulary.append(words)

    value = 0
    for index, letter in enumerate(words):
        value += alphabet.index(letter) * (20 ** index)

    if (value > 422224 and (value % 3) == 0 and value not in prettyNumbers):
        prettyNumbers.append(value)



vocabulary.sort()
ordered = order(vocabulary)


print("There are " + str(prepositions) + " prepositions in Text B")
print("There are " + str(verbs) + " verbs in Text B")
print("There are " + str(verbSubjunctive) + " subjunctive verbs in Text B")
print("In Text B, there are " + len(prettyNumbers) + " distinct(!) pretty numbers")

