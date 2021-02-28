# Egold Observer

The one and only Egold observer bot for Discord.

## Features

The Observer is here to help you get richer. To trigger the bot, either mention him or use the `obs$` prefix, and use one of the following commands:

### Advice

Get some advice from Egold Observer! Trigger the Observer with no particular command and he will give you insightful advice for your investment in Egold, and predictions based on precise calculations from the International Egold Observing Agency.

### Quote

Feeling inspirational? Trigger the Observer with `quote`  and he will answer with a motivating quote from world-renowned Egold investors.

### Graph

Sometimes, you need to see the stats to understand them. Trigger the observer with `graph` and a graph of the value of one Egold over the last 24 hours will be displayed.

## How to use the bot

### Tokens

The `token/` directory contains 3 text files:

- discord.txt: contains your bot's discord token.
- google_cx.txt: contains your Google custom search engine CX.
- google_dev_key.txt: contains your Google dev API.

### Data

The `data/ `directory contains 4 text files:

- advice_queries.txt: contains search queries to get images for the Advice command.

- advice.txt: contains the pieces of advice that will be given in the Advice command.

- quote_authors.txt: contains the authors that will be associated with a quote in the Quote command.

- quotes.txt: contains the quotes that will be given in the Quote command.

Each of these files takes one element per line.

### Running the bot

Go to the `src/` directory and run the `bot.py` script. You can load new data into the bot by using the `dev_refresh` command.

## Requirements

- [discord.py](https://github.com/Rapptz/discord.py)
- matplotlib
- [Google Images Search](https://pypi.org/project/Google-Images-Search/)

