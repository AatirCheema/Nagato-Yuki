import discord
import random
import re  # For link detection

intents = discord.Intents.default()
client = discord.Client(intents=intents)

message_counter = {}

# List of blacklisted words
blacklisted_words = ["test", "hello", "hi"] 

# List of user IDs to ignore, primarily for bot messages
ignored_users = [00000000000000]  # Replace with user IDs

# Delete below if you want it to be able to repost links
def contains_link(message_content):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')  
    return url_pattern.search(message_content) is not None

def contains_blacklisted_word(message_content):
    for word in blacklisted_words:
        if word.lower() in message_content.lower():
            return True
    return False

async def get_random_recent_message(channel):
    # Number of messages it'll go back and read from. Currently set to 10000.
    messages = [message async for message in channel.history(limit=10000)]
    
    if messages:
        random_message = random.choice(messages)

        # Avoid command messages as well
        if (random_message.author == client.user or 
            random_message.author.id in ignored_users or 
            contains_link(random_message.content) or 
            contains_blacklisted_word(random_message.content) or 
            random_message.content.startswith("!")):
            return await get_random_recent_message(channel)
        else:
            return random_message.content
    else:
        return "No messages found."

async def check_random_message(message, message_counter):
    if message.channel.id not in message_counter:
        message_counter[message.channel.id] = 0

    message_counter[message.channel.id] += 1

    print(message_counter) # Prints the number of messages, to the command line, sent in each channel the bot can read

    if message_counter[message.channel.id] >= 1000: # Number of messages before a random message may be sent
        message_counter[message.channel.id] = 0
        random_recent_message = await get_random_recent_message(message.channel)
        await message.channel.send(f"{random_recent_message}")