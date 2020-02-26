from faker import Faker
faker = Faker()


class User:

    def __init__(self):
        self.first_name = faker.first_name()
        self.job = 'QA Engineer'

    def random_user(self):
        return {'first_name': self.first_name, 'job': self.job }
