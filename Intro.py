import numpy as np
import pandas as pd
#CEATING OBJECTS/DATA
#DataFrame = multidimensional array
#Series = one dimensional arrays
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

#df.loc['some index']# shows rows of that index/indexes IT WORKS - df.loc[indexes wanted,[columns wanted]]

# DataFrame.iloc[indexes, columns] shows indexes and columns
# DataFrame.iat[index, column] gives one scalar value fast

#df[df['B'] < 0] boolean indexing shows all indexes and rows that are TRUE with statement

df3 = df.copy()
df3['E'] = ['Egor','Egor','Egor','Ksyusha','Ksyusha','Ksyusha']
df3[df3['E'].isin(['Ksyusha'])] # isin() shows indexes and columns if it has certain value/values in it

#MISSING DATA

# df.reindex(list(indexes)) remakes order of indexes inside DataFrame and if there are indexes with NAN values, shows them

# df.dropna(how='any') drops any row with NAN values

# df.fillna(n) fills NAN values with n value

# pd.isna(df) checks if value is NAN in DataFrame return True or False