import os
import socket
from collections import Counter

path = "/home/data/" #"/Users/sameer/Documents/dockerassignment/"
dir_list = os.listdir(path)

subs = ".txt"
res = [i for i in dir_list if subs in i]
#res.remove("result.txt")
f = open("/home/output/result.txt", "w")

total_words = 0
for i in res:
    file_path = path + i
    file = open(file_path, "rt")
    data = file.read()
    words = data.split()
    CounterVariable = Counter(words)
    most_occur = CounterVariable.most_common(3)
    total_words += len(words)
    f.write("\n\nFile name: " + i)
    f.write('\nTotal number of words in ' + i +': ' + str(len(words)))
    f.write("\nTop 3 most occurring words and their count: " + str(most_occur))
f.write("\n\nGrand total of all word counts of all the files: " + str(total_words))


hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)
f.write("\n\n\nYour Computer Name is: "+hostname)
f.write("\nYour Computer IP Address is: "+IPAddr)
f.write("\n\n")

f.close()

f = open("/home/output/result.txt", "r")
print(f.read())
f.close()