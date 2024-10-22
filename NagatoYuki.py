import discord
import os

from commands.quotes import handle_quote_command, handle_quote_management, active_quotes
from commands.roles import role_command 
from commands.random_message import check_random_message, message_counter
from commands.random_number import random_number
from commands.welcome import send_welcome_message  
from commands.twitter import handle_twitter_link
from commands.pixiv import handle_pixiv_link
from commands.avatar import handle_avatar_command
from commands.coin_flip import handle_coin_flip_command
from commands.actions import actions
from commands.bugs import handle_bug_report, handle_delete_bug, handle_list_bugs

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True  
intents.members = True  
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await handle_quote_command(message, active_quotes, client)

    await handle_quote_management(message)

    await role_command(message)

    await random_number(message)

    await handle_twitter_link(message)

    await handle_pixiv_link(message)

    await check_random_message(message, message_counter)

    await handle_avatar_command(message)
    
    await handle_coin_flip_command(message)

    await actions(message)

    await handle_bug_report(message, client)

    await handle_delete_bug(message)

    await handle_list_bugs(message)

@client.event
async def on_member_join(member):
    
    await send_welcome_message(client, member)  

# Run the bot
TOKEN = '0000000000000000000000' #TOKEN HERE
client.run(TOKEN)
