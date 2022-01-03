from discord.ext import commands, tasks
import os
from keep_alive import keep_alive
import json
from get_most_recent_tweets import get_tweets

with open('ids.json') as f:
    data = json.load(f)

CHANNEL_ID = data['CHANNEL_ID']
MINUTE_INTERVAL = data['MINUTE_INTERVAL']

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@tasks.loop(minutes=MINUTE_INTERVAL)  # repeat after every defined interval
async def send_update():
    await bot.wait_until_ready()
    channel = bot.get_channel(CHANNEL_ID)  # replace with channel ID that you want to send to
    most_recent_tweets = get_tweets(data, MINUTE_INTERVAL)

    if len(most_recent_tweets) > 0:
        for each_msg in most_recent_tweets:
            await channel.send(each_msg)


def main():
    keep_alive()
    send_update.start()
    bot.run(os.environ['BOT_TOKEN'])


if __name__ == '__main__':
    main()
