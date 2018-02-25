fooLetters = ["r", "t", "c", "d", "b"]
alphabet = ["t", "w", "h", "z", "k", "d", "f", "v", "c", "j", "x", "l", "r", "n", "q", "m", "g", "p", "s", "b"] # Bloogan alphabet

vocabulary = [] # List to insert all non-repeated words


def order(vocabulary): # This function serves to get all the words that start with the first letter from the alphabet
    ordenado = []
    for letter in alphabet:
        arr = []
        for word in vocabulary:
            if(word[0] == letter):
                arr.append(word) # It throws the words in this array

        if(len(arr) != 0): ordenado.append(orderResto(arr)); # Then call this other function to sort the rest of the word

    return ordenado

def orderResto(arr): # This function serves to sort the word after the second letter, 'cause the first letter is already filtered
    arrOrder = [] # This array will be returned to *order* function with the words ordered
    for word in arr:
        if (len(arrOrder) == 0): # Checks to see if arrOrder is empty
            arrOrder.append(word)
        else:
            for index, palavra in enumerate(arrOrder): # It starts checking the actual word with the words in the arrOrder
                aux = 1
                if(word in arrOrder): break # Check to see if word is already in arrOrder

                if (word[aux] == palavra[aux]): # Check if the second letter is equal
                    if (aux + 1 < len(palavra)):
                        if(something(palavra, word, aux + 1, index) == 1): arrOrder.insert(index, word) # Call this function to check recursive the others letters
                    else:
                        arrOrder.insert(index, word) # If the word is shorter and the letters is equal than the previous one, it will be inserted in that position
                        break
                elif (alphabet.index(word[aux]) < alphabet.index(palavra[aux])): # Check if the second letter in alphabet is before
                    arrOrder.insert(index, word)
                    break

            if(word not in arrOrder): arrOrder.append(word) # If none of that works, the word will be put in the end of array


    return arrOrder # Return the array sorted


def something(palavra, word, aux, index): # It recursive the rest of the word. It will return 1 if the words can be inserted, otherwise will return 0
    if(word[aux] == palavra[aux]):
        if(aux+1 < len(palavra)):
            something(palavra, word, aux+1, index)
            return
        else:
            return 1
    if (alphabet.index(word[aux]) < alphabet.index(palavra[aux])):
        return 1

    return 0



text = input().split() # Takes the entry and split in a list

# Variables used on the "main"
prepositions = 0; verbSubjunctive = 0; verbs = 0; numbers = []; prettyNumbers = []

for words in text: # Iterate through the list
    if(len(words) == 5): # Checking to see which word is a preposition
        if("l" not in words and words[-1] not in fooLetters):
            prepositions += 1

    elif(len(words) > 7 and words[-1] not in fooLetters): # Check to see which word is a verb
        verbs += 1
        if(words[0] not in fooLetters): # Check to see if the verb is in the subjunctive form
            verbSubjunctive += 1

    if(words not in vocabulary): # Remove words that are repeated in text to sort after
        vocabulary.append(words)

    value = 0
    for index, letter in enumerate(words): # Make the sum of the word
        value += alphabet.index(letter) * (20 ** index)

    if (value > 422224 and (value % 3) == 0 and value not in prettyNumbers): # Check to see if the value of the word is a pretty number
        prettyNumbers.append(value)



vocabulary.sort() # It sorts the non-repeated word's list
ordered = order(vocabulary) # Then call the function to sort the words in Bloogan alphabet


print("There are " + str(prepositions) + " prepositions in Text B")
print("There are " + str(verbs) + " verbs in Text B")
print("There are " + str(verbSubjunctive) + " subjunctive verbs in Text B")
print("In Text B, there are " + len(prettyNumbers) + " distinct(!) pretty numbers")

