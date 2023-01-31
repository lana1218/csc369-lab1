import json


def main():
    user = input('Please enter file name (ex. name.json): ')

    with open(user, 'r', encoding='utf-8') as f:
        num_lines = sum(1 for line in f)  # count the number of lines
        num_in_chunks = num_lines // 8

        f.seek(0)

        dic = {}

        for i in range(8):
            with open(f'partition0{i}.json', 'w', encoding='utf-8') as g:
                a = 0
                for line in f:
                    if a == 0:
                        # grab first id of partition
                        first = line['id']

                    if a != num_in_chunks:
                        lin = json.loads(line)
                        json.dump(lin, g, ensure_ascii=False)
                        g.write("\n")
                        a += 1

                    else:
                        # grab last id of partition
                        last = line['id']

                        # add first and last to dic :)
                        dic[i] = [first, last]

                        break

    # make index.json file
    with open("index.json", 'w') as i:
        json.dump(dic, i)


if __name__ == '__main__':
    main() #2021-04-03-15.json
