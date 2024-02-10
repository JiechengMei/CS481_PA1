import nltk
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


if __name__ == '__main__':
    numberOfWords = 10
    symbol = [',', '.', '``', '\'\'', ';', '?', '--', ')', '(', ':', '!', '-', '&', '\'']

    # PartA.1/2
    # download corpora
    nltk.download('brown')
    nltk.download('reuters')
    nltk.download('stopwords')

    # put all the corpus to an array
    brown = nltk.corpus.brown.words()
    reuters = nltk.corpus.reuters.words()
    stopwords = nltk.corpus.stopwords.words()

    # filtered out all the stopwords token
    filtered_brown = [word for word in brown if word not in stopwords]
    filtered_reuters = [word for word in reuters if word not in stopwords]

    # find out the frequency and store into dictionary
    frequencyDistribution_brown = nltk.FreqDist(word.lower() for word in filtered_brown)
    frequenciesAndWords_brown = dict()
    for word in filtered_brown:
        frequenciesAndWords_brown[word] = frequencyDistribution_brown[word]

    frequencyDistribution_reuters = nltk.FreqDist(word.lower() for word in filtered_reuters)
    frequenciesAndWords_reuters = dict()
    for word in filtered_reuters:
        frequenciesAndWords_reuters[word] = frequencyDistribution_reuters[word]

    # put all information into a list and sort it to most to least
    frequenciesAndWords_brown = list(frequenciesAndWords_brown.items())
    frequenciesAndWords_brown.sort(key=lambda a: a[1])
    frequenciesAndWords_brown.reverse()

    frequenciesAndWords_reuters = list(frequencyDistribution_reuters.items())
    frequenciesAndWords_reuters.sort(key=lambda a: a[1])
    frequenciesAndWords_reuters.reverse()

    labels_brown, frequence_brown = map(list, zip(*frequenciesAndWords_brown))
    labels_reuters, frequence_reuters = map(list, zip(*frequenciesAndWords_reuters))

    # Print the table of word that is top 10 in list
    print('========= Brown =========')
    for index in range(numberOfWords):
        print(f'{labels_brown[index]:<5}', ' ', f'{frequence_brown[index]:<5}')
    print('========= Brown =========')
    print('========= Reuters =========')
    for index in range(numberOfWords):
        print(f'{labels_reuters[index]:<5}', ' ', f'{frequence_reuters[index]:<5}')
    print('========= Reuters =========')
    # bar chart
    yPos = range(len(labels_brown))
    plt.figure(figsize=(20, 20))
    plt.bar(yPos[:numberOfWords], frequence_brown[:numberOfWords], align='center', alpha=0.5)
    plt.xticks(yPos[:numberOfWords], labels_brown[:numberOfWords], rotation=90, fontsize=16)
    plt.title('Top 10 token: Brown', fontsize=26)
    plt.xlabel('Token', fontsize=22)
    plt.ylabel('Frequency count', fontsize=22)
    plt.show()

    # bar chart for reuters
    yPos = range(len(labels_reuters))
    plt.figure(figsize=(20, 20))
    plt.bar(yPos[:numberOfWords], frequence_reuters[:numberOfWords], align='center', alpha=0.5)
    plt.xticks(yPos[:numberOfWords], labels_reuters[:numberOfWords], rotation=90, fontsize=16)
    plt.title('Top 10 token: Reuters', fontsize=22)
    plt.xlabel('Token', fontsize=22)
    plt.ylabel('Frequency count', fontsize=22)
    plt.show()

    # part below is filter word without symbol explanation are similar like previous
    # the difference is I using filtered_brown/reuters to filter out symbol that is on previous top 10
    filtered_symbol_brown = [word for word in filtered_brown if word not in symbol]
    frequencyDistribution_symbol_brown = nltk.FreqDist(word.lower() for word in filtered_symbol_brown)
    frequenciesAndWords_symbol_brown = dict()

    filtered_symbol_reuters = [word for word in filtered_reuters if word not in symbol]
    frequencyDistribution_symbol_reuters = nltk.FreqDist(word.lower() for word in filtered_symbol_reuters)
    frequenciesAndWords_symbol_reuters = dict()

    for word in filtered_symbol_brown:
        frequenciesAndWords_symbol_brown[word] = frequencyDistribution_symbol_brown[word]

    for word in filtered_symbol_reuters:
        frequenciesAndWords_symbol_reuters[word] = frequencyDistribution_symbol_reuters[word]

    frequenciesAndWords_symbol_brown = list(frequencyDistribution_symbol_brown.items())
    frequenciesAndWords_symbol_brown.sort(key=lambda a: a[1])
    frequenciesAndWords_symbol_brown.reverse()

    frequenciesAndWords_symbol_reuters = list(frequencyDistribution_symbol_reuters.items())
    frequenciesAndWords_symbol_reuters.sort(key=lambda a: a[1])
    frequenciesAndWords_symbol_reuters.reverse()

    labels_symbol_brown, frequence_symbol_brown = map(list, zip(*frequenciesAndWords_symbol_brown))
    labels_symbol_reuters, frequence_symbol_reuters = map(list, zip(*frequenciesAndWords_symbol_reuters))

    print('===== Brown without symbol =====')
    for index in range(numberOfWords):
        print(f'{labels_symbol_brown[index]:<5}', ' ', f'{frequence_symbol_brown[index]:<5}')
    print('===== Brown without symbol =====')
    print('===== Reuters without symbol =====')
    for index in range(numberOfWords):
        print(f'{labels_symbol_reuters[index]:<5}', ' ', f'{frequence_symbol_reuters[index]:<5}')
    print('===== Reuters without symbol =====')

    yPos = range(len(labels_symbol_brown))
    plt.figure(figsize=(20, 20))
    plt.bar(yPos[:numberOfWords], frequence_symbol_brown[:numberOfWords], align='center', alpha=0.5)
    plt.xticks(yPos[:numberOfWords], labels_symbol_brown[:numberOfWords], rotation=90, fontsize=16)
    plt.title('Top 10 token: Brown without symbol', fontsize=26)
    plt.xlabel('Token', fontsize=22)
    plt.ylabel('Frequency count', fontsize=22)
    plt.show()

    yPos = range(len(labels_symbol_reuters))
    plt.figure(figsize=(20, 20))
    plt.bar(yPos[:numberOfWords], frequence_symbol_reuters[:numberOfWords], align='center', alpha=0.5)
    plt.xticks(yPos[:numberOfWords], labels_symbol_reuters[:numberOfWords], rotation=90, fontsize=16)
    plt.title('Top 10 token: Reuters without symbol', fontsize=26)
    plt.xlabel('Token', fontsize=22)
    plt.ylabel('Frequency count', fontsize=22)
    plt.show()

    # PartA.3
    # get top 1000 element from the list and draw the plot
    labels_brown2 = labels_brown[:1000]
    frequence_brown2 = frequence_brown[:1000]
    _, ax = plt.subplots()
    xs = range(len(labels_brown))
    labels_brown2 = range(len(labels_brown))


    def format_fn(tick_val, _):
        if int(tick_val) in xs:
            return labels_brown2[int(tick_val)]
        else:
            return ''
    ax.xaxis.set_major_formatter(format_fn)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.plot(xs, frequence_brown)
    ax.set_title('Token frequency counts in corpus ranked - Brown')
    ax.set_xscale('log')
    ax.set_yscale('log')
    plt.xlabel('log(Rank)')
    plt.ylabel('log(Frequency count)')
    plt.show()
    # for reuters
    labels_reuters2 = labels_reuters[:1000]
    frequence_reuters2 = frequence_reuters[:1000]
    _, ax = plt.subplots()
    xs = range(len(labels_reuters))
    labels_reuters2 = range(len(labels_reuters))


    def format_fn(tick_val, _):
        if int(tick_val) in xs:
            return labels_reuters2[int(tick_val)]
        else:
            return ''


    ax.xaxis.set_major_formatter(format_fn)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.plot(xs, frequence_reuters)
    ax.set_title('Token frequency counts in corpus ranked - Reuters')
    ax.set_xscale('log')
    ax.set_yscale('log')
    plt.xlabel('log(Rank)')
    plt.ylabel('log(Frequency count)')
    plt.show()

    # PartA.4
    technical = 'restore'.lower()
    ntechnical = 'add'.lower()

    total_index_brown = len(labels_brown)
    total_index_reuters = len(labels_reuters)

    # brown
    # find out technical word
    try:
        word_index = labels_brown.index(technical)
        word_frequency = frequence_brown[word_index]
    except ValueError:
        print(f"'{technical}' was not found in the list.")
        word_frequency = 0

    if word_frequency != 0:
        prob_brown = word_frequency / total_index_brown
    else:
        prob_brown = 0

    print(f'Brown | Probability of {technical} = {prob_brown} by word frequency = {word_frequency} / total index = {total_index_brown}')
    # find out not technical word
    try:
        word_index = labels_brown.index(ntechnical)
        word_frequency = frequence_brown[word_index]
    except ValueError:
        print(f"'{ntechnical}' was not found in the list.")
        word_frequency = 0

    if word_frequency != 0:
        prob_brown = word_frequency / total_index_brown
    else:
        prob_brown = 0
    print(f'Brown | Probability of {ntechnical} = {prob_brown} by word frequency = {word_frequency} / total index = {total_index_brown}')
    # reuters
    # technical word
    try:
        word_index = labels_reuters.index(technical)
        word_frequency = frequence_reuters[word_index]
    except ValueError:
        print(f"'{technical}' was not found in the list.")
        word_frequency = 0

    if word_frequency != 0:
        prob_reuters = word_frequency / total_index_reuters
    else:
        prob_reuters = 0

    print(f'Reuters | Probability of {technical} = {prob_reuters} by word frequency {word_frequency} / total index = {total_index_reuters}')
    # find out not technical word
    try:
        word_index = labels_reuters.index(ntechnical)
        word_frequency = frequence_reuters[word_index]
    except ValueError:
        print(f"'{ntechnical}' was not found in the list.")
        word_frequency = 0

    if word_frequency != 0:
        prob_reuters = word_frequency / total_index_brown
    else:
        prob_reuters = 0
    print(f'Reuters | Probability of {ntechnical} = {prob_reuters} by word frequency {word_frequency} / total index = {total_index_reuters}')

