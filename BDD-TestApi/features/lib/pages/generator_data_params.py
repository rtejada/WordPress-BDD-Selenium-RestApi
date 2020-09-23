import os
import json
from lib.pages.generator_random_data import GeneratorRamdomData


class GeneratorDataParameters(GeneratorRamdomData):

    def __init__(self):

        self.data_parameters = ''
        with open(os.getcwd() + "/BDD-TestApi/features/lib/data/key_params.json") as file:
            self.data_parameters = json.load(file)

    def content(self):

        return self.data_parameters["content"] + self.random_letters(120)

    def title(self):

        return self.data_parameters["title"] + self.random_name(12)

    def excerpt(self):

        return self.data_parameters["excerpt"] + self.random_lowercase(20)

    def slug(self):
        return self.data_parameters["slug"]

    def status(self):

        return self.data_parameters["status"]

    def author(self):
        return self.data_parameters["author"]

    def comment_status(self):
        return self.data_parameters["comment_status"]

    def ping_status(self):
        return self.data_parameters["ping_status"]

prueba=GeneratorDataParameters()
print(prueba.content())