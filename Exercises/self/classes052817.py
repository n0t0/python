class Music():

    instrument = 'Guitar'
    style = 'Rock'

    def __init__(self, artist, album, song):
        self.artist = artist
        self.album = album
        self.song = song

    def playMusic(self):
        print ('ARTIST:\t %s\n ALBUM:\t %s\n SONG:\t %s' %
               (self.artist, self.album, self.song))


player_1 = Music('Scorpions', 'Savage Amusement', 'Every Minute Every Day')
player_2 = Music('Scorpions', "Best of Rockers 'N' Ballads",
                 'Still Loving You')


player_1.playMusic()
player_2.playMusic()

print (player_1.instrument)
print (player_2.style)
