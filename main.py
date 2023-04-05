from collections import defaultdict
from chain import WordChain

def get_book_1():
    with open("pg70462.txt", "r") as f:
        return f.read()


def yield_block(text):
    for block in text.split("\t"):
        yield block


def write_from_chain(chains, first_word, word_count):
    out_str = first_word
    curr_word = first_word
    for _ in range(word_count):
        curr_word = chains[curr_word].compute_next()
        out_str += f" {curr_word}"
    return f"{out_str}."


def main():
    tokens = defaultdict(list)
    book = get_book_1()
    ts = book.split(" ")
    for i, token in enumerate(ts):
        if i < len(ts) - 1:
            tokens[token].append(ts[i+1])

    words = {}
    for token, values in tokens.items():
        wc = WordChain(token)
        for v in values:
            wc.add_next(v)
        words[token] = wc

    print(write_from_chain(words, "the", 20))

if __name__ == "__main__":
    main()