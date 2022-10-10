import pytest
from morse import encode, decode, MORSE_TO_LETTER


@pytest.mark.parametrize(
    'source_string, result',
    [
        ('... --- ...', 'SOS'),
        ('.... ..', 'HI'),
        ('-.. --- --.', 'CAT'),
    ],
)
def test_decode(source_string, result):
    assert decode(source_string) == result
