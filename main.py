import json
from math import ceil


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def main():
    # data = []
    # with open('2021-04-03-15.json', 'r', encoding='utf-8') as f:
    #     for line in f:
    #         data.append(json.loads(line))
    #     print(json.dumps(data[0], indent=3))
    #     print(json.dumps(data[-1], indent=3))
    #
    # ids = []
    # for i in data:
    #     ids.append(int(i['id']))
    #
    # parts = list(chunks(ids, 13431))    #13431 is hard coded and will return 8 chunks
    #
    # for i in range(8):
    #     with open(F'partition0{i}.json', 'w', encoding='utf-8') as f:
    #         json.dump(data, f, ensure_ascii=False, indent=4)

    test_read = []
    for i in range(8):
        with open(F'partition0{i}.json', 'r', encoding='utf-8') as f:
            for line in f:
                test_read.append(json.loads(line))
    print(test_read)


if __name__ == '__main__':
    main()

