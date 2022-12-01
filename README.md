# CS 533 Script Demo

This repository demonstrates creating and using scripts for managing data.
It is set up to be able to run in GitHub Codespaces.

To use this repository:

- Fork the repository to your GitHub account with the “fork” button
- Open the repository in CodeSpaces — click the ”Code” menu/button, and select “Create codepsace on main”

This will create a new Linux virtual machine on GitHub's infrastructure, install Anaconda along with the
dependencies specified in `environment.yml`, and open Visual Studio Code in a browser tab to browse and
navigate the project.  It includes a copy of the `ml-latest-small` data set from [GroupLens](https://grouplens/datasets/movielens).

## Understanding the Code

The `rating-stats.py` file is a *text file* — a file that only contains plain
text, that you can edit with VS Code, Notepad, or any other *text editor*.  This
file contains Python code that you can run. You can create such a file by using
“New File” in Visual Studio Code.

This script uses the `docopt` library for parsing command line arguments, but you
can also parse the arguments yourself from the `sys.argv` variable.

## Using the Code

When you open the codespace, it will open a "Terminal" in the bottom of the
screen. This is a command-line prompt just like the one on your own computer (if
you are on Mac or Linux; it's similar but not quite the same on Windows).  This
command prompt is running in your codespace on GitHub.

You can run the `rating-stats.py` file by entering the following in the terminal:

    python rating-stats.py ml-latest-small

This will load the ratings file, compute user and item statistics, and write them
into the corresponding output files.

You can then open the `StatsAnalysis.ipynb` notebook to analyze the results.  You
can do this in one of two ways:

- Run `jupyter notebook` in the terminal; VS Code detect that it ran and will
  then give you an option to open the notebook server in your browser.
- Open the notebook in VS Code, which has pretty good notebook support.

## Other Things of Note

The `.gitignore` file tells Git to ignore the Jupyter checkpoint directories, as well
as your output files.