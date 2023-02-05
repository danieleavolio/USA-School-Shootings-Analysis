import pandas as pd
import pandas as pd

def check_null_values(dataframe):
  """
  This function checks for null values in a dataframe and returns a table of the columns with null values.
  """
  null_columns = dataframe.columns[dataframe.isnull().any()]
  return dataframe[null_columns].isnull().sum().to_frame(name='Null Values')

def check_duplicate_values(dataframe):
  """
  This function checks for duplicate values in a dataframe and returns a table of the number of duplicates.
  """
  return dataframe.duplicated().sum().to_frame(name='Duplicate Values')

def check_data_types(dataframe):
  """
  This function checks the data types of the columns in a dataframe and returns a table of the column names and data types.
  """
  
  data_types = {}
  for column in dataframe.columns:
    data_types[column] = dataframe[column].dtype
  return pd.DataFrame.from_dict(data_types, orient='index', columns=['Data Type'])

# Load the data into a pandas dataframe

#Read all csv files in the current folder
import glob
import pandas as pd

path = r'.' # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

# for eachfile call the functions

for df in li:
    print(check_null_values(df))
    print(check_duplicate_values(df))
    print(check_data_types(df))
