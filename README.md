# Battery notification
This Python script checks the battery percentage of your macOS device and provides notifications using `osascript`
and `say` commands when the battery is either too low (<= 30%) or too high (>= 80%)

## Requirements
* [macOS](https://www.apple.com/)
* [Python 3](https://www.python.org/)
* [psutil](https://pypi.org/project/psutil/)

## Installation
1. ```git clone https://github.com/everthinq/mac.battery.git```
2. ```pip install -r requirements.txt```