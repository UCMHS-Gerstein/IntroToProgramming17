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
---
### Committing

Commit the current state of your repository with a commit message of "created pumpkin and readme"
+++
### Expected Results

A new commit should be created

```shell
[master (root-commit) abbf72c] created pumpkin and readme
 2 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 pumpkin.py
 create mode 100644 readme.md
 ```
+++
### Actual Results

You get an error

```shell
*** Please tell me who you are.
Run
  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"
to set your account's default identity.
Omit --global to set the identity only in this repository.
fatal: empty ident name (for <jgerstein@24dcaea7d349>) not allowed
```
+++
### Use Git Config

```shell
git config user.email jgerstein@ucvts.org
git config user.name jgerstein
```
Now try the commit again
---
### Commands

```shell
git commit -m "created pumpkin and readme"
```
---
### Check Status Again

Let's see what's going on now
+++
### Expected Results

```shell
On branch master
nothing to commit, working tree clean
PS C:\Users\gerst\Documents\github\first-repo>
```
---
### Modify Your Files

Change the contents of both files (don't forget to save!). Check your status again
+++
### Expected results

```shell
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   pumpkin.py
        modified:   readme.md

no changes added to commit (use "git add" and/or "git commit -a")
```
---
### Staging and Committing

Make a new commit with the commit message "Updated files". Can you stage and commit in one step?
+++
### Commands

```shell
git commit -am "Updated files"
```