# Work with Python 3.6
import discord
from discord.ext import commands
import urllib
# import lxml
# import yaml
import os
import logging
from twilio.rest import Client

logging.basicConfig(level=logging.INFO)


class TaskmasterBot(object):

    def sendSMS(self, message):
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN'] 
        num_from = os.environ['TWILIO_NUMBER']
        num_to = os.environ['RECIPIENTNUMBER']
        client = Client(account_sid, auth_token)
        if len(message) < 160:
            message = client.messages \
                .create(
                     body=message,
                     from_=num_from,
                     to=num_to
                 )
            return True
        else:
            return False


bot = commands.Bot(command_prefix="?", description="TaskmasterBot")

@bot.command()
@commands.has_permissions(administrator=True)
async def sendSMS(ctx, message):

    """
    SendSMS to predefined person
    :param ctx:
    :return:
    """
    result = m.sendSMS(message)
    if result == True:
        await ctx.send("Message Sent")
    else:
        await ctx.send("Message Too Long Try Again, Max 160 characters")

@bot.event
async def on_ready():
    print(f"{bot.user.name} - {bot.user.id}")
    print(discord.__version__)
    print("Ready")


if __name__ == "__main__":
    token = os.getenv("TOKEN", None)
    if token:
        m = TaskmasterBot()
        bot.run(token)
    else:
        print("No Token Found")
