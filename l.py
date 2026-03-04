class playlist:
    def __init__(self,name):
        self.name=name
        self.songs=[]
    def add__song(self,song):
        self.songs.append(song)
        print(f"added :{song}")
    def remove_song(self,song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"removed :{song}")
    def show_sonf(self):
        print(f"playlist:{self.name}")
        for song in self.songs:
            print(f"{song}")

myplay=playlist("favourite")
myplay.add__song("rand ka tilla")
myplay.add__song("fefjkfd")
myplay.show_sonf()
    