# Telegram-member-scrape

# Telegram Group Usernames Scraper

This Python program uses the Telethon library to scrape usernames of members from a Telegram group. It fetches the usernames and saves them to a text file.

## Prerequisites

1. Python 3.x installed on your system.
2. Telegram API credentials (API ID and API hash). You can obtain these by creating a Telegram API application [here](https://my.telegram.org/auth).

## Installation

1. Clone this repository or copy the program code into a `.py` file.
2. Install the `telethon` library using the following command:

   ```sh
   pip install telethon 




Replace 'YOUR_API_ID' and 'YOUR_API_HASH' in the code with your actual Telegram API credentials.

Replace 'GROUP_USERNAME' with the username of the Telegram group from which you want to scrape usernames.

Run the program using the following command:

``` python scrape_usernames.py  ```

The program will log in to your Telegram account, fetch the members of the specified group, and save their usernames to a text file named usernames.txt.

