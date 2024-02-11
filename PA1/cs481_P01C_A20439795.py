import sys

import nltk
from nltk.util import ngrams
from collections import Counter

from nltk.corpus import brown
from nltk.corpus import stopwords

if __name__ == '__main__':
    sentence = ''
    match_ngrams = []
    probability = []
    # load
    brown = nltk.corpus.brown.words()
    stopwords = nltk.corpus.stopwords.words()

    filtered_brown = [word.lower() for word in brown if word not in stopwords]
    # after filtered, this is what we need to search
    brown_count = Counter(filtered_brown)
    # handle the first token
    while True:
        userInput = input('Enter a word:\n  W: ').lower()
        if userInput not in set(filtered_brown):
            userChoice = input('  a. ask again\n  b. quit\n    userChoice: ')
            if userChoice.lower() == 'b':
                print('Exit')
                sys.exit(0)
            continue
        sentence = userInput
        break
    # handle the rest prediction
    # N fixed on 2
    # get the ngrams out
    ngrams_brown = list(ngrams(filtered_brown, 2))
    ngrams_brown_count = Counter(ngrams_brown)
    while True:
        # filter out and find only match
        # reset all the storage for next word comes up
        probability = []
        top_3_match = []
        match_ngrams = []
        match_ngrams_count = {}

        # split the sentence to get the last word for denominator token
        split_sentence = sentence.split()
        curr_denominator = split_sentence[len(split_sentence) - 1]
        print(f'[DEBUG] curr_denominator == {curr_denominator}')

        # find out the bigrams token contains with first elemnts equals to denominator
        for i in range(len(ngrams_brown)):
            if ngrams_brown[i][0] == curr_denominator:
                match_ngrams.append(ngrams_brown[i])

        # sort the match_ngrams and pick only top 3
        match_ngrams_count = Counter(match_ngrams)
        top_3_match = Counter(match_ngrams_count).most_common(3)
        print(top_3_match)

        # get probability to list
        for index in range(len(top_3_match)):
            prob = top_3_match[index][1] / brown_count[curr_denominator]
            probability.append(prob)
        print()

        # print out the top 3 and probability
        print(f"Current sentence = {sentence}")
        for count in range(3):
            temp = sentence + " " + top_3_match[count][0][1]
            print(f"{count+1}.  {top_3_match[count][0][1]}  P({temp}) = {probability[count]}\n")
        print("4. quit")
        try:
            userSelect = int(input("Which word should follow:"))
        except:
            userSelect = 1

        # handle selection part
        if userSelect in [1, 2, 3]:
            print(f'userSelection = {top_3_match[userSelect - 1][0][1]}')
            sentence = sentence + ' ' + top_3_match[userSelect - 1][0][1]
        elif userSelect == 4:
            print('Exit')
            sys.exit(0)
        else:
            sentence = sentence + ' ' + top_3_match[0][0][1]
        print('======================================================')

