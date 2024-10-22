import random
import asyncio

#Feel freee to change the name of the command (command is written twice to avoid a bug)
async def handle_coin_flip_command(message):
    if message.content == '!flip' or message.content.startswith('!flip '):

        # Delay set to 5 seconds
        await asyncio.sleep(5)

        # Randomly choose between "Heads" and "Tails"
        result = random.choice(['Heads', 'Tails'])

        await message.channel.send(result)

        # Delete the user's inital command
        await message.delete()