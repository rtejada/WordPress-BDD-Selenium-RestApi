import os
import json
from lib.pages.generator_random_data import GeneratorRamdomData
from random import randint


class GeneratorDataParameters(GeneratorRamdomData):

    def __init__(self):

        print(os.getcwd())
        self.data_parameters = ''
        with open(os.getcwd() + "/BDD-TestApi/features/lib/data/key_params.json") as file:
            self.data_parameters = json.load(file)

    def content(self):

        return self.data_parameters["content"] + self.random_letters(120)

    def title(self):

        return self.data_parameters["title"] + self.random_name(12)

    def excerpt(self):

        return self.data_parameters["excerpt"] + self.random_lowercase(20)

    def description(self):
        return self.random_letters(100)

    def name(self):

        return self.random_name(10)+'-'+str(randint(1, 500))

    def status(self):

        return self.data_parameters["status"]

    def author(self):
        return self.data_parameters["author"]

    def comment_status(self):
        return self.data_parameters["comment_status"]

    def ping_status(self):
        return self.data_parameters["ping_status"]

