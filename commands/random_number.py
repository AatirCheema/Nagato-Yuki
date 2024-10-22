import random

async def random_number(message): 
#Feel free to change the name of the command (command is written twice to avoid a bug)
    if message.content == '!random' or message.content.startswith('!random '):
        try:
            _, min_value, max_value = message.content.split()
            min_value = int(min_value)  
            max_value = int(max_value)  
            
            if min_value < max_value:
                random_number = random.randint(min_value, max_value)
                await message.channel.send(f'Your random number between {min_value} and {max_value} is: {random_number}')
            else:
                await message.channel.send('Please ensure the minimum value is less than the maximum value.')
        
        except ValueError:
            
            await message.channel.send('Please provide two valid numbers as the range, e.g., `!random 1 100`.')