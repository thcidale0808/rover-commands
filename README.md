# Rover Commands CLI Tool

It's a CLI tool that apply coordinate instructions on rovers and return the results

## Pre-Requisites:

Install python 3 and pip.

## Environment Variables

- LOGLEVEL: Default value is INFO.

## Running locally

- `python3 -m venv env` to create virtual environment folder
- `source ./env/bin/activate` to activate virtual enviroment
- `pip install -r requirements.txt` to install all dependences
- `python3 -m pytest` to run all unit tests
- `python3 run.py --help` for CLI details
- `python3 run.py --input '[input path]' --output [output path]` to execute the tool.

### Example:

`python3 run.py --input input/data.txt --output output`
