# <package name>

###### <package description>

## Quickstart

- Remove any files that are not necessary for your project. File usages are as follows:
  - Core files:
    - `(packagename)\__init__.py`
    - `tools\testcoverage.bat`
    - `.gitignore`
    - `README.md`
  - Files which facilitate running your project as an application:
    - `(packagename)\__main__.py`
    - `tools\start-dev.bat`
    - `tools\update.py`
    - `requirements.txt`
    - `start.bat`
  - Files which facilitate publishing your project as a package:
    - `tools\setup.bat`
    - `LICENSE.txt`
    - `MANIFEST.in`
    - `setup.py`
  - Files which facilitate freezing your project into a .exe file:
    - `main.py`
- If you do not want your project to open a terminal when it is run:
  - Rename `main.py` to `main.pyw` (if the file is still in your project)
  - Rename `(packagename)\__main__.py` to `(packagename)\__main__.pyw` (if the file is still in your project)
  - Inside `start.bat`, replace `pythonw` with `python` (if the file is still in your project)
- Find and replace any text surrounded with angle brackets (`<` and `>`) with the expected value as indicated inside the brackets
- Double-check any lines commented with exactly five hash symbols (`#####`) have the correct values
- Find and replace any file and folder names entirely contained inside parentheses (`(` and `)`) with the expected value as indicated inside the parentheses
- Remove this bullet list from the readme file once complete
