# NLTK
import nltk
from common import get_utterance_scores, calculate_metrics


def extract_names_nltk(text):
    tokens = nltk.word_tokenize(text)
    ents = nltk.pos_tag(tokens)
    person_tokens = [ent[0] for ent in ents if ent[1] == "NNP"]
    non_person_tokens = [ent[0] for ent in ents if ent[1] and ent[1] != "NNP"]
    return person_tokens, non_person_tokens


if __name__ == "__main__":

    model = "NLTK"
    metrics = get_utterance_scores(model, extract_names_nltk)
    calculate_metrics(model, metrics)
