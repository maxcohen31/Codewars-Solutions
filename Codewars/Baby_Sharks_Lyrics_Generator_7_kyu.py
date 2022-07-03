def baby_shark_lyrics():
    lyrics = ''
    words = ['Baby shark', 'Mommy shark', 'Daddy shark', 'Grandma shark', 'Grandpa shark', "Let's go hunt"]
    s = ' doo'
    for w in words:
        lyrics += (f"{w}," + f"{s*6}\n") * 3 + w +'!' + '\n' 
    return lyrics + 'Run away,…'

print(baby_shark_lyrics())