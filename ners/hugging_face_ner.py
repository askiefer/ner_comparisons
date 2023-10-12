# Hugging Face
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
hugging_face_nlp = pipeline("ner", model=model, tokenizer=tokenizer)

from common import get_utterance_scores, calculate_metrics


def extract_names_hugging_face(text):
    ner_results = hugging_face_nlp(text)
    person_tokens = []
    last_name = ""
    following_bper = False
    for ent in ner_results:
        if ent["entity"] == "B-PER":
            person_tokens.append(ent["word"])
            following_bper = True
        elif ent["entity"] == "I-PER" and following_bper is True:
            last_name += ent["word"].replace("##", "")
        else:
            if following_bper:
                if last_name:
                    person_tokens.append(last_name)
                following_bper = False
                last_name = ""
    if last_name:
        person_tokens.append(last_name)
    non_person_tokens = [ent["word"] for ent in ner_results if ent["entity"] and (ent["entity"] != "B-PER" and ent["entity"] != "I-PER")]
    return person_tokens, non_person_tokens


if __name__ == "__main__":

    model = "Spacy"
    metrics = get_utterance_scores(model, extract_names_hugging_face)
    calculate_metrics(model, metrics)
