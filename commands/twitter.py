import re
import discord 

TWITTER_VIDEO_REGEX = r"(https?://(?:www\.)?(?:x\.com|twitter\.com)/.+/status/\d+(\?.*)?)"
TWITTER_VIDEO_SPOILER_REGEX = r"\s*\|\|\s*(https?://(?:www\.)?(?:x\.com|twitter\.com)/.+/status/\d+(\?.*)?)\s*\|\|\s*"


def convert_to_vxtwitter(twitter_url):
    if "x.com" in twitter_url:
        return twitter_url.replace("x.com", "vxtwitter.com")
    elif "twitter.com" in twitter_url:
        return twitter_url.replace("twitter.com", "vxtwitter.com")
    return twitter_url

async def handle_twitter_link(message):

    spoiler_match = re.search(TWITTER_VIDEO_SPOILER_REGEX, message.content)

    if spoiler_match:
        twitter_url = spoiler_match.group(1)
        await message.edit(suppress=True)
        vxtwitter_url = convert_to_vxtwitter(twitter_url)

        #print(f"Found Twitter link inside spoiler: {twitter_url}")


        edited_content = message.content.replace(twitter_url, f" || {vxtwitter_url} || ")
        try:
            await message.edit(content=edited_content)
            print(f"Edited the original spoiler to prevent the embed.")
        except discord.errors.Forbidden:
            print("Bot doesn't have permission to edit messages.")

        await message.reply(f" || {vxtwitter_url} || ", mention_author=False)
        return  

    match = re.search(TWITTER_VIDEO_REGEX, message.content)

    if match:
        twitter_url = match.group(1)
        await message.edit(suppress=True)
        vxtwitter_url = convert_to_vxtwitter(twitter_url)

        print(f"Found Twitter link: {twitter_url}")

        try:

            edited_content = message.content.replace(twitter_url, f"`{twitter_url}`")

            await message.edit(content=edited_content)

            print(f"Edited the original message to prevent the embed.")
        except discord.errors.Forbidden:
            print("Bot doesn't have permission to edit messages.")

        await message.reply(vxtwitter_url, mention_author=False )
