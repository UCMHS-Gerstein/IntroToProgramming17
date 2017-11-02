---
# Lists (and more Git)

Intro to Programming - Day 20
---
# Do Now

Log in to GitHub using the account you created. Go to my [repository for today's assignment](https://github.com) and fork it by clicking on the fork button. This will make a copy of the repository on your account. Open a bash console, because you're going to need it after the quiz.
---
# Authenticating to GitHub

You'll need to set up PythonAnywhere to connect to your GitHub account. We'll be using SSH keys, which are a way of logging in. Don't worry, you don't need to remember this off the top of your head. You should only have to do this once.
+++
# SSH

SSH keys are used as a type of login and password combo. They'll let you pair PythonAnywhere with your GitHub account. If you want to read more, [GitHub](https://help.github.com/articles/connecting-to-github-with-ssh/) has more info
+++
### Check for existing keys

You probably don't have any existing keys. Confirm using <kbd>ls -al ~/.ssh</kbd>