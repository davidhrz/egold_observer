import image_search
import random

advice = [
    'Hmmm... this looks bad. Very bad! You should SELL NOW!',
    'Please SELL NOW all of your EGOLD!!',
    '$EGLD is not a stable cryptocurrency, reports Frankfurt Stock Exchange. It is recommended to sell all of your Egold. #Crypto',
    'According to the latest statistical data analysis, $EGLD is bound to crash down to -150 USD in coming minutes. All owners are recommended to CASH OUT! #Crypto #Egold',
    'AAAAAAAAAARGHH CASH OUT cash out SELL SELL SELL NOW!! $EGLD',
    'EGOLD IS GOING DOWN!!!! SELL NOW! In two hours, EGLD WILL BE DOWN 300%!!',
    'Latest reports show that $EGLD is declining fast. Sell now.',
    '$EGLD is a DISASTER!!! I lost all of my belongings!',
    'While it looked promising at the beginning, it turns out $EGLD was nothing but an enormous scam. SELL while you still can!',
    '@elonmusk on Twitter: I hate black people',
    '@BillGates on Twitter: Turns out buying 1 billion USD worth of $EGLD was a mistake. #Cryptocurrencies #Mistakes #Scam'
]

queries_advice = [
    'downward chart',
    'statistics going down',
    'currency going down',
    'currency decline',
    'cryptocurrency decline',
    'chart going down',
    'man holding head',
    'woman holding head',
    'desperate woman',
    'desperate man stock picture',
    'despair stock picture',
    'suicide stock picture',
    'elon musk',
    'bill gates'
]

quotes = [
    'I don\'t trust Egold, and neither should you.',
    'I have sold all of my Egold.',
    'You should definitely do what I did and sell all of your EGOLD!',
    'Life is much better without Egold.',
    'Without EGOLD, I feel free.',
    'Back when I used to have Egold, my life was meaningless. I am so much happier now!',
    'FUCK Egold',
    'Sell all of your Egold.',
    'Do not get Egold.',
    'PLEASE don\'t make the same mistake I did. Do NOT buy EGOLD. If you have any, SELL IT NOW!!'
]

queries_quotes = [
    'Geroge Clooney',
    'Mahatma Gandhi',
    'Michael Jackson',
    'Joël Courtois',
    'Brad Pitt',
    'Angelina Jolie',
    'Joseph Stalin',
    'Karl Marx',
    'Benjamin Franklin',
    'Jean Dujardin',
    'Tom Cruise',
    'Leonardo DiCaprio',
    'Paul Walker',
    'Bill Gates',
    'Steve Jobs',
    'Elon Musk',
    'Theodore Roosevelt',
    'Vladimir Putin',
    'Donald Trump'
]

def get_advice():
    return random.choice(advice), image_search.get_image_raw(random.choice(queries_advice))


def get_quote():
    quote_author = random.choice(queries_quotes)
    return random.choice(quotes), quote_author, image_search.get_image_raw(quote_author)
