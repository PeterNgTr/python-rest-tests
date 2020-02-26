Goal
=====

This project will basically perform API tests on this [HTTP API](https://reqres.in/api) combing with Pyest.

Installation
-------

That is not really required but it is better to have a Python version manager to help switch among the python version of your choice. You can use any managers as you like, however this one is simple and easy to use [pyenv](https://github.com/pyenv/pyenv)

- To install the refer python

    ```bash
    pyenv install 3.7.3
    ```

- To list what python versions you have

    ```bash
    pyenv versions
    ```

- To sets the global version of Python to be used in all shells

    ```bash
    pyenv global 3.7.3
    ```

- To other virtualenv users, the idea of a local Python might seem familiar. Indeed, a local Python created from pyenv is almost like a Python virtual environment. The main difference is that pyenv actually copies an entire Python installation every time you create a new pyenv version. In contrast, virtualenv makes use of symbolic links to decrease the size of the virtualenv’s. If you can’t function without your virtual environments anymore then fear not, for there is a plugin for that: pyenv-virtualenv. This plugin adds complete virtualenv functionality to pyenv:

   ```bash
   git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
   source ~/.bashrc
   pyenv virtualenv 3.7.3 venv
   ```

1. **Install pip**
   - **MacOS**
   Run the command:

      ```bash
      sudo easy_install pip
      ```

   - **Windows**
   Download [get-pip.py](https://bootstrap.pypa.io/get-pip.py) to a folder on your computer.
   Open a command prompt window and navigate to the folder containing get-pip.py and then run

      ```bash
      python get-pip.py
      ```

2. **Install Virtualenv** (skip if already installed)
   Virtualenv provides an isolated working copy of Python which allows you to work on a specific project without worrying about affecting other projects.

   To install it run the command:

   ```bash
   pip3 install virtualenv virtualenvwrapper
   ```

3. **Create project environment**
   Create a new virtual environment running the command:

   ```bash
   python3 -m venv your-environment
   ```

   This will create a new folder called `your-environment`.

   __NOTE__: It's suggested (but not required) to run the command outside the root folder of the project so we don't need to pollute the root folder or edit the `.gitignore` file.

4. **Activate env**
   To activate the virtual environment run

   ```bash
   source /path/to/your-environment/bin/activate
   ```

   To deactivate, simply run

   ```bash
   $deactivate
   ```

5. **Install all the required dependencies**
   After activating the virtual environment (step above) from the root of the project, proceed to install all the requirements.

   ```bash
   pip install -r requirements.txt
   ```

Run the tests
-------------

**Run all the tests:**

```bash
pytest tests/*
```

**Run a specific test:**

```bash
pytest -k "test_get_valid_user"
```

**Run all the tests in parallel:**

```bash
pytest tests/* -n 4
```

**Run all the tests and generate the HTML report:**

```bash
pytest tests/* --html=report.html
```

Troubleshooting
--------------

Python installation

- On MacOS (for instance), you may get this error while installing the python `Install failed, "zlib not available"`, don't panic, it's easy to fix the issue, run the following command:

    ```bash
    sudo installer -pkg /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg -target /
    ```
