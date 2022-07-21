str = 'mississippi'                             #input string
def make_dict(x):                               # defining dictionary
    dict= {}
    for letter in x:
        dict[letter] = 1 + dict.get(letter, 0)  #increment if the letter repeats
    return dict
def most_frequent(str):                         #using most_frequent function 
    letters = [letter.lower() for letter in str]
    dict = make_dict(letters)
    result = []
    for y in dict:
        result.append((dict[y], y))             #appending to the final result
    result.sort(reverse=True)                   #sorting and reversing it to descending order
    for count, letter in result:                #printing final count and repeating letters
        print (letter,'=', count)
most_frequent(str)                              
