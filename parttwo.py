import json
from collections import OrderedDict

def open_index() -> dict:
    with open("index.json", 'r') as f:
        dic = json.loads(f.readline())
        return dic

def main():
    user = int(input("What would you like to do? (in number)\n"))

    if user == 1:
        num_lines = 0

        input_id = input("Gimme your id :D\n")
        dic = open_index()

        for i in range(8):
            rang = dic[str(i)]

            # if input id is in the partition and cast strings to ints :)
            if int(rang[0]) <= int(input_id) <= int(rang[1]):
                with open(F"partition0{i}.json", 'r') as g:
                    for line in g:
                        num_lines += 1
                        lin = json.loads(line)
                        if lin["id"] == input_id:
                            print(json.dumps(lin, indent=4))
                            break

        print("Count of partition files: 1")
        print(f"Count of lines: {num_lines}")


    elif user == 2:
        input_start = input("Gimme your min :)\n")
        input_end = input("Gimme your max :0\n")

        num_partitions = 0
        num_lines = 0

        dic = open_index()

        for i in range(8):
            # rang is the range of each partition file keys
            rang = dic[str(i)]

            # if input id is in the partition and cast strings to ints :)
            if int(rang[0]) <= int(input_start) <= int(rang[1]) or int(rang[0]) <= int(input_end) <= int(rang[1]):
                with open(F"partition0{i}.json", 'r') as g:
                    num_partitions += 1

                    for line in g:
                        num_lines += 1
                        lin = json.loads(line)
                        if int(input_start) <= int(lin["id"]) <= int(input_end):
                            print(json.dumps(lin, indent=4))
                        if int(lin["id"]) == int(input_end):
                            break


        print(f"Count of partition files: {num_partitions}")
        print(f"Count of lines: {num_lines}")

    elif user == 3:
        num_partitions = 0
        num_lines = 0

        events = OrderedDict()

        for i in range(8):
            with open(F"partition0{i}.json", 'r') as f:
                num_partitions += 1
                for line in f:
                    num_lines += 1
                    lin = json.loads(line)
                    event = lin['type']
                    if event not in events.keys():
                        events[event] = 0
                    events[event] = events[event] + 1

        sorted_events = sorted(events.items(), key=lambda x: x[1], reverse=True)

        for event in sorted_events:
            print(event)

        print() # printing ONE new line for formatting :)))
        print(f"Count of partition files: {num_partitions}")
        print(f"Count of lines: {num_lines}")


    elif user == 4:
        input_actor = input("Gimme your actor name :-)\n")

        num_partitions = 0
        num_lines = 0

        actor = set()

        for i in range(8):
            with open(F"partition0{i}.json", 'r') as g:
                num_partitions += 1
                for line in g:
                    num_lines += 1
                    lin = json.loads(line)
                    if lin['actor']['display_login'] == input_actor:
                        actor.add(lin['repo']['name'])
        for a in actor:
            print(a)
        print()
        print(f"Count of partition files: {num_partitions}")
        print(f"Count of lines: {num_lines}")


    elif user == 5:
        input_repo = input("Gimme your repo name :o\n")

        num_partitions = 0
        num_lines = 0

        name = set()

        for i in range(8):
            with open(F"partition0{i}.json", 'r') as g:
                num_partitions += 1
                for line in g:
                    num_lines += 1
                    lin = json.loads(line)
                    if lin['repo']['name'] == input_repo:
                        name.add(lin['actor']['display_login'])
        for n in name:
            print(n)
        print()
        print(f"Count of partition files: {num_partitions}")
        print(f"Count of lines: {num_lines}")


if __name__ == '__main__':
    main()