"""
Write a function that takes a string input and reverses the order of words.

input: "Let's start this amazing journey"
output: "journey amazing this start Let's"
"""

def reverse_word_order(sentence):
    words = sentence.split(" ")
    return ' '.join(words[::-1])

print(reverse_word_order("Let's start this amazing journey"))