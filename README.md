# Speedtest Python Script

## Description

This repo contains is for a script that periodically executes the [speedtest cli](https://www.speedtest.net/apps/cli) and outputs to a csv file.

## Instructions

### Download script

Download the script `speedtest.py` script by cloning this repo or downloading the file directly.

### Install Python

First, check python installation
```
python3 --version
```

Python version 3.7 or greater is required.

### Install speedtest-cli

speedtest-cli can be install [via Pip](https://pypi.org/project/speedtest-cli/) or directly as [OS app](https://www.speedtest.net/apps/cli) 

### Adjust config

In the [speedtest script](./speedtest.py), the following params can be updated:
- `interval`
- `num_tests`

By default, the script executes once every 5 minutes.

### Execute script

To run the script, execute `python3 ./speedtest.py` from a shell/terminal.

The script will output a line per executed speedtest.
For example:
```
executing test 0
executing test 1
executing test 2
```