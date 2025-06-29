import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#CREATING OBJECTS/DATA
# DataFrame = multidimensional array
# Series = one dimensional arrays
s = pd.Series([1,2,3,4,5])
dates = pd.date_range('20250101', periods=6) # using pd.date_range() creates range of dates
df = pd.DataFrame(np.random.randn(6,4), index = dates, columns = list('ABCD')) # using pd.DataFrame() we pass values, indexes and columns
df2 = pd.DataFrame(
    {
        'names': pd.Series('Egor', index = list(range(5))),
        'something' : 'foo',
        'dates' : pd.date_range('20250101', periods=5),
        'array' : np.array([1,2,3,4,0])
    }
) # passing to DataFrame object where keys equal column labels and key values equal column values

#VIEWING OBJECTS/DATA
df.head()
df.tail()# DataFrame.head(n) shows n first rows of the frame, DataFrame.tail(n) shows n last rows of the Frame

df.index
df.columns# DataFrame.index shows indexes of the DataFrame, DataFrame.columns shows columns

df.to_numpy()# DataFrame.to_numpy() returns numpy array instead of DataFrame

df.describe()# DataFrame.describe() shows quick statistics fo data

df.sort_index(axis = 1, ascending = False)
df.sort_values(by='B')# DataFrame.sort_index() sorts indexes, DataFrame.sort_values() sorts values

#SELECTION
df['A']# selects all 'A' column values
df[1:4]# selects values of all columns from index 1 to index 3

# df.loc['some index']# shows rows of that index/indexes IT WORKS - df.loc[indexes wanted,[columns wanted]]

# DataFrame.iloc[indexes, columns] index row
# DataFrame.iat[index, column] gives one scalar value fast

# df[df['B'] < 0] boolean indexing shows all indexes and rows that are TRUE with statement

df3 = df.copy()
df3['E'] = ['Egor','Egor','Egor','Ksyusha','Ksyusha','Ksyusha']
df3[df3['E'].isin(['Ksyusha'])] # isin() shows indexes and columns if it has certain value/values in it

#MISSING DATA

# df.reindex(list(indexes)) remakes order of indexes inside DataFrame and if there are indexes with NAN values, shows them

# df.dropna(how='any') drops any row with NAN values

# df.fillna(n) fills NAN values with n value

# pd.isna(df) checks if value is NAN in DataFrame return True or False

#OPERATIONS

# DatFrame.sub(what to substract,axis) IT MEANS = we subtract some values from wanted axis

# DataFrame.index = DataFrame.MultiIndex.from_tuples([],names =[]) creates multiindex DataFrame

# divmod(a,b) return tuples of a//b, a%b


# STATS

my = pd.DataFrame({
    'first':[1,1,100,250],
    'second':[3,3,100,250],
    'third':[3,3,100,250],
    'fourth':[5,5,100,250],
    'fifth':[5,5,100,250],
},index=['june','july','august','september'])

# DataFrame.mean(axis) calculates meanvalue, if axis = 1 it calculates all meanvalues of indexes, otherwise - columns

# DataFrame.agg(function) adds function operations to all elements of DataFrame/ can be used to return single value per column

# DataFram.transform(func) can be used to transform each value in DataFrame

# DataFrame.value_counts() counts how many of different values there are in columns

# STRING OPERATIONS

# Series.str.lower() makes all str's in upper casebecome lowercase

# MERGE concat and join

#pd.concat([]) it merges pieces of DataFrame or Series into one

#pd.merge(a,b,on) merges a and b DataFrames or Series into one DataFrame or Series

# GROUPING

# DataFrame.gorupby(a[b]).function() a as a rows and applies function on b columns

dataframe1 = pd.DataFrame(
    {
        'city' : ['Tashkent','Moscow','Urgench','Tokyo','Seoul','Tashkent','Tashkent'],
        'population' : [1,2,1,2,2,1,1],
        'economy' : [5,10,1,10,10,5,5]
    }
)

#print(dataframe1.groupby('city')[['population','economy']].sum())

# RESHAPING

# DataFrame.stack() reshapes dataframe as below

zxc = pd.DataFrame({
    'happines' : [5,10],
    'workability' : [1,10]
}, index = ['hometown','foreigntown'])

'''
             happines  workability
hometown            5            1
foreigntown        10           10
'''
zxc.stack()
'''
hometown     happines        5
             workability     1
foreigntown  happines       10
             workability    1
'''

# DataFram.unstack() unstacks the dataframe

# PIVOT TABLES

# pd.pivot_tables(a,b,c,d,e) a = DataFrame, b = value being summarized, c = indexes, d = columns, e = function

#TIME SERIES

rng = pd.date_range("1/1/2012", periods=100, freq="s")

ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)

# DataFrame.resample(a).func() resamples DataFrame by a(seconds, hours, minutes e.t.c) and applies func

rng2 = pd.date_range('1/1/2025', periods = 6, freq = 'D')

ts2 = pd.Series(np.random.randn(len(rng2)),index = rng2)

# Series.tz_localize('UTC') localizes time for 'UTC' timezone

(ts2.tz_localize('UTC')).tz_convert('US/Eastern')

# Series.tz_convert('US/Eastern') converts according to US/Eastern timezone

rng2+pd.offsets.BusinessDay(20)

# pd.offsets.BusinessDay(a) returns a businessdays

# CATEGORICALS

zxcgg = pd.DataFrame(
    {
        'id' : [0,1,2,3,4,5],
        'grade' : ['a','b','c','d','a','b']
    }
)

new_cat = ['very good','good','bad','very bad']
zxcgg['raw_grade'] = zxcgg['grade'].astype('category')
zxcgg['raw_grade'] = zxcgg['raw_grade'].cat.rename_categories(new_cat)

'''
Here I create zxcgg dataframe for grades, then i create new category names, make grades categorised and give
these categories new names
'''

# DataFrame.sort_values('by='category') sorts values by category
(zxcgg.sort_values(by='grade'))

# DataFrame.goupby('category',observed = False).size() shows empty categories
(zxcgg.groupby('grade',observed = False).size())

#PLOTTING

# import matplotlib as plt

# Series/DataFrame.plot() plots the graph
# plt.show() shows graph
someSeries = pd.Series(np.random.randn(1000), index = pd.date_range('1/1/2025', periods=1000))
someSeries = someSeries.cumsum()
#someSeries.plot()
#plt.show()

# DataFrame.plot() shows all columns
dff = pd.DataFrame(np.random.randn(1000,4), index = pd.date_range('1/1/2025',periods = 1000), columns = ['A','B','C','D'])
#dff = dff.cumsum()
#plt.figure()
#dff.plot()
#plt.legend(loc='best')
#plt.show()

#IMPORTING AND EXPORTING DATA

# DataFrame.to_csv() creates .csv file from DataFrame
# pd.read_csv() returns csv file to python
dff2 = pd.DataFrame(np.random.randint(0,5,(10,5)))
dff2.to_csv('my.csv')
print(pd.read_csv('my.csv'))

# DataFrame.to_parquet('name') makes .parquet file
# pd.read_parquet('file') return python data
dff3 = pd.DataFrame(np.random.randint(0,5,(10,5)))
dff3.to_parquet('my.parquet')

# DataFrame.to_excel('name', sheet_name = 'sheet') creates excel
# pd.read_excel('name', 'sheetname', index_col = None`, na_values = ['NA'])
