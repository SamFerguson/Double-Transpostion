from math import ceil, factorial
from itertools import permutations
from copy import deepcopy
num_columns = 5
#word = "HTHESTHHRASWRASCSCRSSCWWWESWWEIITAIIT"
word = "Tn'tnhteotrdn a kr iur  evoero yact lseen n, ncciaraaeefmo urZcpre 0s e7 sh sh.ahpweernoee mhhy ttleftg"
#word = word.replace(" ", "")
word_length = len(word)
extra_letters = word_length % num_columns
transposition_array = []
#to print encoded
def print_column_major(array):
    for i in range(len(array[0])):
        for j in range(len(array)):
            print(array[j][i], end = "")
        print("", end= " ")

    print()

#to print decoded
def print_in_order(array):
    to_return = ""
    for i in range(len(array)):
        for j in range(len(array[i])):
            to_return += array[i][j]
    return to_return

transposition_array = [["" for i in range(num_columns)] for j in range(ceil(word_length/num_columns))]
#for each column
index= 0


fake_ta = [["hi" for i in range(num_columns)] for j in range(len(transposition_array))]
print(fake_ta)
#generate all transpositions
for permutation in permutations(list(range(0, num_columns))):
    #fill the 2d array with cipher
    transposition_array = [["" for i in range(num_columns)] for j in range(ceil(word_length/num_columns))]
    for i in range(len(permutation)):
        extra_letter_indices = permutation[:extra_letters]
        added = 1 if (i in extra_letter_indices) else 0
        for j in range(len(transposition_array) -1 + added):
            if(index < len(word)):
                transposition_array[j][i] = word[index]
                index += 1

    index = 0
    fake_ta = [["hi" for i in range(num_columns)] for j in range(len(transposition_array))]

    #transpose the columns
    for number in permutation:
        for i in range(len(fake_ta)):
            fake_ta[i][index] = transposition_array[i][number]
        index += 1
    index = 0

    #get the decoded cipher
    one_transposed_string = print_in_order(fake_ta)
    #print(one_transposed_string, permutation)
    transposition_array = [["" for i in range(num_columns)] for j in range(ceil(word_length/num_columns))]
    #fill 2d array with decoded cipher
    for i in range(len(permutation)):
        extra_letter_indices = permutation[:extra_letters]
        added = 1 if (i in extra_letter_indices) else 0
        for j in range(len(transposition_array) -1 + added):
            if(index < len(word)):
                transposition_array[j][i] = one_transposed_string[index]
                index += 1
    index = 0

    for permutationB in permutations(list(range(0, num_columns))):
        #tranpose the columns
        fake_ta = [["hi" for i in range(num_columns)] for j in range(len(transposition_array))]
        for number in permutationB:
            for i in range(len(fake_ta)):
                fake_ta[i][index] = transposition_array[i][number]
            index += 1
        index = 0
        print(print_in_order(fake_ta),permutation, permutationB)




















