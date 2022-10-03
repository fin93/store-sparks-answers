def read_1():
    f = open('di.txt', 'r')
    data = f.read()
    f.close()
    data = data.split('\n')
    for line in data:
        if line == '':
            data.remove(line)
    return data

def read_2():
    ok = []
    data = read_1()
    for line in data:
        word, definition = line.split(' ', 1)
        ok.append([word, definition])
    return ok


def write_1(data):
    f = open('di.txt', 'w')
    for line in data:
        f.write('\n' + line[0] + ' ' + line[1])
    f.close()

def append_to_data(data, question, answer):
    data.append([question, answer])
    write_1(data)
    return data

def find_relative(data, question):
    for line in data:
        if line[0] == question:
            return line[1]

def safety():
    try:
        f = open('di.txt', 'r+')
        f.write('0 0')
        f.close()
    except FileNotFoundError:
        open('di.txt', 'w')
        safety()

def main():
    while True:
        data = read_2()
        choice = input('Do you want to add an answer to question code or retrieve answer? (a/r): ').lower()
        if choice == 'a':
            code = input('Enter code, no spaces: ').lower()
            answer = input('Enter answer: ')
            data = append_to_data(data, code, answer)
        elif choice == 'r':
            code = input('Enter code: ').lower()
            data = read_2()
            print(find_relative(data, code))
        else:
            print('Invalid input')

safety()
main()