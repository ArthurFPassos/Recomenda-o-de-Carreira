# base de fatos

class Facts:
    def __init__(self):
        self.facts = {}

    def add_fact(self, fact_name):
        self.facts[fact_name] = True

    def has_fact(self, fact_name):
        return self.facts.get(fact_name, False)
