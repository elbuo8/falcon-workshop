from mongoengine import Document, StringField, BooleanField


class Task(Document):
    completed = BooleanField(required=True, default=False)
    description = StringField(required=True)
