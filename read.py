import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv('train_2011_2012.csv', sep=';')

#data.info()
#print data.head()

columns_to_bar = ['DAY_OFF', 'WEEK_END', 'TPER_HOUR', 'ACD_COD', 'CSPL_ABNCALLS1',
            'CSPL_ABNCALLS2', 'CSPL_ABNCALLS3', 'CSPL_ABNCALLS4', 'CSPL_ABNCALLS5',
            'CSPL_ABNCALLS6', 'CSPL_ABNCALLS7', 'CSPL_ABNCALLS8', 'CSPL_ABNCALLS9',
            'CSPL_INCOMPLETE']

for column in columns_to_bar:
    data[column].value_counts(sort=False).plot.bar(title=column)
    plt.show()

"""
columns_to_hist = ['CSPL_ABNCALLS10', 'CSPL_ACCEPTABLE']

for column in columns_to_hist:
    data[column].value_counts(sort=False).plot.hist(bins=50, title=column)
    plt.show()
"""
