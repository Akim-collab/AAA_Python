from morse import decode, LETTER_TO_MORSE


def encode(message: str) -> str:
    """
    Кодирует строку в соответсвии с таблицей азбуки Морзе

    >>> encode('... --- ...')
    'SOS'
    >>> encode('.- --- ...')
    'SOS'
    """
    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)
