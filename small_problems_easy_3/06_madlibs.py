# PY101-109 Small Problems, Easy 3, Problem 6. "Madlibs":

"""Madlibs is a simple game where you create a story template with 
"blanks" for words. You, or another player, then construct a list of 
words and place them into the story, creating an often silly or funny 
story as a result.

Create a simple madlib program that prompts for a noun, a verb, an 
adverb, and an adjective, and injects them into a story that you create.

Example:
Enter a noun: dog
Enter a verb: walk
Enter an adjective: blue
Enter an adverb: quickly

Expected Output:
Do you walk your blue dog quickly? That's hilarious!
The blue dog walks quickly over the lazy dog.
The dog quickly walks up to Joe's blue turtle.
"""


noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adj = input("Enter an adjective: ")
adv = input("Enter an adverb: ")

print(f"Do you {verb} your {adj} {noun} {adv}? That's hilarious!")
print(f"The {adj} {noun} {verb}s {adv} over the lazy {noun}.")
print(f"The {noun} {adv} {verb}s up to Joe's {adj} turtle.")