# Sample word lists for crossword generation

# Common 3-letter words
THREE_LETTER_WORDS = [
    'ACE', 'AGE', 'AID', 'AIM', 'AIR', 'ALL', 'AND', 'ANT', 'ANY', 'APE',
    'ARC', 'ARE', 'ARK', 'ARM', 'ART', 'ASK', 'ATE', 'BAD', 'BAG', 'BAR',
    'BAT', 'BAY', 'BED', 'BEE', 'BET', 'BIG', 'BIT', 'BOX', 'BOY', 'BUG',
    'BUS', 'BUT', 'BUY', 'CAN', 'CAP', 'CAR', 'CAT', 'COW', 'CRY', 'CUP',
    'CUT', 'DAD', 'DAY', 'DID', 'DIE', 'DIG', 'DOG', 'EAR', 'EAT', 'EGG',
    'END', 'EYE', 'FAR', 'FAT', 'FEW', 'FIG', 'FIT', 'FIX', 'FLY', 'FOR',
    'FOX', 'FUN', 'GET', 'GOT', 'GUN', 'GUY', 'HAD', 'HAM', 'HAS', 'HAT',
    'HER', 'HID', 'HIM', 'HIS', 'HIT', 'HOT', 'HOW', 'HUG', 'ICE', 'ILL',
    'INK', 'JAM', 'JAR', 'JOB', 'JOY', 'KEY', 'KID', 'LAP', 'LAW', 'LAY',
    'LEG', 'LET', 'LID', 'LIE', 'LOG', 'LOT', 'LOW', 'MAD', 'MAN', 'MAP'
]

# Common 4-letter words
FOUR_LETTER_WORDS = [
    'ABLE', 'ALSO', 'AREA', 'ARMY', 'AWAY', 'BABY', 'BACK', 'BALL', 'BAND',
    'BANK', 'BASE', 'BEAR', 'BEAT', 'BEEN', 'BELL', 'BEST', 'BILL', 'BIRD',
    'BLOW', 'BLUE', 'BOAT', 'BODY', 'BONE', 'BOOK', 'BORN', 'BOTH', 'BOYS',
    'BUSY', 'CAKE', 'CALL', 'CAME', 'CAMP', 'CARD', 'CARE', 'CARS', 'CASE',
    'CITY', 'CLUB', 'COAL', 'COAT', 'CODE', 'COLD', 'COME', 'COOK', 'COOL',
    'COPY', 'CORN', 'COST', 'DARK', 'DATA', 'DATE', 'DAYS', 'DEAD', 'DEAL',
    'DEAR', 'DEEP', 'DESK', 'DOES', 'DONE', 'DOOR', 'DOWN', 'DRAW', 'DREW',
    'DROP', 'DRUM', 'DUCK', 'DUTY', 'EACH', 'EARL', 'EARN', 'EAST', 'EASY',
    'EDGE', 'ELSE', 'EVEN', 'EVER', 'EYES', 'FACE', 'FACT', 'FAIL', 'FAIR',
    'FALL', 'FARM', 'FAST', 'FEAR', 'FEEL', 'FEET', 'FELL', 'FELT', 'FILE'
]

# Common 5-letter words
FIVE_LETTER_WORDS = [
    'ABOUT', 'ABOVE', 'ABUSE', 'ADMIT', 'ADOPT', 'ADULT', 'AFTER', 'AGAIN',
    'AGENT', 'AGREE', 'AHEAD', 'ALARM', 'ALBUM', 'ALERT', 'ALIEN', 'ALIGN',
    'ALIKE', 'ALIVE', 'ALLOW', 'ALONE', 'ALONG', 'ALTER', 'ANGEL', 'ANGER',
    'ANGLE', 'ANGRY', 'APART', 'APPLE', 'APPLY', 'ARENA', 'ARGUE', 'ARISE',
    'ARRAY', 'ASIDE', 'ASSET', 'AVOID', 'AWAKE', 'AWARD', 'AWARE', 'BADLY',
    'BAKER', 'BALLS', 'BASIC', 'BEACH', 'BEGAN', 'BEGIN', 'BEING', 'BELLY',
    'BELOW', 'BENCH', 'BILLY', 'BIRTH', 'BLACK', 'BLAME', 'BLANK', 'BLIND',
    'BLOCK', 'BLOOD', 'BLOWN', 'BLUES', 'BOARD', 'BOOST', 'BOOTH', 'BOUND',
    'BRAIN', 'BRAND', 'BRASS', 'BRAVE', 'BREAD', 'BREAK', 'BREED', 'BRIEF',
    'BRING', 'BROAD', 'BROKE', 'BROWN', 'BUILD', 'BUILT', 'BUYER', 'CABLE'
]

# Themed word lists
ANIMALS = [
    'CAT', 'DOG', 'BIRD', 'FISH', 'BEAR', 'LION', 'WOLF', 'DEER', 'FROG',
    'DUCK', 'GOAT', 'HORSE', 'MOUSE', 'RABBIT', 'SNAKE', 'TIGER', 'ZEBRA'
]

COLORS = [
    'RED', 'BLUE', 'GREEN', 'BLACK', 'WHITE', 'BROWN', 'PINK', 'GRAY',
    'ORANGE', 'PURPLE', 'YELLOW', 'SILVER', 'GOLDEN'
]

FOOD = [
    'APPLE', 'BREAD', 'CAKE', 'CHEESE', 'FISH', 'FRUIT', 'GRAPE', 'HONEY',
    'JUICE', 'LEMON', 'MEAT', 'MILK', 'PASTA', 'PIZZA', 'RICE', 'SALAD',
    'SOUP', 'SUGAR', 'TOAST', 'WATER'
]

TECHNOLOGY = [
    'PHONE', 'RADIO', 'MUSIC', 'VIDEO', 'CABLE', 'MOUSE', 'SCREEN', 'POWER',
    'BYTES', 'CLOUD', 'EMAIL', 'FIBER', 'GAMES', 'IMAGE', 'LASER', 'PIXEL'
]

# Combined comprehensive word list
ALL_WORDS = list(set(
    THREE_LETTER_WORDS + FOUR_LETTER_WORDS + FIVE_LETTER_WORDS +
    ANIMALS + COLORS + FOOD + TECHNOLOGY
))

# Sort by length for easier usage
ALL_WORDS.sort(key=lambda x: (len(x), x))

def get_words_by_length(length: int) -> list:
    """Get all words of a specific length."""
    return [word for word in ALL_WORDS if len(word) == length]

def get_themed_words(theme: str) -> list:
    """Get words from a specific theme."""
    themes = {
        'animals': ANIMALS,
        'colors': COLORS,
        'food': FOOD,
        'technology': TECHNOLOGY
    }
    return themes.get(theme.lower(), [])

def get_random_word_list(count: int = 50, min_length: int = 3, max_length: int = 5) -> list:
    """Get a random selection of words within specified length constraints."""
    import random

    filtered_words = [
        word for word in ALL_WORDS
        if min_length <= len(word) <= max_length
    ]

    if count >= len(filtered_words):
        return filtered_words

    return random.sample(filtered_words, count)
