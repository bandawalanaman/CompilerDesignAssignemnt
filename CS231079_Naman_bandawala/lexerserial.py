try:
    file = open("input.c", "r")
except FileNotFoundError:
    print("Sorry! File not found")
    exit()

while True:
    character = file.read(1)
    
    if not character:
        break
    
    if character.isalpha():
        print(f"LETTER: {character}")
    elif character.isdigit():
        print(f"NUMBER: {character}")
    else:
        print(f"SYMBOL: {character}")

file.close()
print("File reading complete!")
