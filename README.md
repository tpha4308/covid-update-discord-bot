# Covid Update Discord Bot

## About
Around the end of 2021, in Australia, the number of COVID-19 cases spiked up a lot, reaching 50,000 thousand cases almost daily. At the time, I wished to know the number of new cases every day without having to go on Twitter and being distracted by everything else. 

### Goal
Every day, I want to get a notification of the daily number that was announced on Health Department twitter accounts, without having to actually go on Twitter. 

### Plan
I want to create a discord bot that keeps track of the tweets from a certain list of users (e.g. NSWHealth, SAHealth, ACTHealth, etc.), and if the tweet is the daily update, it will post the tweet URL onto the discord channel. And so the project was split into 2 parts:  
1. Access to Twitter API to get the real-time update on tweets. 
2. Create a Discord bot that send tweet updates and host it. 

Please see the file [Covid_Update_Discord_Bot.pdf](https://github.com/tpha4308/covid-update-discord-bot/blob/main/Covid_Update_Discord_Bot.pdf) for full details of implementation.

## Workflow 
1. Retrieve user_id(s) of the provided username(s) and save into a JSON file. (`setup.py`)
2. Create a discord bot that runs a background task loop. (`main.py`)
3. Retrieve the most recent tweets that have been posted by username(s) within the last specified minute interval. (`get_most_recent_tweets.py`)
4. Filter the tweets so that only the ones containing the keywords will be kept. (`get_most_recent_tweets.py`)
5. Post the tweet url onto the discord channel. (`main.py`)
6. Host the bot. (`keep_alive.py`)

## Example
<div align="center">
  <a href="https://www.youtube.com/watch?v=EjF4kaP34y8"><img src="https://img.youtube.com/vi/EjF4kaP34y8/0.jpg" alt="IMAGE ALT TEXT"></a>
</div>
