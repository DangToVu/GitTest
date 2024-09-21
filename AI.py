import random

# Word lists for the haiku (syllables per line: 5-7-5)
five_syllable_words = ["autumn breeze", "silent night", "whispering trees", "golden sunset", "gentle rain"]
seven_syllable_words = ["a cool wind brushes the shore", "the moon glows soft in the sky", "leaves rustling through the dark night"]

# Function to generate a haiku
def generate_haiku():
    line1 = random.choice(five_syllable_words)
    line2 = random.choice(seven_syllable_words)
    line3 = random.choice(five_syllable_words)
    return f"{line1}\n{line2}\n{line3}"

# Generate and display the random haiku
print(generate_haiku())
