# Sloovi Playwright Pytest

This framework was designed as a demo to test different components for Sloovi's web application using pytest-playwright.


## Installation

Step 1: Download Python 3.X.X

Download Python on your system (version 3.x.x) from the link below:

```bash
  https://www.python.org/downloads/
```

Step 3: Clone the SlooviDemo repository from GitHub:

```bash
  https://github.com/abdulhadi1997/SlooviDemo
```

Step 2: Download PyCharm

Download the setup file compatible to your system from the link provided below:

```bash
  https://www.jetbrains.com/pycharm/download/#section=windows
```

Step 3: Change the Python interpreter in the project settings

In case you already have a python version set up on your system you will have to set up the newer version in the Python Interpreter settings. 
Open the repository on PyCharm & press Ctrl+Alt+S to open the IDE settings and select Project SlooviDemo > Python Interpreter.

Step 4: Install Playwright for Pytest

Open a terminal or any command line interface and navigate to the root folder of the repository and install pytest & playwright as well as the required browsers:


```bash
  pip install pytest
```

```bash
  pip install pytest-playwright
```

```bash
  playwright install
```

Step 5: Set PYTHONPATH

To set PYTHONPATH as an environment variable for Windows, you can follow these instuctions here:

```bash
https://stackoverflow.com/questions/45022655/pythonpath-in-pycharm-and-windows-10-command-line
```

To set on macOS, set this command in the terminal directed to your root folder:

```bash
export PYTHONPATH=.
```

Step 6: Install HTML Reporter for Pytest

 ```bash
  pip install pytest-html
```
## Running Tests

To run all tests, run the following command

```bash
  pytest
```

After execution ends you can get your file from the reports folder which will have an HTML format generated report with an analysis of the execution attached with any screenshots taken on failure
 
