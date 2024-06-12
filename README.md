# Battery notification
This Python script checks the battery percentage of your macOS device and provides notifications using `osascript`
and `say` commands when the battery is either too low (<= 30%) or too high (>= 80%)

## Requirements
* [macOS](https://www.apple.com/)
* [Python 3](https://www.python.org/)
* [psutil](https://pypi.org/project/psutil/)

## Installation
1. Clone the repository:
    ```sh 
    git clone https://github.com/everthinq/mac.battery.git
   ```
2. Install the required dependencies:
    ```sh 
    pip install -r requirements.txt
   ``` 
3. Open the crontab editor:
    ```sh
    crontab -e
   ```
4. [Instead of getting frustrated trying to insert something, just learn how to use vim](https://www.geeksforgeeks.org/basic-vim-commands/)
5. Schedule the script to run every minute, change the directory of `battery.py`:
    ```sh
    */1 * * * * python3 /Users/everthinq/Projects/battery/battery.py
   ```
6. [Check crontab.guru and change the schedule if you want](https://crontab.guru/#*/1_*_*_*_*)
