import re
import math
from datetime import datetime
from collections import Counter

WINDOW_SIZE = 4
MAX_LINES = 2000


def build_semantic_vectors():
    """Builds a co-occurence matrix of when do different words appear together
    We will represent the matrix with dictionaries in the following manner
    {
        'apple': {'eat': 10, 'peel': 9, 'code': 5, 'sleep': 1, 'blanket': 0},
        'computer': {'code': 10, 'eat': 0, 'stare': 5}
    }
    """
    co_occurence_vectors = {}
    words = []
    lines_read = 0

    file = open('book_1.txt', 'r')
    for line in file:
        if lines_read == MAX_LINES:
            break
        lines_read += 1

        words.extend([
            clean_word(w.lower()) for w in line.split()
        ])

        for i in range(len(words) - (WINDOW_SIZE - 1)):
            nearby_words = words[i:i + WINDOW_SIZE]

            for word in nearby_words:
                frequences = co_occurence_vectors.setdefault(word, {})

                for neighbour in (set(nearby_words) - set([word])): 
                    frequences[neighbour] = frequences.get(neighbour, 0) + 1
                    neighbour_frequences = co_occurence_vectors.setdefault(neighbour, {})
                    neighbour_frequences[word] = neighbour_frequences.get(word, 0) + 1

        words = words[-(WINDOW_SIZE-1):]
    file.close()
    return co_occurence_vectors

def clean_word(word):
    return re.sub(r"(\?|\/|\||\"|\.|\,|\!)", "", word)

def build_distance_matrix(co_occurence_vectors):
    """Build a distance matrix in following format
    {('apple', 'computer'): 0.9, ('apple', 'pearch'): 0.7}"""
    distances = {}
    words = sorted(co_occurence_vectors.keys())
    print(len(words))
    pairs_count = sum(len(value) for value in co_occurence_vectors.values())

    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            v1_dict = co_occurence_vectors[words[i]]    
            v2_dict = co_occurence_vectors[words[j]]
            v1 = []
            v2 = []
            for key, value in v1_dict.items():
                probability_of_key = sum(co_occurence_vectors[key].values()) / pairs_count

                v1.append(
                    math.log(
                        (value / pairs_count) 
                        / 
                        (
                            (sum(v1_dict.values()) / pairs_count)
                            *
                            probability_of_key
                        )
                    )
                )

                if key not in v2_dict:
                    v2.append(0)
                    continue

                v2.append(
                    math.log(
                        (v2_dict[key] / pairs_count) 
                        /
                        ( 
                            (sum(v2_dict.values()) / pairs_count)
                            *
                            probability_of_key
                        )
                    )
                )
            distances[(words[i], words[j])] = cosine(v1, v2)
    return distances
   
def cosine(v, v2):
    assert len(v) == len(v2), "Vectors must be same length"
    sum_of_products = 0
    for i in range(len(v)):
        sum_of_products += v[i] * v2[i]

    # This is a slight optimization, also saves us from divide by zero
    if sum_of_products == 0:
        return 0

    sum_of_squares = sum([x ** 2 for x in v]) 
    sum_of_squares2 = sum([x ** 2 for x in v2])
    return sum_of_products / (sum_of_squares * sum_of_squares2)

def main():
    before = datetime.now()
    print(before)
    vectors = build_semantic_vectors()   
    print(f'Building semantic vectors took {(datetime.now() - before).total_seconds()}s')
    before = datetime.now()
    distances = build_distance_matrix(vectors).items()
    print(f'Calculating distances took {(datetime.now() - before).total_seconds()}s')
    s = sorted(distances, key=lambda t: t[1], reverse=True)
    print("\n".join([str(t) for t in s]))

main()
