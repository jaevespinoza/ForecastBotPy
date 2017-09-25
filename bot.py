import discord
from datetime import datetime
import random

client = discord.Client()
global nowtime, previous, currentweather, firstime, currentime, weather, timeofday


def setup():
    global nowtime, previous, currentweather, firstime, currentime, weather, timeofday
    nowtime = datetime.now().time()
    previous = 0
    currentweather = random.randint(0, 9)
    firstime = True
    currentime = 0
    weather = ["Sunny", "Rainy", "Cloudy", "Clear", "Humid", "Thunderstorm", "Windy", "Snowy", "Torrential", "Cold"]
    timeofday = ["Morning", "Afternoon", "Night"]


@client.event
async def on_ready():
    setup()
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    global nowtime, previous, currentweather, firstime, currentime, weather, timeofday
    nowtime = nowtime
    if message.content.startswith("!forecast"):
        timenow = datetime.now().time()
        if timenow.second - nowtime.second > 86400 or firstime:
            previous = currentime
            await client.send_message(message.channel, 'New weather report:\n' + 'Time of day: ' + timeofday[currentime] + '\nWeather: ' + weather[currentweather])
            currentime += 1
            firstime = False
            if currentime > 2:
                currentime = 0
                currentweather = random.randint(0, 9)

        else:
            await client.send_message(message.channel, 'Time of day: ' + timeofday[previous] + '\nWeather: ' + weather[currentweather])


client.run('MzYwMjY2MzEyNTgyMTY4NTc2.DKTJ9g.C6GYuhC1_YY0ePox6RGWpfd62C8')
