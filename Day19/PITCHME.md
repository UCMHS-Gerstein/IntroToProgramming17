---
# Hands on Git

Intro to Programming Day 19
---
# Do Now:

Sign up for a GitHub account. I will collect usernames later. Make sure your username is appropriate. You may using an existing account if you have one. Open PythonAnywhere
---
# Goal

Together, we will be creating and working with a git repository.
---
### New Directory

Open a Bash terminal in Python Anywhere. Create a new directory called `first-repo` and change directories into it
+++
### Expected Results

If you've done this step correctly, your command line should indicate that you're in the `first-repo` directory

```shell
13:46 ~/first-repo $ 
```
+++
### Commands

```shell
mkdir first-repo
cd first-repo
```
---
### Create a repository

Time to turn your current working directory into a *git repository*. What's the command for that?
+++
### Expected Results

If you've done this step correctly, git has created a hidden folder called `.git` inside your working directory, which is how a folder is turned into a git repository
+++
### Commands

```shell
git init
```
---
### Check Status

Let's make sure everything's working. How do we check the current state of our repository?
+++
### Expected Results

Your output should look something like:

```shell
On branch master

Initial commit

nothing to commit (create/copy files and use "git add" to track)
PS C:\Users\gerst\Documents\github\first-repo>
```
+++
### Commands

```shell
git status
```
---
### Create New Files

Inside your first-repo directory, create two files: `pumpkin.py` and `readme.md`
+++
### Expected Results

You should have two empty files in your directory
+++
### Commands

```shell
touch pumpkin.py
touch readme.md
```

or create without command line through PythonAnywhere interface
---
### Check Status Again

You should know how to do this now
+++
### Expected Results

```shell
On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        pumpkin.py
        readme.md

nothing added to commit but untracked files present (use "git add" to track)
PS C:\Users\gerst\Documents\github\first-repo>
```

What does this tell us?
---
### Staging files

Stage both of your new files and check your repo's status
+++
### Expected Results

```shell
On branch master

Initial commit

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

        new file:   pumpkin.py
        new file:   readme.md

PS C:\Users\gerst\Documents\github\first-repo>
```
+++
### Commands
```shell
git add -A
git status
```