class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics
	def sing_me_a_song(self):
		for i in self.lyrics:
			print(i)
flower_song = Song(["Roses are red","Violets are blue", "I wrote this poem for you."])
print(flower_song.sing_me_a_song())	