"""Module providing an ndb model for users."""

from google.cloud.ndb import Model, StringProperty, DateTimeProperty

class User(Model):
    """ User model - a single user """
    display_name = StringProperty()
    updated = DateTimeProperty(auto_now_add=True)
