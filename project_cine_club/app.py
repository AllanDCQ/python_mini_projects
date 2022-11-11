from PySide2 import QtWidgets, QtCore
import movie as m


class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cine Club")

        # Initialize Layout
        self.layout = None  # Layout of the application

        # Initialize widgets
        self.write_film = None  # Widget of the line edit
        self.add_film = None  # Widget of the push button for adding films
        self.list_movies = None  # Widget of the viewed films list
        self.delete_film = None  # Widget of the push button for deleting films

        self.setup_ui()
        self.populate_movies()
        self.setup_connections()

    def setup_ui(self):
        """
        Create the layout and setup all the widgets
        """

        # Create layout
        self.layout = QtWidgets.QVBoxLayout(self)

        # Create widgets
        self.write_film = QtWidgets.QLineEdit("")
        self.add_film = QtWidgets.QPushButton("Ajouter film")
        self.list_movies = QtWidgets.QListWidget()
        self.list_movies.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)  # select serval films
        self.delete_film = QtWidgets.QPushButton("Supprimer le(s) film(s)")

        # Add widgets
        self.layout.addWidget(self.write_film)
        self.layout.addWidget(self.add_film)
        self.layout.addWidget(self.list_movies)
        self.layout.addWidget(self.delete_film)

    def populate_movies(self):
        """
        Add to the list_movies widget the list of film viewed in the save file (data/movies.json)
        """

        # Clear the widget and read the save file
        self.list_movies.clear()
        movies = m.get_movies()

        # Add movies in the list widget
        for movie in movies:
            list_widget_item = QtWidgets.QListWidgetItem(movie.title)
            list_widget_item.setData(QtCore.Qt.UserRole, movie)
            self.list_movies.addItem(list_widget_item)

    def add_movie(self):
        """
        Add in the list viewed film the film write in the line edit widget (write_film).
        Color the border of the line edit widget in red if the film is already in the save film
        """

        # Read the line edit widget
        film = self.write_film.text()

        # Create a Movie and add in the save file (data/movies.json)
        movie = m.Movie(film)

        if movie.add_to_movies():
            self.populate_movies()
            # Color the border in black of the line edit widget
            self.write_film.setStyleSheet("""border: 1px solid #000000;""")
        else:
            # Color the border in red of the line edit widget
            self.write_film.setStyleSheet("""border: 1px solid #bf372b;""")

        # Actualize the list of viewed film widget
        self.write_film.setText("")

    def remove_movie(self):
        """
        Remove in the list viewed film the film selected (list_movies).
        """

        # Create a data
        movies = m.get_movies()
        for movie in movies:
            list_item = QtWidgets.QListWidgetItem(movie.title)
            list_item.setData(QtCore.Qt.UserRole, movie)

        # Remove a selected films
        for selected_movie in self.list_movies.selectedItems():
            movie = selected_movie.data(QtCore.Qt.UserRole)
            movie.remove_from_movies()

        # Actualize the list of viewed film widget
        self.populate_movies()
            # or self.list_movies.takeItem(self.list_movies.row(selected_movie))

    def setup_connections(self):
        self.add_film.clicked.connect(self.add_movie)
        self.delete_film.clicked.connect(self.remove_movie)


app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()
