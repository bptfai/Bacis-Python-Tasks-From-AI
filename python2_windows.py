# TASK2: Find the percentages of characters used in the text

# ==============================================================================================

# error messages
error_message_1 = "Your text can not be empty ..."

# system messages
system_message_1 = ">>> Please enter your text (q:exit, t:test) : "
system_message_2 = "Goodbye !"

# test text
test_text = "There are no facts, only interpretations."

# ==============================================================================================

# program loop
running = True
while running:
	text = input('\n' + system_message_1)

	# check if text is empty
	if text == "":
		print('\n' + error_message_1)

	else:
		# setting up the exit
		if text == 'q' or text == 'Q':
			print('\n' + system_message_2 + '\n')
			running = False

		else: 
			if text == "t":
				text = test_text

			# find used characters
			used_characters = []

			for character in text:
				if character in used_characters:
					pass
				else:
					used_characters.append(character)

			# count used characters
			percentages = []
			
			for used_character in used_characters:
				number_of_use = text.count(used_character)
				percentage_of_use = number_of_use * (100 / len(text))  
				percentages.append(percentage_of_use)

			# getting results
			print('\n' + "Your Text: " + text)
			print('-' * 75)
			for used_character in used_characters:
				percentage_index = used_characters.index(used_character)
				print(""""{}" --> %{}""".format(used_character, percentages[percentage_index]))
