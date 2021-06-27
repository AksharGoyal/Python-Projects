# Madlibs Game

# The user inputs random words to create a story with their own words in them
# The user will not know for what meaning they have provided their choice of word
# And that makes this game more fun to try!

adjective_1 = input("Enter an adjective: ")
adjective_2 = input("Enter another adjective: ")
adjective_3 = input("Enter the last adjective: ")
noun_1 = input("Enter a name: ")
noun_2 = input("Enter a place's name: ")
verb_1 = input("Enter a verb: ")
adverb_1 = input("Enter an adverb: ")
adverb_2 = input("Enter another adverb: ")
noun_3 = input("Lastly, enter your favourite thing to eat: ")

# We have got the lit of inputs. Now it's story time.
sentence_1 = f"There was a programmer named {noun_1} who was very {adjective_1} but didn't know what to do in their life."
sentence_2 = f"One day, they found a(n) {adjective_2} cave while exploring {noun_2}."
sentence_3 = f"{noun_1} went inside the cave {adverb_1} and found a(n) {adjective_3} gold cup."
sentence_4 = f"They {verb_1} the cup {adverb_2} and went home to eat their favourite {noun_3}."
sentence_5 = "#####"+('-'*35)+"THE END"+('-'*35)+"#####"

# Story has been setup. Let's read it together :)
print("1.", sentence_1)
print("2.", sentence_2)
print("3.", sentence_3)
print("4.", sentence_4)
print(sentence_5)
