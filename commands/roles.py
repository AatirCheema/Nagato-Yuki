import discord
import os 
import json

roles_file = "assignable_roles.json"
restricted_channel_id = 0000000000000000  # Replace with the ID of the allowed channel

if os.path.exists(roles_file):
    with open(roles_file, "r") as file:
        assignable_roles = json.load(file)
else:
    assignable_roles = []

authorized_users = [000000000000]  # Replace with user IDs
authorized_roles = [000000000000]  # Replace with role IDs


def save_roles():
    with open(roles_file, "w") as file:
        json.dump(assignable_roles, file)


def is_user_authorized(user):
    return user.id in authorized_users or any(role.id in authorized_roles for role in user.roles)

async def role_command(message):

    if message.content.startswith(('!role', '!addrole', '!deleterole', '!removerole', '!listroles')):

        if message.channel.id != restricted_channel_id:
            await message.channel.send(f"You can only use role commands in <#{restricted_channel_id}>.")
            return

 
    if message.content == '!role' or message.content.startswith('!role '):
        try:
            _, role_name = message.content.split(maxsplit=1)
            
    
            role_data = next((role for role in assignable_roles if role['name'] == role_name), None)
            
            if role_data:
          
                role = discord.utils.get(message.guild.roles, id=role_data['id'])
                
                if role:
                
                    if role in message.author.roles:
                        await message.channel.send(f'You already have that role.')
                    else:
                      
                        await message.author.add_roles(role)
                        await message.channel.send(
                            f'You have been assigned: <@&{role.id}>', 
                            allowed_mentions=discord.AllowedMentions(roles=False)
                        )
                else:
                    await message.channel.send(f'That role does not exist in this server.')
            else:
                await message.channel.send(f'That is not an assignable role. To view a list of assignable roles type `!listroles`')
        
        except ValueError:
            await message.channel.send(f'Usage: `!role <role_name>`. To view a list of assignable roles type `!listroles`')

    # Admin only commands
    elif message.content == '!addrole' or message.content.startswith('!addrole '):
        try:
            if is_user_authorized(message.author):
                _, new_role_name = message.content.split(maxsplit=1)
                
           
                role = discord.utils.get(message.guild.roles, name=new_role_name)
                
                if role:
                    if not any(r['id'] == role.id for r in assignable_roles):
                        assignable_roles.append({'name': new_role_name, 'id': role.id})
                        save_roles()  
                        await message.channel.send(
                            f'<@&{role.id}> has been added to the list of assignable roles.',
                            allowed_mentions=discord.AllowedMentions(roles=False)
                        )
                    else:
                        await message.channel.send(f'That is already an assignable role.')
                else:
                    await message.channel.send(f'That role does not exist on this server. ')

            else:
                await message.channel.send('You do not have permission to add roles.')

        except ValueError:
            await message.channel.send('Usage: `!addrole <role_name>`')

    # Admin only commands
    elif message.content == '!deleterole' or message.content.startswith('!deleterole '):
        try:
            if is_user_authorized(message.author):
                _, role_to_remove_name = message.content.split(maxsplit=1)
                
                role_data = next((role for role in assignable_roles if role['name'] == role_to_remove_name), None)

                if role_data:
                    assignable_roles.remove(role_data)
                    save_roles()  # Save the updated roles list
                    await message.channel.send(
                        f'It has been removed from the list of assignable roles.',
                        allowed_mentions=discord.AllowedMentions(roles=False)
                    )
                else:
                    await message.channel.send(f'That role is not in the assignable list.')
            else:
                await message.channel.send('You do not have permission to delete roles.')

        except ValueError:
            await message.channel.send('Usage: `!deleterole <role_name>`')


    elif message.content == '!removerole' or message.content.startswith('!removerole '):
        try:
            _, role_name = message.content.split(maxsplit=1)

            role_data = next((role for role in assignable_roles if role['name'] == role_name), None)

            if role_data:
                role = discord.utils.get(message.guild.roles, id=role_data['id'])

                
                if role in message.author.roles:
                    await message.author.remove_roles(role)
                    await message.channel.send(
                        f'<@&{role.id}> has been removed from you.',
                        allowed_mentions=discord.AllowedMentions(roles=False)
                    )
                else:
                    await message.channel.send(f'You do not have that role.')
            else:
                await message.channel.send(f'That role is not assignable.')
        
        except ValueError:
            await message.channel.send('Usage: `!removerole <role_name>`')

    elif message.content == '!listroles':
        if assignable_roles:
            role_list = "\n".join([f"<@&{role['id']}>" for role in assignable_roles])
            await message.channel.send(
                f'Assignable roles:\n{role_list}',
                allowed_mentions=discord.AllowedMentions(roles=False)
            )
        else:
            await message.channel.send('No roles are currently assignable.')
