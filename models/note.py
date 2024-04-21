"""Module providing an ndb model for notes."""

from google.cloud.ndb import (
    Model,
    StringProperty,
    DateTimeProperty,
    TextProperty,
    KeyProperty,
)


class Note(Model):
    """Note mode - a single note"""

    # the title of the note
    title = StringProperty()

    # an optional user generated comment
    comment = StringProperty()

    # an optional HTML snippet
    snippet = TextProperty()

    # the optional URL of the note
    url = TextProperty()

    # the foreign key to the user
    user = KeyProperty(kind="User", required=True)

    # the list of related notes
    related = KeyProperty(kind="Note", repeated=True)

    # the time the note was originally created
    created = DateTimeProperty(auto_now_add=True)

    # the time the related notes list was last updated
    related_updated = DateTimeProperty(auto_now_add=True)

    # the time the note was last updated
    updated = DateTimeProperty(auto_now_add=True)
