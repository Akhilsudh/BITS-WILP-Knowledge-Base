# Notebook for data preprocessing

```python
# Importing libraries
import pandas as pd
import numpy as np

# Read csv file into a pandas dataframe
df = pd.read_csv("property_data.csv")

# Take a look at the first few rows
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PID</th>
      <th>ST_NUM</th>
      <th>ST_NAME</th>
      <th>OWN_OCCUPIED</th>
      <th>NUM_BEDROOMS</th>
      <th>NUM_BATH</th>
      <th>SQ_FT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>100001000.0</td>
      <td>104.0</td>
      <td>PUTNAM</td>
      <td>Y</td>
      <td>3</td>
      <td>1.0</td>
      <td>1000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>100002000.0</td>
      <td>197.0</td>
      <td>LEXINGTON</td>
      <td>N</td>
      <td>3</td>
      <td>1.5</td>
      <td>--</td>
    </tr>
    <tr>
      <th>2</th>
      <td>100003000.0</td>
      <td>NaN</td>
      <td>LEXINGON</td>
      <td>N</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>850</td>
    </tr>
    <tr>
      <th>3</th>
      <td>100004000.0</td>
      <td>201.0</td>
      <td>BERKELEY</td>
      <td>12</td>
      <td>1</td>
      <td>NaN</td>
      <td>700</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>203.0</td>
      <td>BERKELEY</td>
      <td>Y</td>
      <td>3</td>
      <td>2.0</td>
      <td>1600</td>
    </tr>
    <tr>
      <th>5</th>
      <td>100006000.0</td>
      <td>207.0</td>
      <td>BERKELEY</td>
      <td>Y</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>800</td>
    </tr>
    <tr>
      <th>6</th>
      <td>100007000.0</td>
      <td>NaN</td>
      <td>WASHINGTON</td>
      <td>NaN</td>
      <td>2</td>
      <td>NaN</td>
      <td>950</td>
    </tr>
    <tr>
      <th>7</th>
      <td>100008000.0</td>
      <td>213.0</td>
      <td>tremont</td>
      <td>Y</td>
      <td>1</td>
      <td>1.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>100009000.0</td>
      <td>215.0</td>
      <td>TREMONT</td>
      <td>Y</td>
      <td>na</td>
      <td>2.0</td>
      <td>1800</td>
    </tr>
    <tr>
      <th>9</th>
      <td>100009000.0</td>
      <td>215.0</td>
      <td>TREMONT</td>
      <td>Y</td>
      <td>na</td>
      <td>2.0</td>
      <td>1800</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Looking at the ST_NUM column
df['ST_NUM'].isnull()
```




    0    False
    1    False
    2     True
    3    False
    4    False
    5    False
    6     True
    7    False
    8    False
    9    False
    Name: ST_NUM, dtype: bool




```python
df['ST_NUM'].isnull().sum()
```




    2




```python
# Looking at the NUM_BEDROOMS column
df['NUM_BEDROOMS'].isnull().sum()
```




    2




```python
# Making a list of missing value types
missing_values = ["n/a", "na", "--"]
df = pd.read_csv("property_data.csv", na_values = missing_values)
```


```python
# Looking at the NUM_BEDROOMS column
df['NUM_BEDROOMS'].isnull().sum()
```




    4




```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PID</th>
      <th>ST_NUM</th>
      <th>ST_NAME</th>
      <th>OWN_OCCUPIED</th>
      <th>NUM_BEDROOMS</th>
      <th>NUM_BATH</th>
      <th>SQ_FT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>100001000.0</td>
      <td>104.0</td>
      <td>PUTNAM</td>
      <td>Y</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1000.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>100002000.0</td>
      <td>197.0</td>
      <td>LEXINGTON</td>
      <td>N</td>
      <td>3.0</td>
      <td>1.5</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>100003000.0</td>
      <td>NaN</td>
      <td>LEXINGON</td>
      <td>N</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>850.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>100004000.0</td>
      <td>201.0</td>
      <td>BERKELEY</td>
      <td>12</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>700.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>203.0</td>
      <td>BERKELEY</td>
      <td>Y</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>1600.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>100006000.0</td>
      <td>207.0</td>
      <td>BERKELEY</td>
      <td>Y</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>800.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>100007000.0</td>
      <td>NaN</td>
      <td>WASHINGTON</td>
      <td>NaN</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>950.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>100008000.0</td>
      <td>213.0</td>
      <td>tremont</td>
      <td>Y</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>100009000.0</td>
      <td>215.0</td>
      <td>TREMONT</td>
      <td>Y</td>
      <td>NaN</td>
      <td>2.0</td>
      <td>1800.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>100009000.0</td>
      <td>215.0</td>
      <td>TREMONT</td>
      <td>Y</td>
      <td>NaN</td>
      <td>2.0</td>
      <td>1800.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['OWN_OCCUPIED'].isnull()
```




    0    False
    1    False
    2    False
    3    False
    4    False
    5    False
    6     True
    7    False
    8    False
    9    False
    Name: OWN_OCCUPIED, dtype: bool




