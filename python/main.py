
# def read_input(input_file):
#     with open(input_file, 'r') as file:
#         file.readline()


def write_file():
    with open('output.txt', 'w') as file:
        for i in range(1, 5):
            file.write('{}\n'.format(i))


if __name__ == '__main__':
    print('hello')
    write_file()
