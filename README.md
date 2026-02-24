# 📘 Compiler Design Assignment Submission - CS603/AD604
Welcome Students! 🎓  
This repository is intended for submitting your **Compiler Design** code assignments.
Please follow the instructions carefully based on your situation.

---------------
# 🧑‍🎓 FOR STUDENTS WITHOUT GITHUB ACCOUNT
## Step 1: Create GitHub Account

1. Go to https://github.com  
2. Click **Sign Up**  
3. Enter your details  
4. Verify your email  

---------------

## Step 2: Install Git

Download from: https://git-scm.com/downloads  

After installation, check:

```bash
git --version

## 📥 How to Submit Your Assignment

Follow the steps below carefully to submit your assignment to this repository.

### 1. **Fork the Repository**
Click the **Fork** button on the top right of this repository page.

---------

### 2. **Clone Your Forked Repository**

```bash
git clone https://github.com/<your-github-username>/CompilerDesignAssignemnt.git

--------

### 3. **Then go inside the folder**
```bash
cd CompilerDesignAssignemnt

--------

### 4. **Create Your Assignment Folder**
Create a new folder inside the repo with this format:
<RollNumber>_<Name>
```bash
 mkdir CS231101_RahulSharma

--------

### 5. **Add your source code files into your folder**
Examples:
lexer.c
parser.c
symbol_table.c

--------

### 5. **Commit Your Changes**
```bash
git add .
git commit -m "Assignment Submission by <Your Name> — <Roll Number>"

### 6. **Push to Your Fork**
```bash
git push origin main

### 7. **Create a Pull Request (PR)**

Go to your fork on GitHub →
Click Compare & Pull Request →
Add a short description →
Click Create Pull Request

-----------------------

📁 **Submission Guidelines**

✔ Folder Naming:
<RollNumber>_<Name>

✔ File Naming:
Assignment1_<RollNumber>.<extension>

✔ Commit messages should clearly state your name and assignment.

**📌 Notes**
- Do not modify other students’ submissions.
- Ensure your code compiles and runs before submitting.
- Do NOT rename main repository folders
- Always write proper commit messages
- Check all files are included before creating the PR.
- Submit before deadline

**❗ Common Errors & Fixes**
Authentication Failed
solution - Use Personal Access Token instead of password.

**Rejected (non-fast-forward)**
solution Run:
git pull origin main
Then push again.

❓ Help
- If you face any issues with Git or submission, please reach out to your instructor.

Good luck and happy coding! 🚀
