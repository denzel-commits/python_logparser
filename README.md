# What is "Apache2 webserver log parser"?

"Apache2 webserver log parser" is a command line tool that parse and analyse "access.log".

## Features
It can be used to get the following information:
- Overall number of requests done
- Requests count per each HTTP METHOD
- TOP 3 IP addresses that do requests

---
# Requirements

Python version 3.9 or greater

---

# Install

To install the "Apache2 webserver log parser" from the command line, do the following.

1. Download it from repository: `git clone -b develop git@github.com:denzel-commits/python_logparser.git`
2. Go to project folder: `cd python_logparser`
3. Create virtual environment: `python3 -m venv venv`
4. Activate virtual environment: `source venv/bin/activate`
5. You can install it now with the following command: `pip install -r requirements.txt`

This installs all modules required to run the tool.

---

# Run

You should now be able to run "Apache2 webserver log parser" with the following command and additional options:

``$ (venv) python app.py [options]``
OR
``$ /path/to/project/venv/bin/python app.py [options]``

---

# Help

To see a general help menu and available commands for "Apache2 webserver log parser", run:

$ python app.py --help

---

# Options

"Apache2 webserver log parser" accepts 2 options, short alias and full name:

* -f, --logfile: path to log file to parse
* -d, --logdir: path to log directory with log files to parse
* -o, --output: path to output file

The "logfile" option is optional, "access.log" file to parse and analyze.

The "logdir" option is optional, directory with "access.log" files to parse and analyze. All log files within this directory will be parsed.

The "output" option is optional, file path. If specified will be used as destination for results. If not specified default file will be used "results.json".

---

# Usage examples

* $ python app.py -f log/access.log -o results.json
* $ python app.py -d log/
