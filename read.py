import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv('train_2011_2012.csv', sep=';')

#data.info()
#print data.head()

print data['SPLIT_COD'].value_counts().size
#print data['ACD_COD'].value_counts().size -> 1
#print data['ASS_ASSIGNMENT'].value_counts().size
S = set(data['ASS_ASSIGNMENT'].value_counts().axes[0])
print S

columns_to_barh = ['ASS_ASSIGNMENT']

for column in columns_to_barh:
    data[column].value_counts(sort=False).plot.barh(title=column)
    plt.show()
