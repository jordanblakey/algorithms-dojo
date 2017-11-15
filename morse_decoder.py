def decodeMorse(morse):
    # ToDo: Accept dots dashes and spaces, return human-readable message
    
    morse_alpha = {
        '.-...': '&',
        '--..--': ',',
        '....-': '4',
        '.....': '5',
        '...---...': 'SOS',
        '-...': 'B',
        '-..-': 'X',
        '.-.': 'R',
        '.--': 'W',
        '..---': '2',
        '.-': 'A',
        '..': 'I',
        '..-.': 'F',
        '.': 'E',
        '.-..': 'L',
        '...': 'S',
        '..-': 'U',
        '..--..': '?',
        '.----': '1',
        '-.-': 'K',
        '-..': 'D',
        '-....': '6',
        '-...-': '=',
        '---': 'O',
        '.--.': 'P',
        '.-.-.-': '.',
        '--': 'M',
        '-.': 'N',
        '....': 'H',
        '.----.': "'",
        '...-': 'V',
        '--...': '7',
        '-.-.-.': ';',
        '-....-': '-',
        '..--.-': '_',
        '-.--.-': ')',
        '-.-.--': '!',
        '--.': 'G',
        '--.-': 'Q',
        '--..': 'Z',
        '-..-.': '/',
        '.-.-.': '+',
        '-.-.': 'C',
        '---...': ':',
        '-.--': 'Y',
        '-': 'T',
        '.--.-.': '@',
        '...-..-': '$',
        '.---': 'J',
        '-----': '0',
        '----.': '9',
        '.-..-.': '"',
        '-.--.': '(',
        '---..': '8',
        '...--': '3'
    }

    morse = morse.strip(' ').split('   ')
    morse = [word.split(' ') for word in morse]
    acc = []
    for word in morse:
        acc.append(''.join([morse_alpha[letter] for letter in word]))
    acc = ' '.join(acc)
    return acc

# Or, more succinctly:
def decodeMorse2(morseCode):
  return ' '.join(''.join(morse_alpha[letter] for letter in word.split(' ')) for word in morseCode.strip.split('   '))
