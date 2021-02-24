with open("token/discord.txt") as file:
    discord_token = file.read().strip()

with open("token/google_cx.txt") as file:
    google_cx = file.read().strip()

with open("token/google_dev_key.txt") as file:
    google_dev_key = file.read().strip()

advice_queries_file = "data/advice_queries.txt"
quotes_file = "data/quotes.txt"
quote_authors_file = "data/quote_authors.txt"
advice_file = "data/advice.txt"

def fill_list_from_file(file, list):
    list.clear()
    with open(file) as f:
        for line in f:
            list.append(line.strip())
