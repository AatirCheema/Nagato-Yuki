import discord

async def handle_avatar_command(message):
    
    #feel freee to change the name of the command
    if message.content == '!avatar' or message.content.startswith('!avatar '):
        parts = message.content.split()

        if len(parts) > 1:
            try:
                user = message.mentions[0]
            except IndexError:
                await message.channel.send("Please mention a valid user.")
                return
        else:
            user = message.author

        avatar_url = user.avatar.url if user.avatar else user.default_avatar.url

        # Specify the size of the avatar (can be adjusted)
        avatar_url += "?size=1024"

        await message.channel.send(avatar_url)
