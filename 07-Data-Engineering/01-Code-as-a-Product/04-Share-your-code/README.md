## Objective

You have learned how to create a package, now we will see one of the benefits of packaging:
👉 Sharing a package with your colleagues

## How do I share my code ?

Simply create a GitHub repository for your package, and then everyone will be able to install your package using:

```bash
pip install git+https://github.com/<user.github_nickname>/mlproject
```

🤔 Still not clear ?
Remember the `packgenlite` package right ?
Inspect the [packgenlite github repo](https://github.com/krokrob/packgenlite) and run:

```bash
pip install git+https://github.com/krokrob/packgenlite
```

Then use it through ipython or a notebook:

```bash
from packgenlite.lib import get_data

get_data()
```

## Share your own library

You just saw how to opensource your package.

You will now share your package with all of your colleagues.

Your colleagues will install your package and run:

```python
from yourpackage.lib import try_me
```

Create a project with the `packgenlite` command:
 Create it outside of the `data-challenges` folder (`cd ~/code/<user.github_nickname>`)
- Name it as you please (avoid using dashes `-` or dots `.` in the name of your package, since this is against [package naming conventions](https://docs.python-guide.org/writing/structure/#modules) and makes importing your package harder)
- Add a `try_me()` function to `lib.py` file
- Insert any code you want in that function, try to be creative
- Create a [new public (obviously) repository](https://github.com/new) on github named after the name of your package
- Choose `... or push an existing repository from the command line`:

```bash
git remote add origin git@github.com:<user.github_nickname>/PACKAGE_NAME
git push -u origin master
```

Publish the `pip install` command on the slack channel of the batch, for your colleagues to install your package and run your function.

💡 __the command should look like `pip install git+https://github.com/<user.github_nickname>/PACKAGE_NAME`__

Your colleagues must have done the same thing. Add all their repositories to a `requirements.txt` file and test their functions.

## Bonus: Pypi, the last layer to Open Source

You can skip the following section, it is pure bonus, but worth reading.

This section is for you general knowledge and will not be usefull until you really want to opensource a package.

You probably wondered how to install your package with the `pip install PACKAGE_NAME` command rather than `pip install git+https://github.com/<user.github_nickname>/PACKAGE_NAME`...

#### Process to fully opensource your package:

- Create two accounts, one on [Pypi](https://pypi.org/account/register/) and one on [TestPypi](https://test.pypi.org/account/register/)
💡 __Pypi allows to officially opensource your package. TestPypi allows to test your package before pushing to Pypi__
- Follow [this tutorial](https://anweshadas.in/how-to-upload-a-package-in-pypi-using-twine/) in order to upload your package to pypi using [twine](https://twine.readthedocs.io/en/latest/)
