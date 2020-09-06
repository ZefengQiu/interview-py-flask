class Message:

	def __init__(self, msg_str):
		self.string = msg_str

	def process_with_state(self, states_dict):
		# Algorithm to process message string for "{|}" information in it
		# Run time is O(n), which n is the length of string

		start = 0
		mid = 0
		end = 0
		state_id = ""
		default_str = ""
		output_str = self.string

		for index in range(len(self.string)):
			c = self.string[index]
			if c == '{':
				start = index

			if c == '|':
				mid = index
				state_id = self.string[start + 1:mid]

			if c == '}':
				end = index
				to_replace = self.string[start: end + 1]

				if self.string[mid + 1] != self.string[end]:
					# there is a default string in { | }
					default_str = self.string[mid + 1:end]
					output_str = self.__replace_string(output_str, state_id, to_replace, states_dict, default_str)
				else:
					# no default string
					output_str = self.__replace_string(output_str, state_id, to_replace, states_dict, "")

				default_str = ""

		self.string = output_str

	def __replace_string(self, string,  state_id, to_replace, states_dict, default_str):
		if state_id in states_dict.keys():
			return string.replace(to_replace, states_dict[state_id], 1)
		else:
			return string.replace(to_replace, default_str, 1)

