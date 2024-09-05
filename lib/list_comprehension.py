# #!/usr/bin/env python3

# def return_evens(num_list):
#     return [n for n in num_list if n%2 == 0]

# def make_exclamation(sentence_list):
#     return [sentence + "!" for sentence in sentence_list]

def return_evens(evens):
    result = [even for even in evens if even%2 == 0]
    return result
# print(return_evens([0, 1, 3, 5, 7, 8, 9]))

def make_exclamation(sentencs):
    result = [i + "!" for i in sentencs]
    return result

print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))