```python
# Detecting numbers 
cnt=0
for row in df['OWN_OCCUPIED']:
    try:
        int(row)
        df.loc[cnt, 'OWN_OCCUPIED']=np.nan
    except ValueError:
        pass
    cnt+=1
```


```python
df['OWN_OCCUPIED'].isnull()
```




    0    False
    1    False
    2    False
    3     True
    4    False
    5    False
    6     True
    7    False
    8    False
    9    False
    Name: OWN_OCCUPIED, dtype: bool




```python
df.isnull().sum()
```




    PID             1
    ST_NUM          2
    ST_NAME         0
    OWN_OCCUPIED    2
    NUM_BEDROOMS    4
    NUM_BATH        2
    SQ_FT           2
    dtype: int64




```python
# Total number of missing value
df.isnull().sum().sum()
```




    13




```python
# Replace missing values with a number
df['ST_NUM'].fillna(125, inplace=True)
```


```python
# Location based replacement
df.loc[2,'ST_NUM'] = 125
```


```python
# Replace using median 
median = df['NUM_BEDROOMS'].median()
df['NUM_BEDROOMS'].fillna(median, inplace=True)
```


```python
df.isnull().sum()
```




    PID             1
    ST_NUM          0
    ST_NAME         0
    OWN_OCCUPIED    2
    NUM_BEDROOMS    0
    NUM_BATH        2
    SQ_FT           2
    dtype: int64




```python
# Replace using mode
df['NUM_BATH'].fillna(df['NUM_BATH'].mode()[0], inplace=True)
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PID</th>
      <th>ST_NUM</th>
      <th>ST_NAME</th>
      <th>OWN_OCCUPIED</th>
      <th>NUM_BEDROOMS</th>
      <th>NUM_BATH</th>
      <th>SQ_FT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>100001000.0</td>
      <td>104.0</td>
      <td>PUTNAM</td>
      <td>Y</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1000.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>100002000.0</td>
      <td>197.0</td>
      <td>LEXINGTON</td>
      <td>N</td>
      <td>3.0</td>
      <td>1.5</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>100003000.0</td>
      <td>125.0</td>
      <td>LEXINGON</td>
      <td>N</td>
      <td>2.5</td>
      <td>1.0</td>
      <td>850.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>100004000.0</td>
      <td>201.0</td>
      <td>BERKELEY</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>700.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>203.0</td>
      <td>BERKELEY</td>
      <td>Y</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>1600.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>100006000.0</td>
      <td>207.0</td>
      <td>BERKELEY</td>
      <td>Y</td>
      <td>2.5</td>
      <td>1.0</td>
      <td>800.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>100007000.0</td>
      <td>125.0</td>
      <td>WASHINGTON</td>
      <td>NaN</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>950.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>100008000.0</td>
      <td>213.0</td>
      <td>tremont</td>
      <td>Y</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>100009000.0</td>
      <td>215.0</td>
      <td>TREMONT</td>
      <td>Y</td>
      <td>2.5</td>
      <td>2.0</td>
      <td>1800.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>100009000.0</td>
      <td>215.0</td>
      <td>TREMONT</td>
      <td>Y</td>
      <td>2.5</td>
      <td>2.0</td>
      <td>1800.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.dtypes
```




    PID             float64
    ST_NUM          float64
    ST_NAME          object
    OWN_OCCUPIED     object
    NUM_BEDROOMS    float64
    NUM_BATH        float64
    SQ_FT           float64
    dtype: object




