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
'''#for code in C language 
#include <stdio.h>
#include <ctype.h>

int main() {
    FILE *fp = fopen("input.c", "r");
    
    if (fp == NULL) {
        printf("File not found\n");
        return 1;
    }

    int ch;

    while ((ch = fgetc(fp)) != EOF) {
        if (isalpha(ch))
            printf("LETTER: %c\n", ch);
        else if (isdigit(ch))
            printf("NUMBER: %c\n", ch);
        else
            printf("SYMBOL: %c\n", ch);
    }

    fclose(fp);
    return 0;
}'''
