'''
what if my list contains duplicates words? assume all unique words
input: list of strings
output: set of tuple

retrospective:
feedback it was good to understand the problem, but with such limited time it's better to code as you go, but you can work through it as, spend less time on pseudo code 

i was proud when i figured out the the value can be a list, and i can later conver it to a tuple and add it to the set 
'''
def grouped(s):
    # initialize set
    ag_set = set()
    ag_hash = {}

    # loop through list of words
    for word in s:
        # add list comprehension
        sorted_word = word.split("").sort() # refactor to use list comprehension 
    # create dictionary where the key is the letters sorted, and the value is a list 
    # if the key exists, i want to append the word to the list

    # loop through the dictionary values
    # convert list to a tuple
    # add tuple to set
    # return set
    pass




lst = ["eat", "tea", "tan", "ate", "nat", "bat"]
answer_1 = set([("ate", "eat", "tea"), ("bat",), ("nat", "tan")])
assert grouped(lst) == answer_1

lst = ["bored", "players", "sadder", "dreads", "robed", "parsley"]
answer_2 = set([("bored", "robed"), ("parsley", "players"),
                ("dreads", "sadder")])
assert grouped(lst) == answer_2

lst = ["eat", "tae", "tea", "eta", "aet", "ate"]
answer_3 = set([("aet", "ate", "eat", "eta", "tae", "tea")])
assert grouped(lst) == answer_3

lst = ["eat", "ear", "tar", "pop", "pan", "pap"]
answer_4 = set([("eat",), ("ear",), ("tar",), ("pop",), ("pan",),
                ("pap",)])
assert grouped(lst) == answer_4

lst = []
answer_5 = set()
assert grouped(lst) == answer_5

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
