import sys

import nltk
from nltk.util import ngrams
from collections import Counter

from nltk.corpus import brown
from nltk.corpus import stopwords

if __name__ == '__main__':
    N = 2
    # load
    filtered_brown = [word for word in brown.words() if word not in stopwords.words()]
    # after filtered, this is what we need to search
    brown_count = Counter(filtered_brown)

    userInput = input('Enter a word:\nW: ').lower()
    while True:
        if userInput in set(filtered_brown):
            N += 1
            ngrams_brown = list(ngrams(filtered_brown, N))
            match_ngrams = [ngram for ngram in ngrams_brown if ngrams_brown[0].lower == userInput]
            ngrams_count = Counter(match_ngrams)
            top_3_ngrams = ngrams_count.most_common(3)
            probability_top_3_ngrams = []
            for word, count in top_3_ngrams:
                prob = count / brown_count[userInput]
                probability_top_3_ngrams.append(prob)
            counter = 0
            for info in zip(top_3_ngrams, probability_top_3_ngrams):
                counter += 1
                word, _ = info[0]
                prob = info[1]
                print(f'{counter}. {word} | Probability = {prob}')
            print(f'4. quit')
            # 做完了打印结果，缺拉出答案并且更新userinput



        else:
            while True:
                choice = input('a. Try again\n b.quit').lower()
                if choice not in ['a', 'b']:
                    print('Invalid input! try again!')
                    continue
                break
            if choice == 'b':
                sys.exit(0)
            else:
                userInput = input('Enter a word:\nW: ').lower()
