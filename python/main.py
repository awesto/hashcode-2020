from collections import namedtuple
import sys

Library = namedtuple('Library', ['id', 'signup', 'bpd', 'books'])


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
        fh.write('{}\n'.format(len(permutation)))
        for slide in permutation:
            fh.write(slide.id + '\n')


if __name__ == '__main__':
    print('hello')
    if len(sys.argv) < 3:
        print ("usage: ./main.py IN_FILE OUT_FILE")
        sys.exit(1)
    parse_input_file(sys.argv[1])
    write_file(sys.argv[2])
