# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import DeclarativeBase, relationship
# from sqlalchemy import Integer, String, ForeignKey
# from sqlalchemy.orm import Mapped, mapped_column
# import requests


# class Base(DeclarativeBase):
#     pass


# db = SQLAlchemy(model_class=Base)


# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///CardDecks.db"
# db.init_app(app)


# class Decks(db.Model):
#     __tablename__ = "decks"

#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
#     cards = relationship("Card", back_populates="deck")


# class Cards(db.Model):
#     __tablename__ = "cards"

#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     front: Mapped[str] = mapped_column(String, unique=True, nullable=False)
#     back: Mapped[str] = mapped_column(String, unique=True, nullable=False)

#     deck_id = mapped_column(Integer, ForeignKey("decks.id"))
#     deck = relationship("Deck", back_populates="cards")


# with app.app_context():
#     db.create_all()
