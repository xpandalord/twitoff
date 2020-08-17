"""SQLAlchemy models and utility functions for TwitOff."""
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class User(DB.Model):
    """Twitter users corresponding to Tweets."""
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)

    def __repr__(self):
        return '-User {}-'.format(self.name)


class Tweet(DB.Model):
    """Tweet text and data."""
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(300))  # Allows for text + links
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))

    def __repr__(self):
        return '-Tweet {}-'.format(self.text)


def insert_example_users():
    """Example data to play with."""
    austen = User(id=1, name='austen')
    elon = User(id=2, name='elonmusk')
    DB.session.add(austen)
    DB.session.add(elon)
    DB.session.commit()

def insert_example_tweets():
    """Example data to play with."""
    tweet1 = Tweet(id=1, text='I love dogs.', user_id=1)
    tweet2 = Tweet(id=2, text='I love cats.', user_id=2)
    tweet3 = Tweet(id=3, text='I love chocolate.', user_id=1)
    tweet4 = Tweet(id=4, text='I love vanilla.', user_id=2)
    tweet5 = Tweet(id=5, text='I love cars.', user_id=1)
    tweet6 = Tweet(id=6, text='I love bikes.', user_id=2)
    DB.session.add(tweet1)
    DB.session.add(tweet2)
    DB.session.add(tweet3)
    DB.session.add(tweet4)
    DB.session.add(tweet5)
    DB.session.add(tweet6)
    DB.session.commit()