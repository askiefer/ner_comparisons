# Spacy
import en_core_web_lg
spacy_nlp = en_core_web_lg.load()
spacy_nlp.add_pipe('sentencizer')


from common import get_utterance_scores, calculate_metrics


def extract_names_spacy(text):
    doc = spacy_nlp(text)
    person_tokens = [token.text for token in doc if token.ent_type_ == 'PERSON']
    non_person_tokens = [token.text for token in doc if token.ent_type_ and token.ent_type != 'PERSON']
    return person_tokens, non_person_tokens


if __name__ == "__main__":

    model = "Spacy"
    metrics = get_utterance_scores(model, extract_names_spacy)
    calculate_metrics(model, metrics)
