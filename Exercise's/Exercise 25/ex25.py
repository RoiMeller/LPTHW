# LPTHW Exercise 25 - Function practice

# ' """ ' those are special strings called: documentation comments. (in python2 write 'help(ex25))

def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts the words."""
	return sorted(words)

def print_first_word(words):
	"""Print the first word after popping it off."""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Print the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words the prints the first last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)

# ==============================================================
# how to:
# run python2
# >>>import ex25

# or use this shortcut to do your import: "from ex25 import *" 
# which is like saying, "Import everything from ex25." 

# >>>sentence = "All good things come to those who wait."
# >>>words = ex25.break_words(sentence)
# >>>words
# >>>sorted_words = ex25.sort_words(words)
# >>>sorted_words
# >>>ex25.print_first_word(words)
# >>>ex25.print_last_word(words)
# >>>words
# >>>ex25.print_first_word(sorted_words)
# >>>ex25.print_last_word(sorted_words)
# >>>sorted_words
# >>>sorted_words = ex25.sort_sentence(sentence)
# >>>sorted_words
# >>>ex25.print_first_and_last(sentence)
# >>>ex25.print_first_and_last_sorted(sentence)
# ==============================================================
