import random
import os
import json
import asyncio
import discord

quotes_file = "quotes.json"
active_quotes = {}

# List of authorized user IDs or role IDs
authorized_users = [00000000000000]  # Replace with user IDs 
authorized_roles = [00000000000000]  # Replace with role IDs


def load_quotes():
    if os.path.exists(quotes_file):
        with open(quotes_file, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []  
    return []


def save_quotes(quotes):
    with open(quotes_file, "w") as file:
        json.dump(quotes, file, indent=4)


def get_random_quote():
    quotes = load_quotes()
    if quotes:
        return random.choice(quotes)
    else:
        return None  


def add_quote(quote_text, author):
    quotes = load_quotes()
    new_quote = {"quote": quote_text, "author": author}
    quotes.append(new_quote)
    save_quotes(quotes)


def remove_quote(quote_text, author):
    quotes = load_quotes()
    quote_to_remove = {"quote": quote_text, "author": author}
    
    if quote_to_remove in quotes:
        quotes.remove(quote_to_remove)
        save_quotes(quotes)
        return True
    else:
        return False  


def parse_quote_command(content):
    if ' -' in content:
        quote, author = content.split(' -', 1)
        return quote.strip(), author.strip()
    else:
        return None, None


def is_user_authorized(user):
    return user.id in authorized_users or any(role.id in authorized_roles for role in user.roles)


async def handle_quote_command(message, active_quotes, bot):
    if message.content == '!quote':
        random_quote = get_random_quote()

        if random_quote:
            
            quote_text = random_quote["quote"]
            author = random_quote["author"]
                
            if author:
               
                active_quotes[message.guild.id] = author

                
                await message.channel.send(quote_text)

                # Question message
                await message.channel.send("Guess who said this? :face_with_raised_eyebrow: ")

                try:
                    
                    def check(m):
                        return m.channel == message.channel and m.content.lower() == author.lower()

                    # Time alloted for response is set to 30. Feel free to change it.
                    guess = await bot.wait_for('message', check=check, timeout=30.0)
                    # Correct answer message
                    await guess.reply('Correct!') 

                except asyncio.TimeoutError:
                    # Wrong answer message
                    await message.channel.send(f"Time's up. The correct answer was {author}.")
                
                # Remove the active quote after the game ends
                del active_quotes[message.guild.id]

            else:
                await message.channel.send("Couldn't find the author of this quote.")
        else:
            await message.channel.send("No quotes available right now.")

async def handle_quote_management(message):
    if message.content.startswith('!addquote'):
        if not is_user_authorized(message.author):  # Check authorization for addquote
            await message.channel.send("You are not authorized to use this command.")
            return
        
        content = message.content[len('!addquote '):].strip()
        quote_text, author = parse_quote_command(content)
        
        if quote_text and author:
            add_quote(quote_text, author)
            await message.channel.send(f"Quote added: \"{quote_text}\" -{author}")
        else:
            await message.channel.send("Usage: `!addquote quote here -author`")

    elif message.content.startswith('!deletequote'):
        if not is_user_authorized(message.author):  # Check authorization for removequote
            await message.channel.send("You are not authorized to use this command.")
            return
        
        content = message.content[len('!deletequote '):].strip()
        quote_text, author = parse_quote_command(content)
        
        if quote_text and author:
            if remove_quote(quote_text, author):
                await message.channel.send(f"Quote deleted: \"{quote_text}\" -{author}")
            else:
                await message.channel.send(f"Quote not found: \"{quote_text}\" -{author}")
        else:
            await message.channel.send("Usage: `!deletequote quote here -author`")
