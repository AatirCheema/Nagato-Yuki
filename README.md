# Nagato-Yuki
Nagato Yuki is a multifunction discord bot written completely in python. Nagato can do the following:  
***Role management  
Convert twitter links to vxtwitter links  
Convert pixiv links to phixiv  
Random number generator  
Coin flip  
Quote  
Random quote  
Welcome  
Avatar
Bug report***  
A list of all the commands can be seeng using:  
`!commands`
## Role Management
List of role commands:  
`!role (role to add to yourself)`  
`!removerole (role to remove from youself)`  
`!addrole (role to add to the list of assignable roles)`  
`!deleterole (role to remove from the list of assignable roles)`  
`!listroles`  
The function is designed so that you can lock it to a specific channel. This is to avoid clutter. The add and delete role commands are also set so only certain users can use them. 

## Converting Twitter (X) and Pixiv links

### Why it exists?

Pixiv and twitter are very commonly used for art posts. Twitter, now known as X, is also used for much more than that for things such as news, quotes, memes, etc. The format of the default share link often doesn't properly embed especially if it's a gif, video, or post with multiple images. Converting the link to a `vxtwitter` link will allow it properly embed regardless of the post. The same applies for pixiv however pixiv is excluseively used for art and it converts the links to `phxiv`. 

### How it works

The function is quite simple. You simply post any working `twitter.com` , `x.com`, or `pxiv.com` link and it'll automatically convert the link for you. There's even support for spoiler posts. This way if a user shares a spoiler link in this format `||x.com||`, Nagato will output `||vxtwitter.com||` to also have the output marked as a spoiler. 

## Random Number Generator

Command  
`!random min_value max_value`  
The output will be any number within the range designated.

## Coin flip

Command  
`!flip`  
The output will appear with a 5 second delay allowing the user(s) to decide on an option.

## Quote

### What is this?

This is a personalizable command where you can add and remove quotes to a list. Nagato then pulls a random quote from that list and allows the user(s) 30 seconds to guess who authored the quote it outputted. The add and delete quote commands are also set so that only certain users can add quotes to the list. 

### Commands
`!quote`  
`!addquote (quote here) -author`  
`!deletequote (quote here) =author`  

## Random Quote

This is another passive function where Nagato, after 1000 messages in a specific channel, pulls a random quote from the past 10000 messages from that same channel. These values cann all be easily adjusted from `random_message.py` script. It's set so that Nagato own messages, commands, and links won't be randomly outputed.

## Welcome Messages

When a new user is added to the server, Nagato can do the following:  
1. Automatically assign a role of your choosing to them
2. Post a welcome message
3. Send them a welcome DM
4. Send you a DM that a new user has joined

All these messages are easily adjustable in the `welcome.py` script. 

## Avatar

Command
`!avatar (@user)`
Will output a larger image of the @'d user's profile picture. The size of the output can be easily adjusted.  
*It's set curretnly set to 1024x1024.*


## Bugs

### Commands
`!bug report (Description of bug) (link to bugged message) (optional image file)`
`!listbugs`
`!detelbug (ID number)`


### How it works 

Everytime there's a bug reported, Nagato will let the user know in the channel that the bug has been reported. A detailed description of the bug can be seen in a channel you designate. The bug is then stored in a list and assigned an ID number. Once the bug is handled you can delete that bug by the designated ID number. 
*If you spot any bugs feel free to forward the bug report to me here!*

