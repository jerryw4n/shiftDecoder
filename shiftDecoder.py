# Ask user for input of sentence to decode
encoded_sentence = input("Enter the sentence you want to decode (lowercase): ")
# Convert sentence into ASCII values as a list
converted_sentence = list(encoded_sentence.encode('ascii'))

for n in range(1, 26):
	# Print the current iteration number
	print('Shift ' + str(n) + ':')
	# Apply the shift to each character in the list
	for i in range(len(converted_sentence)):
		converted_sentence[i] += 1
		# Handle wrap-around for letters (a-z)
		if converted_sentence[i] > ord('z'):
			converted_sentence[i] -= 26
		elif converted_sentence[i] < ord('a'):
			converted_sentence[i] += 26
	# Convert the list back into a string
	decoded_sentence = [chr(num) for num in converted_sentence]
	# Print the decoded sentence
	print(''.join(decoded_sentence))
	print('')