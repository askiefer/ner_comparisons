import csv
import time
import random


def calculate_metrics(model_type, counts):
    # metrics
    # complete matching - precision, recall, f1 score
    # partial matching - precision, recall, f1 score
    # F1 = 2 * (precision * recall) / (precision + recall)
    # tp, fp, fn, tn = counts
    # precision = tp / (tp + fp)
    # recall = tp / (tp + fn)
    # accuracy = (tp + tn) / (tp + fp + fn + tn)
    # f1_score = (2 * precision * recall) / (precision + recall)
    # print(f"""
    # Metrics {model_type}:
    #     precision: {precision}
    #     recall: {recall}
    #     accuracy: {accuracy}
    #     f1_score: {f1_score}
    # """)
    (full_speaker_name_person, partial_speaker_name_person,
     full_speaker_name_nonperson, partial_speaker_name_nonperson,
     other_person_names, no_person_names, no_speaker_name_person_tokens,
     no_speaker_name_no_person_tokens, avg_time) = counts
    print(f"""
    Metrics {model_type}:
        full_speaker_name_person: {full_speaker_name_person}
        partial_speaker_name_person: {partial_speaker_name_person}
        full_speaker_name_nonperson: {full_speaker_name_nonperson}
        partial_speaker_name_nonperson: {partial_speaker_name_nonperson}
        other_person_names: {other_person_names}
        no_person_names: {no_person_names}
        no_speaker_name_person_tokens: {no_speaker_name_person_tokens}
        no_speaker_name_no_person_tokens: {no_speaker_name_no_person_tokens}
        avg_time: {avg_time}
    """)


def get_data(filename):
    data = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        next(reader, None)
        for row in reader:
            data.append(row)
    return data


def get_utterance_scores(model_type, func):
    # tp = 0
    # fp = 0
    # tn = 0
    # fn = 0
    # speaker name included metrics
    full_speaker_name_person = 0
    partial_speaker_name_person = 0
    full_speaker_name_nonperson = 0
    partial_speaker_name_nonperson = 0
    other_person_names = 0
    no_person_names = 0

    # speaker name not included metrics
    no_speaker_name_person_tokens = 0
    no_speaker_name_no_person_tokens = 0

    sum_time = 0
    print(f"Running NER for {model_type}")

    filenames = ['./speakers.csv', './utterances.csv']
    for file_idx, filename in enumerate(filenames):
        data = get_data(filename)
        for idx, row in enumerate(data):
            if idx % 500 == 0:
                print(idx, "...", "\n")
            text = row["text"]
            first = row["first"].strip()
            last = row["last"].strip()
            full_name = f"{first} {last}"

            start = time.time()
            person_tokens, non_person_tokens = func(text)
            end = time.time()
            sum_time += round(end - start, 2)

            # import pdb; pdb.set_trace()

            if file_idx == 0:  # speaker name included case
                if full_name in text:

                    # print("time in ms:", end - start)
                    # has full name of the speaker tagged as PERSON
                    if (first in person_tokens and last in person_tokens) or full_name in person_tokens:
                        # tp += 1
                        full_speaker_name_person += 1
                    # has partial name of the speaker tagged as PERSON
                    elif (first in person_tokens or last in person_tokens):
                        partial_speaker_name_person += 1
                    # has full name of the speaker tagged as NONPERSON
                    elif (first in non_person_tokens and last in non_person_tokens) or full_name in non_person_tokens:
                        # fp += 1
                        full_speaker_name_nonperson += 1
                    elif (first in non_person_tokens or last in non_person_tokens):
                        partial_speaker_name_nonperson += 1
                    # has non-speaker person names
                    elif person_tokens and (first not in person_tokens and last not in person_tokens):
                        other_person_names += 1
                    # does not have any names
                    else:
                        no_person_names += 1
                        # fn += 1
            else:  # speaker name is not included
                if person_tokens:
                    no_speaker_name_person_tokens += 1
                else:
                    no_speaker_name_no_person_tokens += 1


    avg_time = round(sum_time / 10000, 2)
    return (
        full_speaker_name_person,
        partial_speaker_name_person,
        full_speaker_name_nonperson,
        partial_speaker_name_nonperson,
        other_person_names,
        no_person_names,
        no_speaker_name_person_tokens,
        no_speaker_name_no_person_tokens,
        avg_time
    )
