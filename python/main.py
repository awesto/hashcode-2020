from collections import namedtuple
import sys

Library = namedtuple('Library', ['id', 'signup', 'bpd', 'books'])

libraries = [Library(0, 2, 2, [0, 1, 2, 3, 4]), Library(1, 3, 1, [3, 2, 5, 0])]

def parse_input_file(input_file):
    global num_libraries, num_books

    book_scores = [], library = []
    with open(input_file, 'r') as fh:
        line = fh.readline().split(' ')
        num_books, num_libraries, num_days = int(line[0]), int(line[1]), int(line[2])
        book_scores[id] = [int(s) for s in line.rstrip('\n').split(' ')]
        assert len(book_scores) == num_books
        for id in range(0, num_libraries):
            line = fh.readline().split(' ')
            Library(id, int(line[1]), int(line[1]), [])
            books = [int(s) for s in line.rstrip('\n').split(' ')]


    return scores


def write_file(filename):
    with open(filename, 'w') as fh:
        fh.write('{}\n'.format(len(libraries)))
        for lib in libraries:
            fh.write(str(lib.id) + ' ')
            fh.write(str(len(lib.books)) + '\n')
            fh.write(' '.join(map(str, lib.books)) + '\n')


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print ("usage: ./main.py IN_FILE OUT_FILE")
        sys.exit(1)
    #parse_input_file(sys.argv[1])
    write_file(sys.argv[2])
