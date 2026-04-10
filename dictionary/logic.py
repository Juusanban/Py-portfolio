from storage import save_cards, load_cards

cards = load_cards()


def add_card(word, reading, meaning):

    if reading is None:
        cards.append([word, meaning])
    else:
        cards.append([word, reading, meaning])

    save_cards(cards)


def update_card(index, word, reading, meaning):

    if reading is None:
        cards[index] = [word, meaning]
    else:
        cards[index] = [word, reading, meaning]

    save_cards(cards)


def delete_card(index):

    cards.pop(index)
    save_cards(cards)


def get_cards():
    return cards


def search_cards(query):

    q = query.lower()
    result = []

    for c in cards:
        if any(q in str(field).lower() for field in c):
            result.append(c)

    return result


# SORT by DATA
def sort_cards():

    cards.reverse()
    save_cards(cards)