from random import choice


filename = "quotes.txt"


def get_quotes_authors(filename):
    with open(filename, "r", encoding="utf-8") as f:
        quotes = f.readlines()
        quotes_list = []
        for element in quotes:
            quote, author = element.split("|")
            dquotes = {"quote": quote, "author": author.strip("\n")}
            quotes_list.append(dquotes)
    return quotes_list


def get_random_quote(filename):
    return choice(get_quotes_authors(filename))

