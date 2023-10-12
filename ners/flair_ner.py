# Flair NLP
from flair.data import Sentence
from flair.models import SequenceTagger
from common import get_utterance_scores, calculate_metrics


flair_tagger = SequenceTagger.load("flair/ner-english")


def extract_names_flair(text):
    sentence = Sentence(text)
    flair_tagger.predict(sentence)
    entities = [ent.text for ent in sentence.get_spans('ner')]
    person_tokens = [entities[idx] for idx, l in enumerate(sentence.labels) if l.value == "PER"]
    non_person_tokens = [entities[idx] for idx, l in enumerate(sentence.labels) if l.value != "PER"]
    return person_tokens, non_person_tokens


if __name__ == "__main__":

    model = "Flair"
    metrics = get_utterance_scores(model, extract_names_flair)
    calculate_metrics(model, metrics)
