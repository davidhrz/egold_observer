import image_search
import random
import utils

advice = []
advice_queries = []
quotes = []
quote_authors = []

def refresh_data():
    utils.fill_list_from_file(utils.advice_file, advice)
    utils.fill_list_from_file(utils.advice_queries_file, advice_queries)
    utils.fill_list_from_file(utils.quotes_file, quotes)
    utils.fill_list_from_file(utils.quotes_authors_file, quote_authors)

# Picks a random element from a list, deletes it from the list. Refills list if
# no elements are left in the list.
# Returns the random element.
def pick_from_list(list, file):
    choice = random.choice(list)
    list.remove(choice)
    if len(list) == 0:
        utils.fill_list_from_file(file, list)
    return choice

# Returns some advice along with a tuple of an image and its extension (BytesIO, str)
def get_advice():
    advice_choice = pick_from_list(advice, utils.advice_file)
    advice_query = pick_from_list(advice_queries, utils.advice_queries_file)
    return advice_choice, image_search.get_image_raw(advice_query)

# Returns a random quote and a random author, along with a tuple of
# an image of the author and its extension (BytesIO, str)
def get_quote():
    quote = pick_from_list(quotes, utils.quotes_file)
    quote_author = pick_from_list(quote_authors, utils.quote_authors_file)
    return quote, quote_author, image_search.get_image_raw(quote_author)
