import re


def clean_text(text):

    text = text.lower()

    text = re.sub(
        r'https?://\S+',
        ' URL ',
        text
    )

    text = re.sub(
        r'\S+@\S+',
        ' EMAIL ',
        text
    )

    text = re.sub(
        r'\d+',
        ' NUMBER ',
        text
    )

    text = re.sub(
        r'\s+',
        ' ',
        text
    )

    return text.strip()