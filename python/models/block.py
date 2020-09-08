import json


class Block:

	def __init__(self, content):
		self.content = json.loads(content)

	def search_in_content(self, words):
		# check all words need to be in dictionary value,
		# flatten json which makes searching more easy
		words = words.split(" ")
		for c in self.content:
			flatten_c = self.__flatten_json(c)
			for key, value in flatten_c.items():
				count_words = 0
				for word in words:
					# "The 'type' field should be excluded from searches"
					if word.lower() in str(value).lower() and "type" not in key:
						count_words = count_words + 1
					if count_words == len(words):
						return True

		return False

	def __flatten_json(self, json_content):
		"""
			Flatten json object with nested keys into a single level.
			Args:
				nested_json: A nested json object.
			Returns:
				The flattened json object if successful, None otherwise.
		"""
		out = {}

		def flatten(x, name=''):
			if type(x) is dict:
				for a in x:
					flatten(x[a], name + a + '_')
			elif type(x) is list:
				i = 0
				for a in x:
					flatten(a, name + str(i) + '_')
					i += 1
			else:
				out[name[:-1]] = x

		flatten(json_content)
		return out
