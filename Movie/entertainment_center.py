import fresh_tomatoes
import media

shrek = media.Movie("Shrek",
                    "An ogre's swamp gets invaded by fairy tale creatures",
                    "https://ia.media-imdb.com/images/M/MV5BOGZhM2FhNTItODAzNi00YjA0LWEyN2UtNjJlYWQzYzU1MDg5L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,671,1000_AL_.jpg",
                    "https://www.youtube.com/watch?v=W37DlG1i61s")
#print(shrek.storyline)

shrek_2 = media.Movie("Shrek 2", "An ogre returns from his honeymoon with his rich wife",
                      "https://ia.media-imdb.com/images/M/MV5BMDJhMGRjN2QtNDUxYy00NGM3LThjNGQtMmZiZTRhNjM4YzUxL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_SX677_AL_.jpg",
                      "https://www.youtube.com/watch?v=V6X5ti4YlG8")
#print(shrek_2.storyline)
#shrek_2.show_trailer()

shrek_3 = media.Movie("Shrek the Third", "An ogre doesn't want to be king and enlists his cat and donkey for help",
                      "https://ia.media-imdb.com/images/M/MV5BOTgyMjc3ODk2MV5BMl5BanBnXkFtZTcwMjY0MjEzMw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                      "https://www.youtube.com/watch?v=InR865IDDjU")

shrek_4 = media.Movie("Shrek Forever After", "A unhappily domesticated ogre gets stuck in an alternate reality",
                      "https://upload.wikimedia.org/wikipedia/en/7/75/Shrek_forever_after_ver8.jpg",
                      "https://www.youtube.com/watch?v=u7__TG7swg0")

shrek_musical = media.Movie("Shrek The Musical", "A singsong version of the ogre's life events",
                            "https://upload.wikimedia.org/wikipedia/en/4/46/Shrekcovernew.jpg",
                            "https://www.youtube.com/watch?v=UPSPj3kx3Cc")

shrek_xmas = media.Movie("Shrek the Halls", "An ogre celebrates Christmas at the urging of his donkey friend",
                         "https://upload.wikimedia.org/wikipedia/en/b/b7/Shrek_the_Halls_poster.jpg",
                         "https://www.youtube.com/watch?v=KpytAHTmKXI")

shrek_halloween = media.Movie("Scared Shrekless", "An ogre and his friends tell scary stories",
                              "https://upload.wikimedia.org/wikipedia/en/0/0f/Scared_Shrekless_DVD_cover.jpg",
                              "https://www.youtube.com/watch?v=ZIbHKKXz-BE")

movies = [shrek, shrek_2, shrek_3, shrek_4, shrek_musical, shrek_xmas, shrek_halloween]                        
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
