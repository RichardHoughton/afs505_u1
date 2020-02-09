class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

wonder = Song(["This is very interesting",
                "May be useful later"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

wonder.sing_me_a_song()

curiosity = Song(wonder.lyrics)
curiosity.sing_me_a_song()
