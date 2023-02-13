def longest_possible(songs: dict, playback: int):
    """
    Very bad
    """
    seconds_for_each_song = []
    title = ""

    if playback <= 150:
        return False

    for n in songs:
        for k,v in n.items():
            if k == "playback":
                seconds_for_each_song.append(int(v.split(':')[0])*60 + int(v.split(':')[1]))

    candidate = max([i for i in seconds_for_each_song if i <= playback])
    return candidate

    for element in songs:
        for k, v in element.items():
            if k == "playback" and int(v.split(':')[0])*60 + int(v.split(':')[1]) == candidate:
                title = element['title']

    return title or False

            
# ALternative Solution
def to_seconds(time):
    minutes, seconds = map(int, time.split(':'))
    return minutes * 60 + seconds


def longest_possible(playback):
    longest_song = 0
    song_title = ''
    for song in songs:
        song_length = to_seconds(song['playback'])
        if longest_song < song_length <= playback:
            longest_song = song_length
            song_title = song['title']
    return song_title or False


songs = [
    {'artist': 'Marillion', 'title': 'Keyleigh', 'playback': '03:36'}, 
    {'artist': 'Pink Floyd', 'title': 'Time', 'playback': '06:48'}, 
    {'artist': 'Rush', 'title': 'YYZ', 'playback': '04:27'}, 
    {'artist': 'Bonobo', 'title': 'Days To Come', 'playback': '03:50'}, 
    {'artist': 'Coldplay', 'title': 'Yellow', 'playback': '04:32'}, 
    {'artist': 'Bloc Party', 'title': 'Like Eating Glass', 'playback': '04:22'}, 
    {'artist': 'The Killers', 'title': 'For Reasons Unknown', 'playback': '03:30'},
    {'artist': 'Arctic Monkeys', 'title': 'Teddy Picker', 'playback': '03:25'}, 
    {'artist': 'Joe Satriani', 'title': 'Surfing With The Alien', 'playback': '04:34'}
    ]

print(longest_possible(songs, 13))