```python
df['OWN_OCCUPIED'].fillna('N', inplace=True)
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PID</th>
      <th>ST_NUM</th>
      <th>ST_NAME</th>
      <th>OWN_OCCUPIED</th>
      <th>NUM_BEDROOMS</th>
      <th>NUM_BATH</th>
      <th>SQ_FT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>100001000.0</td>
      <td>104.0</td>
      <td>PUTNAM</td>
      <td>Y</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1000.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>100002000.0</td>
      <td>197.0</td>
      <td>LEXINGTON</td>
      <td>N</td>
      <td>3.0</td>
      <td>1.5</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>100003000.0</td>
      <td>125.0</td>
      <td>LEXINGON</td>
      <td>N</td>
      <td>2.5</td>
      <td>1.0</td>
      <td>850.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>100004000.0</td>
      <td>201.0</td>
      <td>BERKELEY</td>
      <td>N</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>700.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>203.0</td>
      <td>BERKELEY</td>
      <td>Y</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>1600.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>100006000.0</td>
      <td>207.0</td>
      <td>BERKELEY</td>
      <td>Y</td>
      <td>2.5</td>
      <td>1.0</td>
      <td>800.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>100007000.0</td>
      <td>125.0</td>
      <td>WASHINGTON</td>
      <td>N</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>950.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>100008000.0</td>
      <td>213.0</td>
      <td>tremont</td>
      <td>Y</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>100009000.0</td>
      <td>215.0</td>
      <td>TREMONT</td>
      <td>Y</td>
      <td>2.5</td>
      <td>2.0</td>
      <td>1800.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>100009000.0</td>
      <td>215.0</td>
      <td>TREMONT</td>
      <td>Y</td>
      <td>2.5</td>
      <td>2.0</td>
      <td>1800.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Replace using mean
mean = df['SQ_FT'].mean()
df['SQ_FT'].fillna(mean, inplace=True)
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PID</th>
      <th>ST_NUM</th>
      <th>ST_NAME</th>
      <th>OWN_OCCUPIED</th>
      <th>NUM_BEDROOMS</th>
      <th>NUM_BATH</th>
      <th>SQ_FT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>100001000.0</td>
      <td>104.0</td>
      <td>PUTNAM</td>
      <td>Y</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1000.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>100002000.0</td>
      <td>197.0</td>
      <td>LEXINGTON</td>
      <td>N</td>
      <td>3.0</td>
      <td>1.5</td>
      <td>1187.5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>100003000.0</td>
      <td>125.0</td>
      <td>LEXINGON</td>
      <td>N</td>
      <td>2.5</td>
      <td>1.0</td>
      <td>850.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>100004000.0</td>
      <td>201.0</td>
      <td>BERKELEY</td>
      <td>N</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>700.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>203.0</td>
      <td>BERKELEY</td>
      <td>Y</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>1600.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>100006000.0</td>
      <td>207.0</td>
      <td>BERKELEY</td>
      <td>Y</td>
      <td>2.5</td>
      <td>1.0</td>
      <td>800.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>100007000.0</td>
      <td>125.0</td>
      <td>WASHINGTON</td>
      <td>N</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>950.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>100008000.0</td>
      <td>213.0</td>
      <td>tremont</td>
      <td>Y</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1187.5</td>
    </tr>
    <tr>
      <th>8</th>
      <td>100009000.0</td>
      <td>215.0</td>
      <td>TREMONT</td>
      <td>Y</td>
      <td>2.5</td>
      <td>2.0</td>
      <td>1800.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>100009000.0</td>
      <td>215.0</td>
      <td>TREMONT</td>
      <td>Y</td>
      <td>2.5</td>
      <td>2.0</td>
      <td>1800.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1 = df.dropna(subset=['PID'])
```


```python
df1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PID</th>
      <th>ST_NUM</th>
      <th>ST_NAME</th>
      <th>OWN_OCCUPIED</th>
      <th>NUM_BEDROOMS</th>
      <th>NUM_BATH</th>
      <th>SQ_FT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>100001000.0</td>
      <td>104.0</td>
      <td>PUTNAM</td>
      <td>Y</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1000.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>100002000.0</td>
      <td>197.0</td>
      <td>LEXINGTON</td>
      <td>N</td>
      <td>3.0</td>
      <td>1.5</td>
      <td>1187.5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>100003000.0</td>
      <td>125.0</td>
      <td>LEXINGON</td>
      <td>N</td>
      <td>2.5</td>
      <td>1.0</td>
      <td>850.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>100004000.0</td>
      <td>201.0</td>
      <td>BERKELEY</td>
      <td>N</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>700.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>100006000.0</td>
      <td>207.0</td>
      <td>BERKELEY</td>
      <td>Y</td>
      <td>2.5</td>
      <td>1.0</td>
      <td>800.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>100007000.0</td>
      <td>125.0</td>
      <td>WASHINGTON</td>
      <td>N</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>950.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>100008000.0</td>
      <td>213.0</td>
      <td>tremont</td>
      <td>Y</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1187.5</td>
    </tr>
    <tr>
      <th>8</th>
      <td>100009000.0</td>
      <td>215.0</td>
      <td>TREMONT</td>
      <td>Y</td>
      <td>2.5</td>
      <td>2.0</td>
      <td>1800.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>100009000.0</td>
      <td>215.0</td>
      <td>TREMONT</td>
      <td>Y</td>
      <td>2.5</td>
      <td>2.0</td>
      <td>1800.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.ST_NAME.unique()
```




    array(['PUTNAM', 'LEXINGTON', 'LEXINGON', 'BERKELEY', 'WASHINGTON',
           'tremont', 'TREMONT'], dtype=object)




