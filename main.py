# import dos commands
import os
# Creates a variable (loop)
loop = 0
# Gets the text and store it in variable (text)
text = input("What text do you wanna print?\n")
# Gets how many times and store it in variable (times)
times = int(input("How many times\n"))

# Runs the loop and print the text.
for loop in range(0,times):
    print(text)

# Print pakte and pauses the console
print("Press any key to exit...")
os.system("pause > nul")