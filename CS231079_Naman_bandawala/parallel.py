'''import threading
THREADS = 2

def lexer(data, start, end):
    for i in range(start, end):
        ch = data[i]
        if ch.isalpha():
            print("LETTER:", ch)
        elif ch.isdigit():
            print("NUMBER:", ch)
        else:
            print("SYMBOL:", ch)

def main():
    try:
        with open("input.c", "r") as f:
            data = f.read()
    except FileNotFoundError:
        print("File not found")
        return

    size = len(data)
    part = size // THREADS

    threads = []

    for i in range(THREADS):
        start = i * part
        end = size if i == THREADS - 1 else (i + 1) * part
        t = threading.Thread(target=lexer, args=(data, start, end))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
'''
'''# C code 
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <pthread.h>

#define THREADS 2

typedef struct {
    char *data;
    long start;
    long end;
} Block;

void *lexer(void *arg) {
    Block *b = (Block *)arg;

    for (long i = b->start; i < b->end; i++) {
        char ch = b->data[i];

        if (isalpha(ch))
            printf("LETTER: %c\n", ch);
        else if (isdigit(ch))
            printf("NUMBER: %c\n", ch);
        else
            printf("SYMBOL: %c\n", ch);
    }

    return NULL;
}

int main() {
    FILE *fp = fopen("input.c", "r");
    if (fp == NULL) {
        printf("File not found\n");
        return 1;
    }

    fseek(fp, 0, SEEK_END);
    long size = ftell(fp);
    rewind(fp);

    char *buffer = malloc(size);
    fread(buffer, 1, size, fp);
    fclose(fp);

    pthread_t threads[THREADS];
    Block blocks[THREADS];

    long part = size / THREADS;

    for (int i = 0; i < THREADS; i++) {
        blocks[i].data = buffer;
        blocks[i].start = i * part;
        blocks[i].end = (i == THREADS - 1) ? size : (i + 1) * part;

        pthread_create(&threads[i], NULL, lexer, &blocks[i]);
    }

    for (int i = 0; i < THREADS; i++)
        pthread_join(threads[i], NULL);

    free(buffer);
    return 0;
}'''
