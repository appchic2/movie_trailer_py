#Class Movie File
#Good idea to keep class file separate
import webbrowser

class Movie():
    """ This class provides a way to store movie related information """
    #This is a class variable and it is a CONSTANT so it should be ALL CAPS
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    # The double __ is a way for python to tell us that
    # the name "init" is reserved in python and it is a special function
    # "self" is the instance being created; 

    # define the constructor to create space in memory
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        # these are instance variables (title, etc)
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Don't need any of this - I added it.
    def show_movie_title(self):
        print(self.title)

    def show_storyline(self):
        print(self.storyline)

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def show_poster_image(self):
        webbrowser.open(self.poster_image_url)

