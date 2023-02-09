import json
from math import ceil


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def main():

    test_read = []
    for i in range(8):
        with open(F'partition0{i}.json', 'r', encoding='utf-8') as f:
            for line in f:
                test_read.append(json.loads(line))
    print(test_read)


if __name__ == '__main__':
    main()

