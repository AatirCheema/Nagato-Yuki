
async def actions(message):
    if message.content == '!commands' or message.content.startswith('!commands '):
        commands_message = (
            '`!role` : add role to yourself\n'
            '`!removerole`: remove role from yourself\n'
            '`!addrole`: add role to list of roles assignable to users (only available to daimyo)\n'
            '`!deleterole`: delete role from list of roles assignable to users (only available to daimyo)\n'
            '`!listroles`: list out the available roles to users\n'
            '`!quote`: randomly outputs a quote saved to a list and gives the user 30 seconds to guess who said it\n'
            '`!addquote`: add quote to list of quotes (available to samurai and above)\n'
            '`!deletequote`: remove quote from list (available to samurai and above)\n'
            '`!avatar`: shows the avatar of the user or user @d\n'
            '`!random`: outputs a random number within a specified range\n'
            '`!flip`: flips coin after 5 seconds\n'
            '`!bugreport`: report a bug with description followed by message link (you can attach images as well\n'
            '`!deletebug`: deletebugs by ID\n'
            '`!listbugs`: outputs a list of all current bugs along with IDs\n'
            '**Note: Role commands will only work in watemote**'
        )
        await message.channel.send(commands_message)
    else:
        
        return