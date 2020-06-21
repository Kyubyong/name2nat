from flair.models import TextClassifier
from flair.data import Sentence
import pickle
import os

CKPT = os.path.dirname(os.path.abspath(__file__)) + "/best-model.pt"
DICT = os.path.dirname(os.path.abspath(__file__)) + "/name2nats.pkl"

class Name2nat:
    def __init__(self, ckpt=CKPT, name2nats=DICT):
        self.classifier = TextClassifier.load(ckpt)
        self.name2nats = self.construct(name2nats)

    def construct(self, name2nats):
         return pickle.load(open(name2nats, 'rb'))

    def convert(self, name):
        name = name.replace(" ", "▁")
        name = " ".join(char for char in name)
        return name

    def restore(self, name):
        return name.replace(" ", "").replace("▁", " ")

    def get_top_n_results(self, sentence, top_n):
        results = sentence.labels
        results = [(each.value, each.score) for each in results]
        results = sorted(results, key=lambda x: x[1], reverse=True)
        results = results[:top_n]
        return results

    def __call__(self, names, top_n=1, use_dict=True, mini_batch_size=128):
        if not isinstance(names, list):
            names = [names]

        sentences = [Sentence(self.convert(name), use_tokenizer=True) for name in names]
        self.classifier.predict(sentences, mini_batch_size=mini_batch_size, multi_class_prob=True, verbose=len(sentences)>1000)

        ret = []
        for sent in sentences:
            name = self.restore(sent.to_tagged_string()) # plain string
            if use_dict:
                if name in self.name2nats:
                    results = [(nat, 1.0) for nat in self.name2nats[name]]
                else:
                    results = self.get_top_n_results(sent, top_n)
            else:
                results = self.get_top_n_results(sent, top_n)

            ret.append((name, results))
        return ret







