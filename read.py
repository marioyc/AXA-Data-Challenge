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

columns_to_bar = ['ASS_ASSIGNMENT']

for column in columns_to_bar:
    data[column].value_counts(sort=False).plot.bar(title=column)
    plt.show()

"""
columns_to_hist = ['CSPL_ABNCALLS10', 'CSPL_ACCEPTABLE']

for column in columns_to_hist:
    data[column].value_counts(sort=False).plot.hist(bins=50, title=column)
    plt.show()
"""
