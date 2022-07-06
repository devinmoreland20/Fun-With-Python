if __name__ == '__main__':
    records = []
    lowscore = []
    namelist = []
for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        lowscore.append(score)
lowscore = sorted(set(lowscore))
x = lowscore[1]
for y in records:
    if x == y[1]:
        namelist.append(y[0])
namelist.sort()
for z in namelist:
    print(z)