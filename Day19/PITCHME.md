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
If you've done this step correctly, your command line should indicate that you're in the `first-repo` directory
+++
```shell
mkdir first-repo
cd first-repo
```
---
### Create a repository

Time to turn your current working directory into a *git repository*. What's the command for that?
+++
If you've done this step correctly, git has created a hidden folder called `.git` inside your working directory, which is how a folder is turned into a git repository
+++
```shell
git init
```
---
### Check Status

Let's make sure everything's working. How do we check the current state of our repository?
+++
Your output should look something like:

```shell
On branch master

Initial commit

nothing to commit (create/copy files and use "git add" to track)
PS C:\Users\gerst\Documents\github\first-repo>
```
+++
```shell
git status
```