# Setting Up Your Repository

## Starting from scratch

1. Go to http://github.com and create a new repository called `FinalProject17`.
2. Near the top of your repository's Quick Setup page, copy the URL provided to get the direct URL for the repository. If you're on the main page of the repository instead of quick setup, you'll need to click the big green "Clone or Download" button to get to the URL.
3. In the command line of your bash console, navigate to wherever you'd like to place the repository.
4. `git clone <your_url>` will copy the remote repository onto your local computer (or your PythonAnywhere account's local computer) and link the local and remote repositories together.
5. Now you can use your repository as normal, and using `git push` will send your work to the remote repository.

## If you have a folder (or repository) on your local computer
1. Go to http://github.com and create a new repository called `FinalProject17`. Do not initialize with a readme, license, or gitignore or you'll have to go through extra steps. You can add the readme yourself.
2. If you haven't initialized your project folder as a git repository, use `cd` to navigate into the project folder and use `git init` to turn the folder into a git repository
3. To link your local repository with the remote one, without navigating outside of the project folder/git repository, use the following commands (the lines starting with # are comments and can be ignored):
```shell
git remote add origin remote repository URL
# Sets the new remote
git remote -v
# Verifies the new remote URL
```
4. The first time you push to the remote, you'll need to use `git push --set-upstream origin master` to make the necessary links, but after that you'll be able to use `git push`
