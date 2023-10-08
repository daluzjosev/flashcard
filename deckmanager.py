import uuid
import sqlite3
import os


class DeckManager:
    # Implement methods to create, manage, and retrieve decks of cards
    def __init__(self):
        self.decks = self.retrieve_deck()

    def new_deck(self, title):
        db_path = os.path.join("instance", "CardDecks.db")

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute(
            f"""
            INSERT INTO decks VALUES
                       ({uuid.uuid4()},{title})
        """
        )
        conn.commit()

    def retrieve_decks(self):
        db_path = os.path.join("instance", "CardDecks.db")

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Fetch deck titles from the database (assuming title is in the second column)
        cursor.execute("SELECT name FROM decks")
        deck_titles = [row[0] for row in cursor.fetchall()]

        # Close the database connection
        conn.close()
        return deck_titles

    def select_deck(title):
        pass


class Card:
    def __init__(self, front, back):
        self.front = front
        self.back = back

    def add_card():
        pass


db_path = os.path.join("instance", "CardDecks.db")
