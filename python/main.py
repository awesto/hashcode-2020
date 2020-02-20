from collections import namedtuple
import sys

Library = namedtuple('Library', ['id', 'signup', 'bpd', 'books'])

sample_libraries = [Library(0, 2, 2, [0, 1, 2, 3, 4]), Library(1, 3, 1, [3, 2, 5, 0])]

def parse_input_file(input_file):
    global num_libraries, num_books

    libraries = []
    with open(input_file, 'r') as fh:
        line = fh.readline().rstrip('\n').split(' ')
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
            books = [book_score[b] for b in books]
            assert len(books) == int(line1[0])
            libraries.append(Library(id, int(line1[1]), int(line1[2]), books))
    return total_num_days, libraries


def write_file(filename):
    with open(filename, 'w') as fh:
        fh.write('{}\n'.format(len(libraries)))
        for lib in libraries:
            fh.write(str(lib.id) + ' ')
            fh.write(str(len(lib.books)) + '\n')
            fh.write(' '.join(map(str, lib.books)) + '\n')


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("usage: ./main.py IN_FILE OUT_FILE")
        sys.exit(1)
    total_num_days, libraries = parse_input_file(sys.argv[1])
    write_file(sys.argv[2])
