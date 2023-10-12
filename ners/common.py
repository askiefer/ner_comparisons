import csv
import time


def calculate_metrics(model_type, counts):
    # metrics
    # complete matching - precision, recall, f1 score
    # partial matching - precision, recall, f1 score
    # F1 = 2 * (precision * recall) / (precision + recall)
    tp, fp, fn, tn = counts
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    accuracy = (tp + tn) / (tp + fp + fn + tn)
    f1_score = (2 * precision * recall) / (precision + recall)
    print(f"""
    Metrics {model_type}:
        precision: {precision}
        recall: {recall}
        accuracy: {accuracy}
        f1_score: {f1_score}
    """)


def get_utterance_scores(model_type, func):
    tp = 0
    fp = 0
    tn = 0
    fn = 0

    print(f"Running NER for {model_type}")
    with open('./speakers.csv', "r") as f:
        reader = csv.DictReader(f)
        next(reader, None)
        for idx, row in enumerate(reader):
            if idx % 500 == 0:
                print(idx, "...", "\n")
            text = row["text"]
            first = row["first"].strip()
            last = row["last"].strip()
            full_name = f"{first} {last}"

            if full_name in text:
                start = time.time()
                person_tokens, non_person_tokens = func(text)
                end = time.time()
                print("time in ms:", end - start)

                # metrics COMPLETE case
                if (first in person_tokens and last in person_tokens) or full_name in person_tokens:
                    tp += 1
                elif (first in non_person_tokens or last in non_person_tokens) or full_name in non_person_tokens:
                    fp += 1
                else:
                    fn += 1

    return tp, fp, fn, tn
