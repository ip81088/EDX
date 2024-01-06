# Import emoji library
import emoji

# Get user input
answer = input("Input")

output = emoji.emojize(answer, language='alias')

print("Output", output)

