def decodeMorse(morse_code):
    morse_code = morse_code.split(' ')
    translation = ''.join(MORSE_CODE[k] if k in MORSE_CODE else ' ' for k in morse_code)
    return translation.replace('  ', ' ').strip()



mess = '.... . -.--   .--- ..- -.. .'
print(decodeMorse(mess))