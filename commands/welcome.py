import discord

# Replace with your main channel ID and role ID
MAIN_CHANNEL_ID = 000000000000000  # Welcome message channel
WELCOME_ROLE_ID = 000000000000000  # Welcome Role ID

client = discord.Client(intents=discord.Intents.all())

async def send_welcome_message(client, member):
    # 1. Send a welcome message to the main channel
    channel = member.guild.get_channel(MAIN_CHANNEL_ID)
    if channel:
        await channel.send(f"Welcome to the server, {member.mention}!")

    # 2. Assign the welcome role to the new member
    role = member.guild.get_role(WELCOME_ROLE_ID)
    if role:
        await member.add_roles(role)
        print(f"Assigned role {role.name} to {member.name}.")
    else:
        print(f"Role with ID {WELCOME_ROLE_ID} not found.")

    # Send a direct message to the new member
    try:
        await member.send(f"Put your message to new user here")
    except discord.Forbidden:
        print(f"Couldn't send DM to {member.name}.")

   # DM the server admin (replace with your user ID)
    your_user = await client.fetch_user() #user you want to DM
    if your_user:
        await your_user.send(f"{member.name} has joined the server.")