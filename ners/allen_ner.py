# Allen NLP
from allennlp.predictors.predictor import Predictor
from common import get_utterance_scores, calculate_metrics


allen_predictor = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/ner-elmo.2021-02-12.tar.gz")


def extract_names_allen(text):
    ents = allen_predictor.predict(
        sentence=text
    )
    words = ents["words"]
    tags = ents["tags"]
    person_tokens = [word for idx, word in enumerate(words) if tags[idx] == "B-PER" or tags[idx] == "L-PER"]
    non_person_tokens = [word for idx, word in enumerate(words) if tags[idx] and (tags[idx] != "B-PER" and tags[idx] != "L-PER")]
    return person_tokens, non_person_tokens


if __name__ == "__main__":

    model = "Allen"
    metrics = get_utterance_scores(model, extract_names_allen)
    calculate_metrics(model, metrics)
