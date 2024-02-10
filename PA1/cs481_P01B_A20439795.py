import nltk
from nltk.corpus import brown
from nltk import bigrams
from collections import Counter


if __name__ == '__main__':
    # handling user input and convert it to lowercase
    userInput = input('enter a sentence\n   S: ').lower()
    tokens = userInput.split()
    # I using <s> and </s> for the start and end tag
    tokens = ['<s>']+tokens+['</s>']
    # process all the tokens and brown tokens to bigrams structure
    bigram_token = list(bigrams(tokens))
    # this part will return {(bigram/unigram token) : amount}
    bigram_brown = list(bigrams(brown.words()))
    unigram_brown = list(brown.words())
    bigram_brown_counts = Counter(bigram_brown)
    unigram_brown_counts = Counter(unigram_brown)
    # P(Second word|First word) = C(First word, Second word)/C(First word)
    # first extract out <s> and </s> and assign it to P = 0.25
    # next get the counter of C(First word, Second word)
    probabilities = []
    for bg in bigram_token:
        if bg[0] == '<s>' or bg[1] == '</s>':
            prob = 0.25
        else:
            prob = bigram_brown_counts[bg] / unigram_brown_counts[bg[0]] if unigram_brown_counts[bg[0]] > 0 else 0.0
        probabilities.append((bg, prob))
    # get final probability
    final_probability = 1
    for _, prob in probabilities:
        final_probability *= prob
    # Display results
    print(f"Sentence that User Input: {userInput}")
    print("Bigrams and probabilities:")
    for bg, prob in probabilities:
        print(f"  {bg}: {prob}")
    print(f"\nFinal probability P(S): {final_probability}")
