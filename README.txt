CSC 369
Lab 1
Lana Huynh

In the first part of the lab, I created a "partone.py" to partition the json file into 8 json files. To do this, I
opened and counted the number of lines in the file. Then, I decided how many chunks I wanted to divide the partitions in.
Then, I open a new file for every partition file that I want to open and also make an index json file. In the index json
file, I have the key as the partition file number, and the values as the range of the id's.

In the second part of the lab, I asked the user to input a number that corresponds to a specific query.

In query one, I asked the user for an id number. Then, using the index json file, I searched for which partition file it
would be in. Then, I would go into that partition file and read it in line-by-line until I found the id I was looking for.

In query two, I asked the user for the minimum and maximum id number in two different inputs. Then, I checked if either
of those numbers are in the range of our partition files. If this is true then I would print out the contents of lines.

In query three, I computed the count of each event by storing the event type in a dictionary and adding 1 to its value
if it showed up.

In query four, I asked the user for the actor name. Then, for every partition file, I looked for the actor and stored
the repo name into a set to ensure that there are no duplicates. Finally, I printed every element in the set.

In query five, I asked the user for the repo name. Then, for every partition file, I looked for the repo and stored
the actor name into a set to ensure that there are no duplicates. Finally, I printed every element in the set.
