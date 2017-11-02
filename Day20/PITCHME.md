---
# Lists (and more Git)

Intro to Programming - Day 20
---
# Do Now

Log in to GitHub using the account you created. Go to my [repository for today's assignment](https://github.com/UCMHS-Gerstein/intro-to-lists) and fork it by clicking on the fork button in the upper right corner. This will make a copy of the repository on your account.
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
+++
* Go to **SSH and GPG Keys** in the left sidebar
* Click **Add SSH key**
* Add a name for the key so you can recognize it, paste your key into the **Key** field, and click **Add SSH key**. Confirm your password if necessary
---
# Cloning

* Cloning makes a local copy of your remote repository
* Go to your copy of the repository - if you have trouble finding it, the URL should be https://github.com/USERNAME/intro-to-lists
* Click on the green **Clone or download** button and copy the url provided - https://github.com/USERNAME/intro-to-lists.git
* In your Bash console, use the **clone** command:

```shell
git clone https://github.com/USERNAME/intro-to-lists.git
```
---
# Lists

* Ordered list of values
* Zero-indexed
* Comma separated values in square brackets
+++
# Examples

* `[1, 2, 3, 4, 5]`
* `['aardvark', 'bear', 'cat', 'dog', 'elephant']`
+++
# Try It

In **exercise1.py**, insert values into the `my_list` variables. What happens when you run it? Try changing the variable. Can you use different types of values? Is it always in the same order? Stage and commit your changes
---
# Index

* An item's position in the list is called its **index**
* The first index is 0
* `my_list[0]` returns the first item in the list called **my_list**
* `my_list[3]` returns the fourth item in the list called **my_list**
* You can work backwards, too: `my_list[-1]` returns the last item in the list called **my_list**
* `my_list[-3]` will return the third item from the end
+++
# Try It

In **exercise2.py** follow the directions. Did the code work as you expected? Did you run into any problems? Stage and commit your changes
---
# Slicing

You can use slices to return a section of a list

* `my_list[2:4]` will return the chunk starting at index 2 and ending *right before* index 4. So index 4 is not included
* You can leave the start blank to start at 0, or leave the end blank to end with the last item
+++
# Try It

In **exercise3.py** follow the directions. Stage and commit your changes
---
# More Functions

* `len(my_list)` will return the length of the list. This is used a lot, so get used to seeing it
* `my_list.append(x)` will add **x** to the end of my_list. **x** cam be any valid value
* There are other functions associated with lists - you can check them out [here](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
+++
# Try It

In **exercise4.py** follow the directions. Stage and commit your changes