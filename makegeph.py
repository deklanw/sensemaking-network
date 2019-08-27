import csv
from fuzzywuzzy import fuzz
from itertools import combinations


def do():
    podcast_list = []
    guest_dict = {}
    all_guests = set()

    with open("rawdata.txt", encoding="utf8") as f:
        for line in f:
            line = line.strip()
            stuff = line.split(';')
            podcast_name = stuff[0]
            guests = stuff[1].split(', ')
            guest_set = set(guests)
            all_guests = all_guests.union(guest_set)
            podcast_list.append((podcast_name, guest_set))

            for guest in guests:
                if guest in guest_dict:
                    guest_dict[guest] = guest_dict[guest].union(
                        {podcast_name})
                else:
                    guest_dict[guest] = {podcast_name}

    with open("guest_nodes.csv", "w", encoding="utf8", newline="") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(["Source", "Target", "Type", "Label"])

        for (guest1, guest2) in combinations(all_guests, 2):
            for something in guest_dict[guest1].intersection(guest_dict[guest2]):
                csvwriter.writerow([guest1, guest2, "undirected", something])

    with open("podcast_nodes.csv", "w", encoding="utf8", newline="") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(["Source", "Target", "Type", "Label"])

        for (podcast1, podcast2) in combinations(podcast_list, 2):
            for guest1 in podcast1[1]:
                for guest2 in podcast2[1]:
                    if guest1 == guest2:
                        csvwriter.writerow(
                            [podcast1[0], podcast2[0], "undirected", guest1])
                    # elif fuzz.ratio(guest1, guest2) > 80:
                    #     print("Suspicious ", guest1, guest2)


do()
