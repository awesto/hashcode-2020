from collections import namedtuple
import sys

Library = namedtuple('Library', ['id', 'signup', 'bpd', 'books'])


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
            books = [book_score[b] for b in books]
            assert len(books) == int(line1[0])
            libraries.append(Library(id, int(line1[1]), int(line1[2]), books))
    return total_num_days, libraries


def write_file(filename):
    with open(filename, 'w') as fh:
        fh.write('{}\n'.format(len(libraries)))
        for lib in libraries:
            fh.write('{}\n'.format(lib.id))


if __name__ == '__main__':
    print('hello')
    if len(sys.argv) < 3:
        print ("usage: ./main.py IN_FILE OUT_FILE")
        sys.exit(1)
    parse_input_file(sys.argv[1])
    write_file(sys.argv[2])
