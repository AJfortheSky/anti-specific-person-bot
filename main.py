from hikari import GatewayBot, GuildMessageCreateEvent, Intents
from config import *
from mein_token import *


def get_token():
    if CONFIG_TOKEN is None:
        return TOKEN
    else:
        return CONFIG_TOKEN

def get_guild():
    if KKK is None:
        return DEFAULT_SEVER
    else:
        return KKK


def get_disliked_person():
    if JAKOBUS is None:
        return DISLIKED_PERSON
    else:
        return JAKOBUS

bot = GatewayBot(token=get_token(), intents=Intents.ALL)

@bot.listen()
async def stfu_pedo(event: GuildMessageCreateEvent):
    if event.member.id == get_disliked_person():
        await bot.rest.delete_message(event.channel_id, event.message_id)
        print('Pedo blocked lol')
    else:
        return

def main():
    bot.run()

if __name__ == '__main__':
    main()