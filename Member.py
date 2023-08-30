# Telegam-member-scrape

from telethon.sync import TelegramClient

api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'

group_username = 'GROUP_USERNAME'

with TelegramClient('session_name', api_id, api_hash) as client:
    group_entity = client.get_entity(group_username)
    
    members = client.get_participants(group_entity)
    
    usernames = []
    
    for member in members:
        if member.username:
            usernames.append(member.username)
    
    with open('usernames.txt', 'w') as file:
        for username in usernames:
            file.write(username + '\n')

print("Usernames scraped and saved to 'usernames.txt'.")
