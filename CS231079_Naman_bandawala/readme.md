[README1.md](https://github.com/user-attachments/files/25562524/README1.md)
# 📚 Assignment 1 – Parallel Tokenization (Compiler Design)

**Subject:** Compiler Design (CS-603 / AD604)
**College:** Truba Institute of Engineering & Information Technology, Bhopal
**Marks:** 2
**Due Date:** 26 February 2026, 3:00 PM (IST) ⚠️ No late submissions accepted

---

## 🤔 What is this assignment about?

You need to **research and implement a parallel (multi-threaded) lexer** — a program that reads source code and breaks it into tokens (like keywords, numbers, symbols) — but does it **really fast** by using **multiple CPU cores at the same time**.

Think of it like this:
> Instead of one person reading a 1000-page book word by word, you give different chapters to 10 people to read simultaneously. Much faster!

---

## 🧩 Key Concepts (Explained Simply)

### What is Lexical Analysis?
It's the **first step of a compiler**. It reads raw source code (text) and converts it into a list of meaningful chunks called **tokens**.

For example, the code `int x = 5;` becomes:
```
[KEYWORD: int] [IDENTIFIER: x] [OPERATOR: =] [NUMBER: 5] [SEMICOLON: ;]
```

### What is a Sequential Lexer?
A normal (standard) lexer reads the file **one character at a time, from start to finish**. It's simple but slow for huge files.

### What is a Parallel / Concurrent Lexer?
A parallel lexer **splits the file into chunks** and gives each chunk to a separate thread (worker). All threads tokenize their chunk at the same time → much faster!

### What is the Problem with Splitting?
Imagine splitting a file right in the middle of a multi-line comment like this:

```
/* This is a very
   long comment */
```

If you cut the file right at "very", one thread gets `/* This is a very` and the other gets `long comment */`. Neither knows it's part of the same comment! 😬

**Your job is to figure out how to handle this correctly.**

---

## ✅ What You Need to Do

1. **Research** how parallel tokenization works on multi-core CPUs.
2. **Implement** a Concurrent Lexical Analyzer using one of these languages:
   - C
   - C++
   - Go
   - Rust
3. **Use threads** to tokenize large files (1GB+) in parallel.
4. Make sure it is **thread-safe** (no data corruption when threads run together).
5. **Benchmark** your implementation against the standard `Flex` tool and show the performance comparison.

---

## 🧠 Core Challenges to Solve

| Challenge | What it means |
|---|---|
| File splitting | How to divide the file without cutting a token in half |
| Token boundary detection | Detecting where it's "safe" to start a new chunk |
| Thread safety | Ensuring threads don't overwrite each other's data |
| Result merging | Combining token lists from all threads in the correct order |

---

## 🛠️ Suggested Approach (High Level)

1. **Memory-map** the large file so all threads can access it efficiently.
2. **Scan for safe split points** — positions where no multi-char token (string, comment) is "open".
3. **Assign each chunk to a thread.**
4. **Each thread tokenizes its chunk** independently.
5. **Merge all results** in order at the end.
6. **Measure time** and compare with Flex.

---

## 📏 Benchmarking

You need to compare:
- ⏱️ Your parallel lexer (with 2, 4, 8 threads) — time taken
- ⏱️ Flex (standard sequential lexer) — time taken

Use a **1GB+ source file** as your test input. Show speedup clearly.

---

## ⚠️ Important Rules

- ❌ No plagiarism
- ❌ No use of AI tools (ChatGPT, Copilot, etc.)
- ✅ Work must be original and done by you
- ✅ Cite all references and sources used
- 📅 Submit before **26 Feb 2026, 3:00 PM** — no exceptions

---

## 📖 Suggested References to Cite

- Dragon Book: *Compilers: Principles, Techniques & Tools* – Aho, Lam, Sethi, Ullman
- Flex documentation: https://github.com/westes/flex
- POSIX Threads (pthreads) manual
- Go `sync` package documentation (if using Go)
- Any research papers on parallel lexical analysis

---

> **Bottom line:** Build a lexer that uses multiple threads to tokenize huge codebases faster than Flex, while correctly handling tokens that span chunk boundaries.
