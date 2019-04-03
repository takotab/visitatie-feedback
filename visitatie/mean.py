from visitatie.toetsen.q_a import add_single_qa


class Mean(object):
    def __init__(self, base_question=""):
        self.sum = 0
        self.entries = 0
        self.question = {}
        self.base_q = base_question

    def add(self, item: int, question: str = None):
        self.sum += item
        self.entries += 1
        if question is not None:
            if question in self.question:
                self.question[question].add(item)
            else:
                self.question[question] = Mean()
                self.question[question].add(item)

    def __call__(self, item: int, question: str = None):
        self.add(item, question)

    def mean(self):
        self.handle_question()
        return self.sum / self.entries

    def __len__(self):
        return self.entries

    def handle_question(self):
        for key, item in self.question.items():
            add_single_qa(key, item.mean(), self.base_q)
