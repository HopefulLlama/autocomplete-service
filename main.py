#!/usr/bin/python 
import sys
import yaml

import logging

def load_words(file_path):
	logging.print_banner("Loading words into memory...")
	
	list_of_words = {}
	with open(file_path, "r") as file:
		for word in file:
			word = word.strip()
			current_map = list_of_words
			for character in word:
				if character not in current_map.keys():
					current_map[character] = {}
				current_map = current_map[character]
			current_map["is_word"] = True
	print("Completed loading words.")
	return list_of_words

def get_sub_map(word_map, prefix):
	sub_map = word_map
	for character in prefix:
		if character in sub_map.keys():
			sub_map = sub_map[character]
		else:
			sub_map = None
			break
	return sub_map

def get_suggestions(prefix, suffix_map, suggestions):
	if "is_word" in suffix_map.keys():
		suggestions.append(prefix)

	keys = {key for key in suffix_map.keys() if len(key) is 1}
	for key in keys:
		get_suggestions(prefix + key, suffix_map[key], suggestions)

	return suggestions


def main(): 
	if len(sys.argv) == 2:
		words = load_words("words.txt")
		prefix = sys.argv[1]

		sub_map = get_sub_map(words, prefix)
		if sub_map is not None:
			logging.print_banner("Loading suggestions for '" + prefix + "'")
			suggestions = get_suggestions(prefix, sub_map, [])
			print(suggestions)
		else: 
			logging.print_banner("No suggestions found.")			
	else: 
		logging.print_banner("Require a word to complete.")

main()