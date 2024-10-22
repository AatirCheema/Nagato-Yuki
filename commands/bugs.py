import json
import os
import discord

bug_report_file = 'bugs.json'
detailed_report_channel_id = 0000000000000000  # Channel ID for the channel where a detailed bug report will be outlined

def load_bugs():
    if os.path.exists(bug_report_file):
        with open(bug_report_file, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []  # Return an empty list if JSON is corrupted
    return []

def save_bugs(bugs):
    with open(bug_report_file, "w") as file:
        json.dump(bugs, file, indent=4)

def add_bug(bug_text, message_link, attachments=None):
    bugs = load_bugs()
    new_id = len(bugs) + 1  # Assign the next available ID
    new_bug = {
        "id": new_id,
        "bug": bug_text,
        "message": message_link,
        "attachments": attachments if attachments else []
    }
    bugs.append(new_bug)
    save_bugs(bugs)

def remove_bug_by_id(bug_id):
    bugs = load_bugs()
    for bug in bugs:
        if bug["id"] == bug_id:
            bugs.remove(bug)
            # Reassign IDs to remaining bugs
            for index, remaining_bug in enumerate(bugs):
                remaining_bug["id"] = index + 1
            save_bugs(bugs)
            return True
    return False  # Bug not found

# Function to list all bugs with attachments
def list_bugs():
    bugs = load_bugs()
    if not bugs:
        return "No bugs reported."
    
    report = "Bug Reports:\n"
    for bug in bugs:
        attachments = "\n".join(bug["attachments"]) if bug["attachments"] else "No attachments"
        report += f"ID: {bug['id']}, Description: {bug['bug']}, Message Link: {bug['message']}\nAttachments: {attachments}\n\n"
    return report

# Improved function to parse bug report command
def parse_bug_report_command(content):
    # Split the content at the last space to separate description from the message link
    if ' ' in content:
        bug_text, message_link = content.rsplit(' ', 1)
        return bug_text.strip(), message_link.strip()
    else:
        return None, None

# Function to handle bug report command
async def handle_bug_report(message, client):
    if message.content.startswith('!bugreport'):
        content = message.content[len('!bugreport '):].strip()
        bug_text, message_link = parse_bug_report_command(content)

        if bug_text and message_link:
            attachments = [attachment.url for attachment in message.attachments]  # Get attachment URLs

            add_bug(bug_text, message_link, attachments)
            await message.channel.send("The bug has been logged.")

            # Send detailed report to the specified channel
            detailed_channel = client.get_channel(detailed_report_channel_id)
            if detailed_channel:
                attachments_str = "\n".join(attachments) if attachments else "No attachments"
                detailed_report = f"New Bug Report:\nDescription: {bug_text}\nMessage Link: {message_link}\nAttachments: {attachments_str}"
                await detailed_channel.send(detailed_report)
            else:
                print("Detailed report channel not found.")
        else:
            await message.channel.send("Usage: `!bugreport (bug description) (message link) (attached image is optional)`")

# Function to delete a bug by ID
async def handle_delete_bug(message):
    if message.content.startswith('!deletebug'):
        try:
            bug_id = int(message.content[len('!deletebug '):].strip())
            if remove_bug_by_id(bug_id):
                await message.channel.send(f"Bug report with ID {bug_id} has been deleted.")
            else:
                await message.channel.send(f"No bug report found with ID {bug_id}.")
        except ValueError:
            await message.channel.send("Please provide a valid bug ID.")

# Function to handle listing bugs in response to the !listbugs command
async def handle_list_bugs(message):
    if message.content == '!listbugs':
        bug_list = list_bugs()
        await message.channel.send(bug_list)