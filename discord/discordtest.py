from PyLyrics import *
from random import *
import discord
from weather import Weather
import speech_recognition as sr

client = discord.Client()

startup_extensions = ["Music"]

class Main_Commands():
    def __init__(self,bot):
        self.bot = bot

help = "Commands:\n" \
       "coin flip: Flips a coin \n" \
       "weather in <city name>: gives the weather in specified city \n" \
       "forecast for <city name>: gives a 3 day forecast for the specified city \n" \
       "twitch link <name of twitch channel>: will link the twitch channel specified (must be specific name) \n" \
       "search lyrics <name of artist>,<name of song>: will search lyrics for given artist and song(for some reason does" \
       " not like eminem... \n" \
       "repeat <text> : will repeat whatever you type \n" \
       "you could also ask a magic 8 ball style question by typing 'hey bot' followed by the question"

@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):

    if message.content.startswith('twitch link'):
        x = message.content
        y = x[12:]

        done = True

        await client.send_message(message.channel, 'https://www.twitch.tv/' + y)



    elif message.content.startswith('repeat'):
        userID = message.author.id
        x = message.content
        y = x[7:]
        await client.send_message(message.channel, "<@%s> said: " % (userID) + y, tts=True)

    elif message.content.startswith('link surrenderat20'):
        await client.send_message(message.channel, 'http://www.surrenderat20.net/')

    elif message.content.startswith('link op.gg'):
        await client.send_message(message.channel, 'http://na.op.gg/l=en_US')

    elif message.content.startswith('tea') or message.content.startswith('sips tea'):
        await client.send_message(message.channel,
                               'https://cdn.discordapp.com/attachments/394540733765255182/401601777817878530/image.jpg')

    elif message.content.startswith('wtf') or message.content.startswith('WTF'):
        await client.send_message(message.channel, 'https://cdn.discordapp.com/emojis/394669496138334209.png')

    elif message.content.startswith('wtf') or message.content.startswith('ugh'):
        await client.send_message(message.channel, 'https://cdn.discordapp.com/emojis/394978715936751626.png')

    elif message.content.startswith('lol') or message.content.startswith('LOL') or message.content.startswith(
            'lmao') \
            or message.content.startswith('LMAO'):
        await client.send_message(message.channel, "https://cdn.discordapp.com/emojis/395045718143926272.png")


    elif message.content.startswith('search lyrics'):

        x = message.content

        y = x[14:]

        artist, song = y.split(",")

        lyrics = PyLyrics.getLyrics(artist, song)

        half = int(len(lyrics) / 2)

        lyrics1 = lyrics[0:half]

        lyrics2 = lyrics[half:]

        await client.send_message(message.channel, lyrics1)
        await client.send_message(message.channel, lyrics2)




    elif message.content.startswith('weather in'):

        x = message.content

        y = x[11:]

        weather = Weather()
        location = weather.lookup_by_location(y)

        forecasts = location.forecast()

        await client.send_message(message.channel, "Weather in: " + y)

        for forecast in forecasts:
            await client.send_message(message.channel, "\nDate: " + forecast.date())
            await client.send_message(message.channel, "Condition: " + forecast.text())
            await client.send_message(message.channel, "High: " + forecast.high())
            await client.send_message(message.channel, "Low: " + forecast.low())
            break;

    elif message.content.startswith('forecast for'):

        x = message.content

        y = x[13:]

        weather = Weather()
        location = weather.lookup_by_location(y)

        forecasts = location.forecast()

        await client.send_message(message.channel, "Forecast for " + y)

        for forecast in forecasts[0:3]:
            await client.send_message(message.channel, "\nDate: " + forecast.date())
            await client.send_message(message.channel, "Condition: " + forecast.text())
            await client.send_message(message.channel, "High: " + forecast.high())
            await client.send_message(message.channel, "Low: " + forecast.low())
            await client.send_message(message.channel, "-------------------------- ")


    elif message.content.startswith('coin flip'):
        x = randint(1, 2)

        respond = ""

        if x == 1:
            respond = "heads"
        elif x == 2:
            respond = "tails"
        await client.send_message(message.channel, respond)

    elif message.content.startswith('hey bot is') or message.content.startswith('hey bot are') \
            or message.content.startswith('hey bot will') or message.content.startswith('hey bot am') or \
            message.content.startswith('hey bot should'):

        x = randint(1, 10)

        response = ""

        if x == 1:
            response = "Hmm, im not sure"
        elif x == 2:
            response = "Absolutely not"
        elif x == 3:
            response = "Ask again later"
        elif x == 4:
            response = "Most likely"
        elif x == 5:
            response = "Yep, for sure "
        elif x == 6:
            response = "You dont want to know..."
        elif x == 7:
            response = "Outlook not good"
        elif x == 8:
            response = "Hell nah"
        elif x == 9:
            response = "i think so"
        elif x == 10:
            response = "Thats a dumb question"

        await client.send_message(message.channel, response)

    elif message.content.startswith('hey bot'):
        await client.send_message(message.channel, 'cant answer that')

    elif message.content.startswith('help'):
        await client.send_message(message.channel, help)


client.run('NDAxNTY5MzgwNjk1MTQ2NDk2.DTsGKg.Y6lrI7wY1ySVvwe4Sh84oKNpUa8')







