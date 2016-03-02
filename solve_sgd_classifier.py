#Score: 814.68536428111
import pandas
from datetime import datetime, timedelta
from sklearn import linear_model
from numpy import array

data = pandas.read_csv('train_2011_2012.csv', sep=';')
n = data.shape[0]
data = data.sort_values(by=['DATE'])
labels = data['CSPL_RECEIVED_CALLS'].unique()

file = open('submission.txt')

lines = [line.rstrip('\n') for line in file]
lines = lines[1:]

submission = []

for line in lines:
    tokens = line.split()
    date1 = tokens[0].split("-")
    date2 = tokens[1].split(":")
    date = datetime(int(date1[0]),int(date1[1]),int(date1[2]),int(date2[0]),int(date2[1]))
    ass_assignment = ' '.join(tokens[2:-1])
    submission.append((date, ass_assignment))
    #print date1 + " " + date2 + "\t" + ass_assignment + "\t" + str(int(round(ans[ass_assignment])))

m = len(submission)

start_date = datetime(2011,1,1)
end_date = datetime(2012,12,28,23,30)
delta = timedelta(minutes=30)
d = start_date
pos1, pos2 = 0, 0

ass_num = {}
cont_ass = 0

for i in range(0,n):
    ass = data['ASS_ASSIGNMENT'][i]
    if ass not in ass_num:
        ass_num[ass] = cont_ass
        cont_ass += 1

#print "ass_num built"

clf = linear_model.SGDClassifier()
col_date = data['DATE']
col_assignment = data['ASS_ASSIGNMENT']
col_received = data['CSPL_RECEIVED_CALLS']

print "DATE\tASS_ASSIGNMENT\tprediction"

while pos2 < m:
    X = []
    y = []
    d = submission[pos2][0]
    d_str = "%d-%02d-%02d %02d:%02d:00.000" % (d.year, d.month, d.day, d.hour, d.minute)
    #print d_str

    while pos1 < n and col_date[pos1] <= d_str:#data.iloc[pos1]['DATE'] <= d_str:
        #ass_assignment = data.iloc[pos1]['ASS_ASSIGNMENT']
        ass_assignment = ass_num[ col_assignment[pos1] ]
        #ass_assignment = ass_num[ass_assignment]

        X.append([ass_assignment])
        y.append([ col_received[pos1] ])
        pos1 += 1

    #print pos1

    if len(X) > 0:
        X = array(X)
        y = array(y).ravel()
        clf.partial_fit(X,y,classes=labels)
    #print "fit"

    X = []
    pos3 = pos2

    while pos3 < m and submission[pos3][0] == d:
        ass_assignment = submission[pos3][1]
        X.append([ ass_num[ass_assignment] ])
        pos3 += 1

    #print pos3

    if len(X) > 0:
        X = array(X)
        y = clf.predict(X)
    #print "predicted"

    for i in range(pos2,pos3):
        print "%d-%d-%d %d:%d:00.000\t%s\t%d" % (submission[i][0].year,
            submission[i][0].month, submission[i][0].day,
            submission[i][0].hour, submission[i][0].minute, submission[i][1],
            y[i - pos2])

    pos2 = pos3
    d += delta
