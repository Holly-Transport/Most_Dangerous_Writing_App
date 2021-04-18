import pandas

class Prompt:

    def __init__(self):
        self.data = pandas.read_csv("Prompts.csv")

    def NewPrompt (self):
        self.prompt = self.data.sample()
        return self.prompt.values.tolist()


