import json
import logging
import os

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "movies.json")


class Movie:
    def __init__(self, title: str):
        """Capitalize the first letters of the movie and add it to the list of movies viewed in the
        save file (data/movies.json)

        Args:
            title(str): New film viewed
        """
        self.title = title.title()

    def __str__(self) -> str:
        """ Return the new film viewed when the class is called

        Returns:
            title (str): New film viewed
        """
        return self.title

    @staticmethod
    def _get_movies() -> list[str]:
        """Read the save file of the films viewed (data/movies.json)

        Return :
            (list[str]): list of films viewed of String
        """
        with open(DATA_FILE, "r") as f:
            return json.load(f)

    @staticmethod
    def _write_movies(movies):
        """Write the new movie in the save file (data/movies.json)

        Args:
            movies (list): Return String list of viewed films
        """
        with open(DATA_FILE, "w") as f:
            json.dump(movies, f, indent=4)

    def add_to_movies(self) -> bool:
        """Add the new film in the save file of viewed films (data/movies.json)

        Returns:
            (bool): Return True if the film is added and False if it's already in the save file
        """
        movies = self._get_movies()

        if self.title not in movies:
            movies.append(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f" Le film {self.title} est deja dans la liste")
            return False

    def remove_from_movies(self) -> bool:
        """Remove the new film in the save file of viewed films (data/movies.json)

        Returns:
            (bool): Return True if the film is removed and False if it isn't in the save file
        """

        movies = self._get_movies()

        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f" Le film {self.title} n'est pas dans la liste")
            return False

    def get_movies(self):
        movies = self._get_movies()


def get_movies() -> list[Movie]:
    """Read the save file of the films viewed (data/movies.json)

    Return :
        (list[Movie]) : Return Movie instance list of viewed films
    """
    with open(DATA_FILE, "r") as f:
        movies_title = json.load(f)
    movies = [Movie(movie_title) for movie_title in movies_title]
    return movies


if __name__ == "__main__":
    Movie("harry potter").add_to_movies()
    Movie("star wars").add_to_movies()
    Movie("gladiator").add_to_movies()
    Movie("seigneur des anneaux").add_to_movies()
    Movie("potter").add_to_movies()