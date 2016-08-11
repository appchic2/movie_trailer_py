# entertainment_center.py
# These import files HAVE to be in the same directory as the other files
import fresh_tomatoes
import media


toy_story = media.Movie("Toy Story",
                        " A story of his boy and his toys come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# THis stuff shows up in the python shell window
#toy_story.show_poster_image()  
#toy_story.show_movie_title()
#toy_story.show_storyline()
#toy_story.show_trailer()

avatar = media.Movie("Avatar",
                     " A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=2v-svozQvc4")

school_of_rock = media.Movie("School of Rock",
                     " Using rock music to learn",
                     "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                     "https://www.youtube.com/watch?v=3PsUJFEBC74")
ratatouille = media.Movie("Ratatouille",
                     " A rat is a chef in Paris",
                     "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                     "https://www.youtube.com/watch?v=c3sBBRxDAqk")
midnight_in_paris = media.Movie("Midnight in Paris",
                     " Going back in time to meet authors",
                     "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                     "https://www.youtube.com/watch?v=5nOF93SzX6s")
hunger_games = media.Movie("Hunger Games",
                     " A really real reality show",
                     "https://upload.wikimedia.org/wikipedia/en/4/4b/Hunger_Games_Film_Poster.jpg",
                     "https://www.youtube.com/watch?v=PbA63a7H0bo")

#print(media.Movie.VALID_RATINGS)  #prints in python shell window

# This prints out the comment in the """...""" at the top of the class definition
print(media.Movie.__doc__)

#create movies array
movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)








