import json
from math import ceil


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def main():
    data = []
    with open('2021-04-03-15.json', 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))
        print(json.dumps(data[0], indent=3))
        print(json.dumps(data[-1], indent=3))

    ids = []
    for i in data:
        ids.append(int(i['id']))

    parts = list(chunks(ids, 13431))
    print(parts[5])



if __name__ == '__main__':
    main()

