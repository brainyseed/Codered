//This program involves creating a fill in the blank word game. Try prompting the user to enter a noun, verb, and an adjective. 
//Use the provided responses to fill in the blanks and then display the story. 
//First, write a short story. Remove a noun, verb, and an adjective.
//Create a function that asks for input from the user.
//Create another function that will fill the blanks in the story you’ve just created. Ensure that each function contains a docstring.
//After the noun, verb, and adjective have been collected from the user, display the story that has been created using their input
def get_word(word_class):
 """Get a word from standard input and return that word."""
 if word_class.lower() == 'adjective':
 article = 'an'
 else:
 article = 'a'
 return input('Enter a word that is {0} {1}: '.format(article, word_class))
def fill_in_the_blanks(noun, verb, adjective):
 """Fills in the blanks and returns a completed story."""
 story = "I never knew anyone that hadn't {1} at least once in their life,
except for {2}, old Aunt Polly. She never {1}, not even when that {0} came to
town.".format(noun, verb, adjective)
 return story
