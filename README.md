# Discord App

A bot for discord, I began messing with this after looking at a tutorial on youtube, and because I was learning python I decided to make this my first "big" python project. 

Using discord.py I setup a bot that responds based on what the user typed in chat. A simple command for example, such as "coin flip" will return a heads or tails response. I wanted to mess with some APIs so I implemented a feature where the user can look up the weather/forecast in a given city using yahoo's weather api.

By typing "weather in <city name>" or "forecast for <ckty name>" the bot will give either the weather for the day or a 3 day foreacast resepectively.
  The biggest challenge in this was manipulating the String token that the user provides and extract only the name of the city. I did this by cutting the String after the "Weather in"/"forecast for" part and use only the city name part of the string.
  After that I use that city name in the api call to give the forecast for the city, the api uses a for loop to give the forecast for the current day up to 5 days so I looped it once for the current weather, and 3 times to get a 3-day forecast.
  
  Another feature I implemented was the ability to search up song lyrics. Using the lyrics.wikia api I did a similiar thing in terms of string manupulation to get lyrics. The command is "lyrics search <Artist name>,<Song name>" this one was a bit tricker because it required a bit more string maipulation to get the information I needed for the api call. I first cut the string so that it would only contain the "<artist name>,<song name>" part. Then I cut the string from the begginning up to the comma to retrieve the artist name, and from the comma afterwards to get the song name. With that information I was able to use the api to retrieve the lyrics and display it. However I ran into one more issue, discord only allows up to 150 words per message in chat. So I had to cut the token string containing the lyrics into chunks and then display those as individual messages afterwards.
  
  This project was lots of fun and I learned alot about how to manipulate strings in python. Next thing I will try and do is to implement a music player function in voice chat
