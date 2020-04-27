## Clone Package builder and install it

Get package builder from github package git@github.com:lologibus2/wagon_tools.git


## Install package

Before doing anything here, please make sure _**you are inside a python3 virtual environment**_

```bash
git clone git@github.com:lologibus2/wagon_tools.git
cd wagon_tools
make clean install
```

Quite a lot of things happened. Amongst others, you have install a `wagon-make-package` script.  

This script will be your package builder.

Now let's suppose you start a new ML project, you want to package your code somewhere.  

You now have access to a cool script that you can run from anywhere on your laptop

Go somewhere you want to project to live, and build your first package:

```bash
wagon-make-package mlproject
```

Now go into the project you've just built. Here is the project structure where you'll want to use to package your code.  
Check how your package is structured by running `tree` command or just `ls` if tree not installed  





