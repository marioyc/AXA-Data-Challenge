#Score: 720.9055448098
import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv('train_2011_2012.csv', sep=';')
S = set(data['ASS_ASSIGNMENT'].value_counts().axes[0])

n = data.shape[0]
sum = {}
cont = {}

for i in range(0,n):
    ass = data['ASS_ASSIGNMENT'][i]
    received = data['CSPL_RECEIVED_CALLS'][i]
    if ass in sum:
        sum[ass] += received
        cont[ass] += 1
    else:
        sum[ass] = received
        cont[ass] = 1

ans = {}

for x in S:
    #print x, sum[x], cont[x], sum[x] * 1.0 / cont[x]
    ans[x] = sum[x] * 1.0 / cont[x]

file = open('submission.txt')

lines = [line.rstrip('\n') for line in file]
lines = lines[1:]

print "DATE\tASS_ASSIGNMENT\tprediction"

for line in lines:
    tokens = line.split()
    date1 = tokens[0]
    date2 = tokens[1]
    ass_assignment = ' '.join(tokens[2:-1])
    #S.add(ass_assignment)

    print date1 + " " + date2 + "\t" + ass_assignment + "\t" + str(int(round(ans[ass_assignment])))
