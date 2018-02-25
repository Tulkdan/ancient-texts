fooLetters = ["r", "t", "c", "d", "b"]
alphabet = ["t", "w", "h", "z", "k", "d", "f", "v", "c", "j", "x", "l", "r", "n", "q", "m", "g", "p", "s", "b"]

vocabulary = []


prepositions = 0; verbSubjunctive = 0; verbs = 0

def order(vocabulary):
    ordenado = []
    for letter in alphabet:
        print(letter)
        arr = []
        for word in vocabulary:
            if(word[0] == letter):
                arr.append(word)

        print(arr)
        if(len(arr) != 0): ordenado.append(orderResto(arr)); print(ordenado)

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

                print(word, word[aux], palavra, palavra[aux])

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

for words in text:
    if(len(words) == 5):
        if("l" not in words and words[-1] not in fooLetters):
            prepositions += 1

    elif(len(words) >= 7 and words[-1] not in fooLetters): # check if the last letter is a bar letter and the word is >= 7
        if(words[0] in fooLetters): # if the first letter isn't a bar letter
            verbs += 1
        else:
            verbSubjunctive += 1

    if(words not in vocabulary):
        vocabulary.append(words)


vocabulary.sort()
order(vocabulary)


print("There are " + str(prepositions) + " prepositions in Text B")
print("There are " + str(verbs) + " verbs in Text B")
print("There are " + str(verbSubjunctive) + " subjunctive verbs in Text B")

# print(order(vocabulary, alphabet))
# print(vocabulary)

