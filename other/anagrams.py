from __future__ import print_function
import collections, pprint, time, os

def signature(word):
    return ''.join(sorted(word))

def main():
    start_time = time.time()
    print('creating word list...')
    path = os.path.split(os.path.realpath(__file__))
    with open(path[0] + '/words') as f:
        word_list = sorted(list(set([word.strip().lower() for word in f])))

    word_bysig = collections.defaultdict(list)
    for word in word_list:
        word_bysig[signature(word)].append(word)

    print('finding anagrams...')
    all_anagrams = {word: word_bysig[signature(word)]
                    for word in word_list if len(word_bysig[signature(word)]) > 1}

    print('writing anagrams to file...')
    with open('anagrams.txt', 'w') as file:
        file.write('all_anagrams = ')
        file.write(pprint.pformat(all_anagrams))

    total_time = round(time.time() - start_time, 2)
    print(('Done [', total_time, 'seconds ]'))

if __name__ == "__main__":
    main()
