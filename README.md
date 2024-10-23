# Nagato-Yuki
Nagato Yuki is a multifunction discord bot written completely in python. Nagato can do the following:
***Role management
Convert twitter links to vxtwitter links
Convert pixiv links to phixiv
Random number generator
Coin flip
Quote
Random quote  
Bug report
***
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
The output will be any number within the range of 
