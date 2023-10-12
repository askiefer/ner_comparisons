# Stanford NLP
import nltk
from nltk.tag.stanford import StanfordNERTagger
from nltk.tokenize import word_tokenize
from common import get_utterance_scores, calculate_metrics

nltk.download('punkt')

PATH_TO_JAR='./stanford-ner.jar'
PATH_TO_MODEL = './english.all.3class.distsim.crf.ser.gz'
stanford_tagger = StanfordNERTagger(model_filename=PATH_TO_MODEL, path_to_jar=PATH_TO_JAR, encoding='utf-8')


def extract_names_stanford(text):
    tokenized_text = word_tokenize(text)
    classified_text = stanford_tagger.tag(tokenized_text)
    person_tokens = [t[0] for t in classified_text if t[1] == 'PERSON']
    non_person_tokens = [t[0] for t in classified_text if t[1] and t[1] != 'PERSON']
    return person_tokens, non_person_tokens


if __name__ == "__main__":

    model = "Stanford"
    metrics = get_utterance_scores(model, extract_names_stanford)
    calculate_metrics(model, metrics)
