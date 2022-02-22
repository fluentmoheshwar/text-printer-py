import os
loop = 0
text = input("What text do you wanna print?\n")
times = int(input("How many times\n"))

for loop in range(0, times):
    print(text)
print("Press any key to exit...")
os.system('pause > nul')