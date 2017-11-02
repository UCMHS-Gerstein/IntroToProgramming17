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

You probably don't have any existing keys. Confirm by entering
```shell 
ls -al ~/.ssh
```
at the command prompt.

You should get a warning that there is no such file or directory. That's normal
```shell
ls: cannot access /home/gersteinj/.ssh: No such file or directory
```

Let me know if you get some other result
+++
### Making a new key

Use the following command in your Bash console, replacing the email address with **the one you signed up for GitHub with**.

```shell
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

When it asks you to choose a location, just press enter to accept the default location

If you want to set a passphrase on your SSH key, you can. Otherwise, just press enter when prompted. If you're using a passphrase, let me know so I can give you some additional info.
+++
### Registering your key

Now we'll set GitHub up to recognize your new SSH key

* Use `cat ~/.ssh/id_rsa.pub` to print your SSH key to the terminal window. It will start with **ssh-rsa** and end with your email address
* Copy the SSH key
* Go to GitHub and click on your profile picture in the top right
* Choose **Settings**
* Go to **SSH and GPG Keys** in the left sidebar
* Click **Add SSH key**
* Add a name for the key so you can recognize it, paste your key into the **Key** field, and click **Add SSH key**. Confirm your password if necessary
---

