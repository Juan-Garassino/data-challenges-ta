## Background & Objectives

`Sqlite` is a simple database that relies on a standalone file.
You can read more on [en.wikipedia.org/wiki/SQLite](http://en.wikipedia.org/wiki/SQLite).

The goal of this first exercise is to use the command line to read and query
a sample database called `jukebox.sqlite` that we give you

### Setup

First test just to see if you have sqlite3 installed on your computer:

```bash
sqlite3 --version
```

If you don't have it, you can install it by running:

- Mac: `brew install sqlite`
- Ubuntu: `sudo apt-get install sqlite3 libsqlite3-dev`
- Window:

```
# Sqlite3
​
To persist our data, we need a database.
We are going to use Sqlite3.
​
Please go to [sqlite download](https://www.sqlite.org/download.html) and under "Precompiled Binaries for Windows", click on "sqlite-dll-win32-x86-xxxxxxx.zip".
​
A popup will appear at the bottom of the page, click on "Save".
​
The popup will change and click on "Open folder".
​
Open a new explorer window and go to C:
​
Create a new folder there and call it "sqlite".
​
Go to the downloaded file and right click on it and chose "Extract All". Click on "Extract".
​
A new window will open with 2 files in it. Copy those files in the C:/sqlite/
​
Go back to the website and this time under "Precompiled Binaries for Windows", click on "sqlite-tools-win32-x86-xxxxxxx.zip".
​
A popup will appear at the bottom of the page, click on "Save".
​
The popup will change and click on "Open folder".
​
Open a new explorer window and go to C:
​
Create a new folder there and call it "sqlite".
​
Go to the downloaded file and right click on it and chose "Extract All". Click on "Extract".
​
A new window will open with 2 files in it. Copy those files in the C:/sqlite/
​
Open a new Git Bash terminal and run the following command:
​
```bash
echo 'export PATH="/c/sqlite/:${PATH}"' >> .bash_profile
```
​
Restart your Git Bash terminal.
​
To make sure everything works, please run the following command:
​
```bash
sqlite3 -version
```
​
You should get an answer like: "3.30.0.....", if not please ask a TA.
```


You can open the database we provided you to make some queries on it:

```bash
sqlite3 lib/db/jukebox.sqlite
```

You are now in the interactive sqlite3 console and you can write your SQL queries to the database.
You can exit the sqlite3 console with `.quit` or `CTRL+D`.

## Tools

You can also use a **SQLite viewer** application to read the SQLite database, explore the schema and even **run SQL queries**.

- [SQLite Pro (macOS only, paying but trial seems unlimited)](https://www.sqlitepro.com/)
- [SQLStudio (Free)](http://sqlitestudio.pl/)
- [SQLite Browser (Free)](http://sqlitebrowser.org/)

❓Should I use the command-line `sqlite3` or one of the visual tool above? Well, both are useful! It's good to learn a bit to manipulate the command line for two reasons. On the one hand, a [CLI](https://en.wikipedia.org/wiki/Command-line_interface) allows you to focus on the SQL queries. On the other hand, a [GUI](https://en.wikipedia.org/wiki/Graphical_user_interface) tool will prove helpful to explore a database schema structure (tables? columns? etc.). Try both!

## Specs

The goal of this exercise is to explore the Jukebox database, and understand its schema. Answer the following questions:

- What is the database schema? (i.e what are the tables, and the relations between tables)
- Use SQL Design tool to draw the schema of this database.
- How many rows does each table contain? What are the column names for each table?

Use [db.lewagon.com](http://db.lewagon.com/) to draw the Jukebox schema. Save it in XML format to `jukebox.xml` and check it with `make`.
