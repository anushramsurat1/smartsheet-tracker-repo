# ise-as-poc
This repository holds all of the ISE proof of concept code.

Instructions to run ISE PoC Web Application:

Git clone the following repository onto your local machine: https://wwwin-github.cisco.com/spa-ie/ise-as-poc

Then, go into the folder 'ise-as-poc/flask/flaskr', and to first set up the virtual environment, run the following commands:

virtualenv -p python3 ./venv3
source ./venv3/bin/activate

Then, from inside the same directory specified, run the following commands to install Flask and pyaml:

pip install Flask
pip install pyaml


Finally, to run the app, run the following commands:

export FLASK_APP=flaskr.py
flask run


After this, go to the following IP: 127.0.0.1:5000 in a web browser to access the app.

# smartsheet-tracker
