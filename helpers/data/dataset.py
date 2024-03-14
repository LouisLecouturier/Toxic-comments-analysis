def print_data_composition(data):
    severe_toxic_count = len(data[data["severe_toxic"] == 1])
    obscene_count = len(data[data["obscene"] == 1])
    threat_count = len(data[data["threat"] == 1])
    insult_count = len(data[data["insult"] == 1])
    identity_hate_count = len(data[data["identity_hate"] == 1])

    neutral_count = len(data[(data["toxic"] == 0) & (data["severe_toxic"] == 0)
                             & (data["obscene"] == 0) & (data["threat"] == 0) & (
                                     data["insult"] == 0) & (data["identity_hate"] == 0)])

    print(f'Number of neutral comments : {neutral_count}\n')
    print(f'Number of toxic comments : {len(data) - neutral_count}')
    print(f'| number of severe_toxic : {severe_toxic_count}')
    print(f'| number of obscene : {obscene_count}')
    print(f'| number of threat : {threat_count}')
    print(f'| number of insult : {insult_count}')
    print(f'| number of identity_hate : {identity_hate_count}')
