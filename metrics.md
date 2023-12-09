NER model time is time to run a single row

Metrics Spacy:
    
    NER model time (ms): 0.004189014434814453
    precision: 0.9426514399205561
    recall: 0.991901776384535
    accuracy: 0.9354520817935452
    f1_score: 0.9666496945010183

Metrics Hugging Face:
    
    NER model time (ms): 0.1040647029876709
    precision: 0.9970817120622568
    recall: 0.7592592592592593
    accuracy: 0.7575757575757576
    f1_score: 0.8620689655172414

Metrics Stanford NLP
    
    NER model time (ms): 3.0293869972229004
    precision: 0.9747878182725911
    recall: 0.9866093986862051
    accuracy: 0.962059620596206
    f1_score: 0.9806629834254144

Metrics Allen NLP

    NER model time (ms): 0.14516806602478027
    precision: 0.9709554140127389
    recall: 0.9660329531051964
    accuracy: 0.9389012071938901
    f1_score: 0.9684879288437103

Metrics nltk:
    
    NER model time (ms): 0.055999040603637695
    precision: 0.8859495882206139
    recall: 0.9855635757912271
    accuracy: 0.87459965508746
    f1_score: 0.9331055329215402

Metrics Flair

    NER model time (ms): 0.18662190437316895
    precision: 0.9946902654867257
    recall: 0.9742446755819713
    accuracy: 0.9692042374969204
    f1_score: 0.9843613161516326


#### New Metrics

  Metrics Spacy:

        full_speaker_name_person: 3837
        partial_speaker_name_person: 143
        full_speaker_name_nonperson: 62
        partial_speaker_name_nonperson: 7
        other_person_names: 3
        no_person_names: 7
        no_speaker_name_person_tokens: 1938
        no_speaker_name_no_person_tokens: 3061
        avg_time: 0.01

Metrics HuggingFace:

        full_speaker_name_person: 3075
        partial_speaker_name_person: 736
        full_speaker_name_nonperson: 2
        partial_speaker_name_nonperson: 7
        other_person_names: 229
        no_person_names: 10
        no_speaker_name_person_tokens: 1888
        no_speaker_name_no_person_tokens: 3111
        avg_time: 0.05

 Metrics NLTK:
        full_speaker_name_person: 3550
        partial_speaker_name_person: 478
        full_speaker_name_nonperson: 28
        partial_speaker_name_nonperson: 1
        other_person_names: 2
        no_person_names: 0
        no_speaker_name_person_tokens: 3904
        no_speaker_name_no_person_tokens: 1095
        avg_time: 0.0