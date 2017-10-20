filename = 'alice.txt'

# with open(filename) as file_object:
# 	contents = file_object.read()

try:
	with open(filename) as file_object:
		contents = file_object.read()
except IOError:
	msg = "Sorry, the file " + filename + " does not exist."
	print(msg)
else:
	words = contents.split()
	num_words = len(words)
	print("The file " + filename + " has about " + str(num_words) + " words")