```python
df1["ST_NAME"] = df1["ST_NAME"].apply(lambda x: x.replace("LEXINGON", "LEXINGTON"))
df1["ST_NAME"] = df1["ST_NAME"].apply(lambda x: x.upper())
```

    <ipython-input-27-3a1ae30bd232>:1: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      df1["ST_NAME"] = df1["ST_NAME"].apply(lambda x: x.replace("LEXINGON", "LEXINGTON"))
    <ipython-input-27-3a1ae30bd232>:2: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      df1["ST_NAME"] = df1["ST_NAME"].apply(lambda x: x.upper())
    


```python
df1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PID</th>
      <th>ST_NUM</th>
      <th>ST_NAME</th>
      <th>OWN_OCCUPIED</th>
      <th>NUM_BEDROOMS</th>
      <th>NUM_BATH</th>
      <th>SQ_FT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>100001000.0</td>
      <td>104.0</td>
      <td>PUTNAM</td>
      <td>Y</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1000.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>100002000.0</td>
      <td>197.0</td>
      <td>LEXINGTON</td>
      <td>N</td>
      <td>3.0</td>
      <td>1.5</td>
      <td>1187.5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>100003000.0</td>
      <td>125.0</td>
      <td>LEXINGTON</td>
      <td>N</td>
      <td>2.5</td>
      <td>1.0</td>
      <td>850.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>100004000.0</td>
      <td>201.0</td>
      <td>BERKELEY</td>
      <td>N</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>700.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>100006000.0</td>
      <td>207.0</td>
      <td>BERKELEY</td>
      <td>Y</td>
      <td>2.5</td>
      <td>1.0</td>
      <td>800.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>100007000.0</td>
      <td>125.0</td>
      <td>WASHINGTON</td>
      <td>N</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>950.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>100008000.0</td>
      <td>213.0</td>
      <td>TREMONT</td>
      <td>Y</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1187.5</td>
    </tr>
    <tr>
      <th>8</th>
      <td>100009000.0</td>
      <td>215.0</td>
      <td>TREMONT</td>
      <td>Y</td>
      <td>2.5</td>
      <td>2.0</td>
      <td>1800.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>100009000.0</td>
      <td>215.0</td>
      <td>TREMONT</td>
      <td>Y</td>
      <td>2.5</td>
      <td>2.0</td>
      <td>1800.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.drop_duplicates(keep='last')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PID</th>
      <th>ST_NUM</th>
      <th>ST_NAME</th>
      <th>OWN_OCCUPIED</th>
      <th>NUM_BEDROOMS</th>
      <th>NUM_BATH</th>
      <th>SQ_FT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>100001000.0</td>
      <td>104.0</td>
      <td>PUTNAM</td>
      <td>Y</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1000.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>100002000.0</td>
      <td>197.0</td>
      <td>LEXINGTON</td>
      <td>N</td>
      <td>3.0</td>
      <td>1.5</td>
      <td>1187.5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>100003000.0</td>
      <td>125.0</td>
      <td>LEXINGTON</td>
      <td>N</td>
      <td>2.5</td>
      <td>1.0</td>
      <td>850.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>100004000.0</td>
      <td>201.0</td>
      <td>BERKELEY</td>
      <td>N</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>700.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>100006000.0</td>
      <td>207.0</td>
      <td>BERKELEY</td>
      <td>Y</td>
      <td>2.5</td>
      <td>1.0</td>
      <td>800.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>100007000.0</td>
      <td>125.0</td>
      <td>WASHINGTON</td>
      <td>N</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>950.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>100008000.0</td>
      <td>213.0</td>
      <td>TREMONT</td>
      <td>Y</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1187.5</td>
    </tr>
    <tr>
      <th>9</th>
      <td>100009000.0</td>
      <td>215.0</td>
      <td>TREMONT</td>
      <td>Y</td>
      <td>2.5</td>
      <td>2.0</td>
      <td>1800.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1['ST_NUM'] = df1['ST_NUM'].astype(str)
```

    <ipython-input-30-09fc6084589a>:1: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      df1['ST_NUM'] = df1['ST_NUM'].astype(str)
    


```python
df1.dtypes
```




    PID             float64
    ST_NUM           object
    ST_NAME          object
    OWN_OCCUPIED     object
    NUM_BEDROOMS    float64
    NUM_BATH        float64
    SQ_FT           float64
    dtype: object



---
Tags: [[!AMLIndex]]