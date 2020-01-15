import discord
import asyncio
import constants #this will be a python script with the token and channel_id
#putting this information in a separate file prevents people without the constants.py file
#from having access to the bot's auth token, channel ID, and member user IDs.
import subprocess

delay = 1 #delay in seconds
members = constants.MEMBERS
token = constants.TOKEN
channel_id = constants.CHANNELID

#logging in
client = discord.Client()
await client.start(token, bot=True)
channel = get_channel(channel_id)

@client.event
async def on_message(message: str):
    if message.content.startswith("http"):
        with open("address.txt", "a") as myfile:
            myfile.write(message.content)
        subprocess.call(['./pushToHub.sh'])# dunno if this will work (might need to delete ./)
        await client.send_message(message.author, "Thanks! Now download the connector script here: [ https://github.com/ahl98/discordbots ]. You will have to install selenium.")
        await client.process_commands(message)

#main control loop
try:
    while (True)

    new_members = channel.recipients #only works for private channels, still working on how to get new members
    unseen = new_members - members #find new members
    members = new_members #update list of members

    #logic for if we found a new member
    if unseen != []:
        st = ''
        for name in unseen:
            st = st + ", " + name
        st = st[2:]
        message = "Connecting new members: " + st
        client.send_message(channel, message)

        #send each new member a message requesting linkedin profile page
        msg = "Please reply with a link to your LinkedIn profile. This link should be in the format 'http://www.linkedin.com/in/[firstname]-[lastname]-[alphanumeric string]/"
        for member_id in unseen:
            task = asyncio.ensure_future(send_message(member_id, msg))

        #update constants file
        with open("constants.py", "w") as f:
            f.writeline("TOKEN = " + token)
            f.writeline("CHANNELID = " + channel_id)
            f.writeline("MEMBERS = " + str(members))

    #delay so the server isnt going crazy checking constantly for new members
    time.sleep(delay)


#make sure we exit correctly in case it crashes
except:
    client.close()
