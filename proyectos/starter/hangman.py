import random

with open("./data/data.txt","r", encoding="utf-8") as f:
    file = f.read()

for i in file:
    print(i)