#!/usr/bin/python
class Suggester:
	word_map = {}

	def __init__(self, file_path):
		self.word_map = {}

		with open(file_path, "r") as file:
			for word in file:
				word = word.strip()
				current_map = self.word_map
				for character in word:
					if character not in current_map.keys():
						current_map[character] = {}
					current_map = current_map[character]
				current_map["is_word"] = True
		print("Completed loading words.")

	def get_sub_map(self, prefix):
		sub_map = self.word_map
		for character in prefix:
			character = character.lower()
			if character in sub_map.keys():
				sub_map = sub_map[character]
			else:
				sub_map = None
				break
		return sub_map

	def get_suggestions_from_sub_map(self, prefix, suffix_map, suggestions):
		if "is_word" in suffix_map.keys():
			suggestions.append(prefix)

		keys = {key for key in suffix_map.keys() if len(key) is 1}
		for key in keys:
			self.get_suggestions_from_sub_map(prefix + key, suffix_map[key], suggestions)

		return suggestions

	def get_suggestions(self, prefix):
		sub_map = self.get_sub_map(prefix)
		if sub_map is not None:
			suggestions = self.get_suggestions_from_sub_map(prefix, sub_map, [])
			return suggestions
		else:
			return []