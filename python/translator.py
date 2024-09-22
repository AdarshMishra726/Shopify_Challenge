# Dictionary mapping English letters and numbers to Braille
english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    '#': '.O.OOO',  # Braille number prefix
    '^': '.....O',  # Braille capital letter prefix
}

# Reverse mapping from Braille to English
braille_to_english = {v: k for k, v in english_to_braille.items()}

def is_braille(input_str):
    """Detect if input is Braille based on 'O' and '.' format."""
    return all(c in 'O.' for c in input_str) and len(input_str) % 6 == 0
def translate_to_english(braille):
    """Translate Braille to English, handling capitalization and numbers."""
    result = []
    is_capital = False
    is_number = False
    
    for i in range(0, len(braille), 6):
        braille_char = braille[i:i+6]
        if braille_char == '......':
            result.append(' ')  # space
            is_capital = False
            is_number = False
        elif braille_char == '.....O':
            is_capital = True
        elif braille_char == '.O.OOO':
            is_number = True
        else:
            char = braille_to_english.get(braille_char, '')
            if is_number:
                result.append(char)
            else:
                result.append(char.upper() if is_capital else char)
            is_capital = False
            is_number = False
    return ''.join(result)
def translate_to_braille(text):
    """Translate English to Braille, handling capitalization and numbers."""
    result = []
    is_number = False
    
    for char in text:
        if char.isupper():
            result.append(english_to_braille['^'])  # Capital sign
            char = char.lower()
        if char.isdigit():
            if not is_number:
                result.append(english_to_braille['#'])  # Number sign
                is_number = True
        elif char == ' ':
            is_number = False
        
        result.append(english_to_braille[char.lower()])
    
    return ''.join(result)
def main(input_str):
    if is_braille(input_str):
        # Translate Braille to English
        print(translate_to_english(input_str))
    else:
        # Translate English to Braille
        print(translate_to_braille(input_str))

# Example command-line usage
if _name_ == "_main_":
    import sys
    input_str = sys.argv[1] if len(sys.argv) > 1 else ""
    main(input_str)
