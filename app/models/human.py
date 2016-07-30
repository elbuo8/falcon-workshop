from mongoengine import Document, StringField, ListField
from task import Task


class Human(Document):
    ssn = StringField(required=True, unique=True, max_length=9, min_length=9)
    tasks = ListField()

    def create_task(self, data):
        task = Task(data)
        human.tasks.append(task['_id'])
        task.save()
        human.save()

    def to_json(self):
        human = self.to_mongo()
        human['id'] = str(human['_id'])
        del human['_id']
        return human
