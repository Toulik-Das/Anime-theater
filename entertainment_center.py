import media
import fresh_tomatoes


def run():
    """ Generate and open the movies listing html page """
    fresh_tomatoes.open_movies_page(
            get_movie_list(),
            "Top Anime Movies")


def get_movie_list():
    """ Retrieve a list of movies """
    return [media.Movie(
            "Your Name",
            "https://upload.wikimedia.org/wikipedia/en/0/0b/Your_Name_poster.png",
            "https://www.youtube.com/watch?v=xU47nhruN-Q"),
            media.Movie(
                "My Neighbor Totoro",
                "https://upload.wikimedia.org/wikipedia/en/0/02/My_Neighbor_Totoro_-_Tonari_no_Totoro_%28Movie_Poster%29.jpg",
                "https://www.youtube.com/watch?v=92a7Hj0ijLs"),
            media.Movie(
                "Spirited Away",
                "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcS6MveoDoJOg9-wMvtHE4ak_-HDZeYS1egb9PwRcf8lhrtcppMc",
                "https://www.youtube.com/watch?v=7cv5p1XNuDw"),
            media.Movie(
                "Kiki's Delivery Service",
                "https://upload.wikimedia.org/wikipedia/en/0/07/Kiki%27s_Delivery_Service_%28Movie%29.jpg",
                "https://www.youtube.com/watch?v=4bG17OYs-GA"),
            media.Movie(
                "Wolf Children",
                "https://upload.wikimedia.org/wikipedia/en/9/9c/%C5%8Ckami_Kodomo_no_Ame_to_Yuki_poster.jpg",
                "https://www.youtube.com/watch?v=8xLji7WsW0w"),
            media.Movie(
                "Ghost in the Shell",
                "https://upload.wikimedia.org/wikipedia/en/c/ca/Ghostintheshellposter.jpg",
                "https://www.youtube.com/watch?v=SvBVDibOrgs")

            media.Movie(
                "When Marnie Was There",
                "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSNjvkqicvyX8WpuKxlGP8hmGa8ZZs5OOYO5XSKla2hny_2gFNP",
                "https://youtu.be/watch?v=GlM33eGzN9o")
            media.Movie(
                "Weathering with You",
                "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcROPn8FcJ8LSRQ3TGGW3kYuETfwj3iBbrPUltyiFuf6fcMX_bFV",
                "https://youtu.be/Q6iK6DjV_iE")
            media.Movie(
                "A Silent Voice",
                "https://www.gstatic.com/tv/thumb/v22vodart/15060746/p15060746_v_v8_ab.jpg",
                "https://youtu.be/nfK6UgLra7g")

            media.Movie(
                "The Garden of Words",
                "https://www.gstatic.com/tv/thumb/v22vodart/10191455/p10191455_v_v8_ab.jpg",
                "https://youtu.be/FMabhvDoolc")]

run()

