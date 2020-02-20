from collections import namedtuple
import sys

Library = namedtuple('Library', ['id', 'signup', 'bpd', 'books', 'score', 'potential'])

sample_libraries = [Library(0, 2, 2, [0, 1, 2, 3, 4], 777, 888), Library(1, 3, 1, [3, 2, 5, 0], 999, 1111)]
"""
id: of Library
signup: days for signup
bpd: books which can be scanned per day
books: a dictionary of books, key: score
"""

def parse_input_file(input_file):
    global libraries, total_num_days

    with open(input_file, 'r') as fh:
        line = fh.readline().rstrip('\n').split(' ')
        libraries = []
        num_books = int(line[0])
        num_libraries = int(line[1])
        total_num_days = int(line[2])
        line = fh.readline().rstrip('\n').split(' ')
        book_score = [int(s) for s in line]
        assert len(book_score) == num_books
        for id in range(0, num_libraries):
            line1 = fh.readline().rstrip('\n').split(' ')
            line2 = fh.readline().rstrip('\n').split(' ')
            books = [int(s) for s in line2]
            books = {b: book_score[b] for b in books}
            assert len(books) == int(line1[0])
            score = sum(books.values())
            bpd = int(line1[2])
            signup = int(line1[1])
            potential = score * bpd / signup
            libraries.append(Library(id, signup, bpd, books, score, potential))


def write_file(filename, scanned_libraries):
    with open(filename, 'w') as fh:
        fh.write('{}\n'.format(len(scanned_libraries)))
        for id, books in scanned_libraries.items():
            fh.write("{} {}\n".format(id, len(books)))
            # TODO check libraries with 0 books
            if (len(books) is not 0):
                fh.write(' '.join(map(str, books)) + '\n')


def write_file(filename):
    with open(filename, 'w') as fh:
        fh.write('{}\n'.format(len(libraries)))
        for lib in libraries:
            fh.write(str(lib.id) + ' ')
            fh.write(str(len(lib.books)) + '\n')
            fh.write(' '.join(map(str, lib.books)) + '\n')


def optimize():
    elapsed_days = 0
    total_score = 0
    scanned_books = set()
    scanned_libraries = {}
    for lib in libraries:
        elapsed_days += lib.signup
        if elapsed_days > total_num_days:
            break
        num_scanned = 0
        scanned_libraries[lib.id] = []
        for k, s in lib.books.items():
            if elapsed_days + num_scanned / lib.bpd > total_num_days:
                break
            if k not in scanned_books:
                scanned_books.add(k)
                scanned_libraries[lib.id].append(k)
                total_score += s
                num_scanned +=1
    print("Total score: {}".format(total_score))
    print(scanned_libraries)
    return scanned_libraries


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("usage: ./main.py IN_FILE OUT_FILE")
        sys.exit(1)
    parse_input_file(sys.argv[1])
    libraries.sort(key=lambda l: l.signup)
    #scanned_libraries = optimize()
    write_file(sys.argv[2])
