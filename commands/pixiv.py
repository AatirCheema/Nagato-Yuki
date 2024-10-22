import re
import discord

PIXIV_REGEX = r"\s*\|\|\s*(https?://(?:www\.)?(pixiv\.net)/.+?/(\d+))\s*\|\|\s*|(https?://(?:www\.)?(pixiv\.net)/.+?/(\d+))"

# Convert Pixiv link to phixiv link
def convert_to_phixiv(pixiv_url):
    return pixiv_url.replace("pixiv.net", "phixiv.net")

async def handle_pixiv_link(message):

    match = re.search(PIXIV_REGEX, message.content)

    if match:
        # Determine if the URL was in spoiler tags
        if match.group(1):  
            pixiv_url = match.group(1)
            is_spoiler = True
        else:  
            pixiv_url = match.group(4)
            is_spoiler = False

        # Suppress the original embed
        await message.edit(suppress=True)  
        
        # Convert Pixiv URL to Phixiv
        phixiv_url = convert_to_phixiv(pixiv_url)
        
        # Log the found link for debugging purposes
        # print(f"Found Pixiv link: {pixiv_url}")

        # Modify the original message to prevent the embed
        try:
            # If the link was in spoilers, keep it wrapped in `||`
            if is_spoiler:
                edited_content = message.content.replace(f"||{pixiv_url}||", f" || {phixiv_url} || ")
            else:
                edited_content = message.content.replace(pixiv_url, f"`{phixiv_url}`")

            # Edit the message to remove the original link (thus stopping the embed)
            await message.edit(content=edited_content)

            print("Edited the original message to prevent the embed.")

        except discord.errors.Forbidden:

            print("Bot doesn't have permission to edit messages.")

        # Reply with spoiler markers
        if is_spoiler:
            await message.reply(f" || {phixiv_url} || ", mention_author=False)
        else:
            await message.reply(phixiv_url, mention_author=False)

    #else:
        #print("No Pixiv link found.")
