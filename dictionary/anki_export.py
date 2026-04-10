import genanki


def export_anki(data):

    english_model = genanki.Model(
        1607392319,
        'English Model',
        fields=[
            {'name': 'Word'},
            {'name': 'Meaning'}
        ],
        templates=[
            {
                'name': 'Card',
                'qfmt': '{{Word}}',
                'afmt': '{{FrontSide}}<hr>{{Meaning}}'
            }
        ]
    )


    japanese_model = genanki.Model(
        1607392320,
        'Japanese Model',
        fields=[
            {'name': 'Word'},
            {'name': 'Reading'},
            {'name': 'Meaning'}
        ],
        templates=[
            {
                'name': 'Card',
                'qfmt': '{{Word}}',
                'afmt': '{{FrontSide}}<hr>{{Reading}}<br>{{Meaning}}'
            }
        ]
    )


    english_deck = genanki.Deck(
        2059400110,
        'English Deck'
    )


    japanese_deck = genanki.Deck(
        2059400111,
        'Japanese Deck'
    )


    for row in data:

        if len(row) == 2:

            note = genanki.Note(
                model=english_model,
                fields=row
            )

            english_deck.add_note(note)

        else:

            note = genanki.Note(
                model=japanese_model,
                fields=row
            )

            japanese_deck.add_note(note)


    genanki.Package([english_deck, japanese_deck]).write_to_file("deck.apkg")