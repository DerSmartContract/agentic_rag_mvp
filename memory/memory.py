class Memory:
    def __init__(self):
        self.data = {}

    def store(self, query, context):
        self.data[query] = context

    def retrieve(self, query):
        return self.data.get(query, "")