# Notebook for data cleaning
Reference: https://www.justintodata.com/data-cleaning-techniques-python-guide/#what-is-data-cleaning-and-why-is-it-important

<u><b>Data Cleaning</b></u>: Data cleansing or data cleaning is the process of detecting and correcting (or removing) corrupt or inaccurate records from a record set, table, or database and refers to identifying incomplete, incorrect, inaccurate or irrelevant parts of the data and then replacing, modifying, or deleting the dirty or coarse data.

<ul>Methods & techniques in Python on how to find and clean:
<li>Missing data
<li>Irregular data (outliers)
<li>Unnecessary data — repetitive data, duplicates, and more
<li>Inconsistent data — capitalization, data types, typos, addresses

Raw data is always messy, may suffer from various quality issues. We can't use it as it is. If you use such data for analysis, for example, feed into a machine learning model, you’ll get useless insights most of the time. That’s why data cleansing is a critical process for data analysts and data scientists.

<ul><u><b> Useful Python Libraries </b></u>
    <li><b>pandas:</b> a popular data analysis and manipulation tool, which will be used for most of our data cleaning techniques
    <li><b>seaborn:</b> statistical data visualization library

<li> <b>Missingno</b> Python library that provides a series of visualisations to understand the presence and distribution of missing data within a pandas dataframe. 
    <li><b> nltk:</b> natural language toolkit   

<b><u>Case Study</u> -->  Russian housing market dataset</b>
The goal of the project is to predict housing prices.


```python
import pandas as pd
df = pd.read_csv("sberbank-russian-housing-market/train/train.csv")
df.head()
df.shape
```




    (30471, 292)



There are 292 columns and 30471 rows in the data set


```python
# to check datatypes 
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 30471 entries, 0 to 30470
    Columns: 292 entries, id to price_doc
    dtypes: float64(119), int64(157), object(16)
    memory usage: 67.9+ MB
    


```python
# to identify numeric and non-numeric attributes in the dataset
numeric_cols = df.select_dtypes(include=['number']).columns
non_numeric_cols = df.select_dtypes(exclude=['number']).columns
```


```python
numeric_cols
```




    Index(['id', 'full_sq', 'life_sq', 'floor', 'max_floor', 'material',
           'build_year', 'num_room', 'kitch_sq', 'state',
           ...
           'cafe_count_5000_price_2500', 'cafe_count_5000_price_4000',
           'cafe_count_5000_price_high', 'big_church_count_5000',
           'church_count_5000', 'mosque_count_5000', 'leisure_count_5000',
           'sport_count_5000', 'market_count_5000', 'price_doc'],
          dtype='object', length=276)




```python
non_numeric_cols
```




    Index(['timestamp', 'product_type', 'sub_area', 'culture_objects_top_25',
           'thermal_power_plant_raion', 'incineration_raion',
           'oil_chemistry_raion', 'radiation_raion', 'railroad_terminal_raion',
           'big_market_raion', 'nuclear_reactor_raion', 'detention_facility_raion',
           'water_1line', 'big_road1_1line', 'railroad_1line', 'ecology'],
          dtype='object')



# Missing Data

<ul>When data is missing for a column in a row. Ways to handle it:
 <li>   <b><u> How to find out? </u></b>
    <li> <b> Method #1: missing data (by columns) count & percentage</b>
        


```python
df[non_numeric_cols].info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 30471 entries, 0 to 30470
    Data columns (total 16 columns):
     #   Column                     Non-Null Count  Dtype 
    ---  ------                     --------------  ----- 
     0   timestamp                  30471 non-null  object
     1   product_type               30471 non-null  object
     2   sub_area                   30471 non-null  object
     3   culture_objects_top_25     30471 non-null  object
     4   thermal_power_plant_raion  30471 non-null  object
     5   incineration_raion         30471 non-null  object
     6   oil_chemistry_raion        30471 non-null  object
     7   radiation_raion            30471 non-null  object
     8   railroad_terminal_raion    30471 non-null  object
     9   big_market_raion           30471 non-null  object
     10  nuclear_reactor_raion      30471 non-null  object
     11  detention_facility_raion   30471 non-null  object
     12  water_1line                30471 non-null  object
     13  big_road1_1line            30471 non-null  object
     14  railroad_1line             30471 non-null  object
     15  ecology                    30471 non-null  object
    dtypes: object(16)
    memory usage: 3.7+ MB
    

all counts are same for non-numeric columns, hence no missing data


```python
num_missing = df.isna().sum()
num_missing[:10]
```




    id                0
    timestamp         0
    full_sq           0
    life_sq        6383
    floor           167
    max_floor      9572
    material       9572
    build_year    13605
    num_room       9572
    kitch_sq       9572
    dtype: int64




```python
# to caclulate mean of missing values by columns
num_missing = df.isna().mean()
num_missing[:10]
```




    id            0.000000
    timestamp     0.000000
    full_sq       0.000000
    life_sq       0.209478
    floor         0.005481
    max_floor     0.314135
    material      0.314135
    build_year    0.446490
    num_room      0.314135
    kitch_sq      0.314135
    dtype: float64



 <li> <b> Method #2: missing data (by columns) heatmap </b>


```python
# to visualise missing values
# heapmap can be created using "seaborn" and "missingno" libraries
import seaborn as sns

# since number of columns are very large, it would be difficult to visualise them at the same time. We can learn the patter
# pattern of missing data for the first 30 columns
cols= df.columns[:30]
colors = ["green", "blue"]
sns.heatmap(df[cols].isna(), cmap=sns.color_palette(colors))
```




    <matplotlib.axes._subplots.AxesSubplot at 0x24be7d5e520>




    
![[Assets/DataVisualizationNotebook/output_19_1.png]]
    


the column life_sq has missing values across different rows. While the column max_floor has most of its missing values 

# missingno
The missingno library is a small toolset focused on missing data visualizations and utilities. So you can get the same missing data heatmap as above with shorter code.


```python

!pip install missingno
import missingno as msno
msno.matrix(df.iloc[:, :30])
```

    Requirement already satisfied: missingno in c:\users\bits-wilp\anaconda3\lib\site-packages (0.5.0)
    Requirement already satisfied: matplotlib in c:\users\bits-wilp\anaconda3\lib\site-packages (from missingno) (3.2.2)
    Requirement already satisfied: numpy in c:\users\bits-wilp\anaconda3\lib\site-packages (from missingno) (1.18.5)
    Requirement already satisfied: scipy in c:\users\bits-wilp\anaconda3\lib\site-packages (from missingno) (1.5.0)
    Requirement already satisfied: seaborn in c:\users\bits-wilp\anaconda3\lib\site-packages (from missingno) (0.10.1)
    Requirement already satisfied: kiwisolver>=1.0.1 in c:\users\bits-wilp\anaconda3\lib\site-packages (from matplotlib->missingno) (1.2.0)
    Requirement already satisfied: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.1 in c:\users\bits-wilp\anaconda3\lib\site-packages (from matplotlib->missingno) (2.4.7)
    Requirement already satisfied: cycler>=0.10 in c:\users\bits-wilp\anaconda3\lib\site-packages (from matplotlib->missingno) (0.10.0)
    Requirement already satisfied: python-dateutil>=2.1 in c:\users\bits-wilp\anaconda3\lib\site-packages (from matplotlib->missingno) (2.8.1)
    Requirement already satisfied: pandas>=0.22.0 in c:\users\bits-wilp\anaconda3\lib\site-packages (from seaborn->missingno) (1.0.5)
    Requirement already satisfied: six in c:\users\bits-wilp\anaconda3\lib\site-packages (from cycler>=0.10->matplotlib->missingno) (1.15.0)
    Requirement already satisfied: pytz>=2017.2 in c:\users\bits-wilp\anaconda3\lib\site-packages (from pandas>=0.22.0->seaborn->missingno) (2020.1)
    




    <matplotlib.axes._subplots.AxesSubplot at 0x24be8bc6310>




    
![[output_22_2.png]]
    


<li> <b> Method #3: missing data (by rows) histogram </b>
    <li> summarize the missing data by rows.


```python
missing_by_row = df.isna().sum(axis='columns')
missing_by_row.hist(bins=50)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x24be8e1c610>




    
![[Assets/DataVisualizationNotebook/output_24_1.png]]
    


This histogram helps to identify the missing patterns among the 30,471 observations. For example, there are over 6,000 observations with no missing values, and close to 4,000 observations with 1 missing value.

<ul> <b> How to handle missing data </b>
    <li> Methods:
    <li> <b>Technique #1:</b> drop columns / features: drop the entire column or features with large number of missing values. But, this will cause a loss of information. Let’s consider the columns with a high percentage of missing.


```python
num_missing[num_missing > 0.3]
```




    max_floor                     0.314135
    material                      0.314135
    build_year                    0.446490
    num_room                      0.314135
    kitch_sq                      0.314135
    state                         0.444980
    hospital_beds_raion           0.473926
    cafe_sum_500_min_price_avg    0.435857
    cafe_sum_500_max_price_avg    0.435857
    cafe_avg_price_500            0.435857
    dtype: float64




```python
df.drop(['max_floor', 'material', 'build_year', 'num_room', 'kitch_sq','state','hospital_beds_raion', 'cafe_sum_500_min_price_avg','cafe_sum_500_max_price_avg', 'cafe_avg_price_500'],axis = 1)
df.head()
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
      <th>id</th>
      <th>timestamp</th>
      <th>full_sq</th>
      <th>life_sq</th>
      <th>floor</th>
      <th>max_floor</th>
      <th>material</th>
      <th>build_year</th>
      <th>num_room</th>
      <th>kitch_sq</th>
      <th>...</th>
      <th>cafe_count_5000_price_2500</th>
      <th>cafe_count_5000_price_4000</th>
      <th>cafe_count_5000_price_high</th>
      <th>big_church_count_5000</th>
      <th>church_count_5000</th>
      <th>mosque_count_5000</th>
      <th>leisure_count_5000</th>
      <th>sport_count_5000</th>
      <th>market_count_5000</th>
      <th>price_doc</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2011-08-20</td>
      <td>43</td>
      <td>27.0</td>
      <td>4.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>9</td>
      <td>4</td>
      <td>0</td>
      <td>13</td>
      <td>22</td>
      <td>1</td>
      <td>0</td>
      <td>52</td>
      <td>4</td>
      <td>5850000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>2011-08-23</td>
      <td>34</td>
      <td>19.0</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>15</td>
      <td>3</td>
      <td>0</td>
      <td>15</td>
      <td>29</td>
      <td>1</td>
      <td>10</td>
      <td>66</td>
      <td>14</td>
      <td>6000000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>2011-08-27</td>
      <td>43</td>
      <td>29.0</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>10</td>
      <td>3</td>
      <td>0</td>
      <td>11</td>
      <td>27</td>
      <td>0</td>
      <td>4</td>
      <td>67</td>
      <td>10</td>
      <td>5700000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>2011-09-01</td>
      <td>89</td>
      <td>50.0</td>
      <td>9.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>11</td>
      <td>2</td>
      <td>1</td>
      <td>4</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>26</td>
      <td>3</td>
      <td>13100000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>2011-09-05</td>
      <td>77</td>
      <td>77.0</td>
      <td>4.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>319</td>
      <td>108</td>
      <td>17</td>
      <td>135</td>
      <td>236</td>
      <td>2</td>
      <td>91</td>
      <td>195</td>
      <td>14</td>
      <td>16331452</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 292 columns</p>
</div>



<li><b> Technique #2: drop rows / observations</b>


```python
df.dropna(axis=0, how='any', thresh=257, subset=None, inplace=True)
# thresh argument that specifies the number of non-missing values that should be present for each row in order not to be dropped.
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
      <th>id</th>
      <th>timestamp</th>
      <th>full_sq</th>
      <th>life_sq</th>
      <th>floor</th>
      <th>max_floor</th>
      <th>material</th>
      <th>build_year</th>
      <th>num_room</th>
      <th>kitch_sq</th>
      <th>...</th>
      <th>cafe_count_5000_price_2500</th>
      <th>cafe_count_5000_price_4000</th>
      <th>cafe_count_5000_price_high</th>
      <th>big_church_count_5000</th>
      <th>church_count_5000</th>
      <th>mosque_count_5000</th>
      <th>leisure_count_5000</th>
      <th>sport_count_5000</th>
      <th>market_count_5000</th>
      <th>price_doc</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2011-08-20</td>
      <td>43</td>
      <td>27.0</td>
      <td>4.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>9</td>
      <td>4</td>
      <td>0</td>
      <td>13</td>
      <td>22</td>
      <td>1</td>
      <td>0</td>
      <td>52</td>
      <td>4</td>
      <td>5850000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>2011-08-23</td>
      <td>34</td>
      <td>19.0</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>15</td>
      <td>3</td>
      <td>0</td>
      <td>15</td>
      <td>29</td>
      <td>1</td>
      <td>10</td>
      <td>66</td>
      <td>14</td>
      <td>6000000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>2011-08-27</td>
      <td>43</td>
      <td>29.0</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>10</td>
      <td>3</td>
      <td>0</td>
      <td>11</td>
      <td>27</td>
      <td>0</td>
      <td>4</td>
      <td>67</td>
      <td>10</td>
      <td>5700000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>2011-09-01</td>
      <td>89</td>
      <td>50.0</td>
      <td>9.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>11</td>
      <td>2</td>
      <td>1</td>
      <td>4</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>26</td>
      <td>3</td>
      <td>13100000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>2011-09-05</td>
      <td>77</td>
      <td>77.0</td>
      <td>4.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>319</td>
      <td>108</td>
      <td>17</td>
      <td>135</td>
      <td>236</td>
      <td>2</td>
      <td>91</td>
      <td>195</td>
      <td>14</td>
      <td>16331452</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>30466</th>
      <td>30469</td>
      <td>2015-06-30</td>
      <td>44</td>
      <td>27.0</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>1975.0</td>
      <td>2.0</td>
      <td>6.0</td>
      <td>...</td>
      <td>15</td>
      <td>5</td>
      <td>0</td>
      <td>15</td>
      <td>26</td>
      <td>1</td>
      <td>2</td>
      <td>84</td>
      <td>6</td>
      <td>7400000</td>
    </tr>
    <tr>
      <th>30467</th>
      <td>30470</td>
      <td>2015-06-30</td>
      <td>86</td>
      <td>59.0</td>
      <td>3.0</td>
      <td>9.0</td>
      <td>2.0</td>
      <td>1935.0</td>
      <td>4.0</td>
      <td>10.0</td>
      <td>...</td>
      <td>313</td>
      <td>128</td>
      <td>24</td>
      <td>98</td>
      <td>182</td>
      <td>1</td>
      <td>82</td>
      <td>171</td>
      <td>15</td>
      <td>25000000</td>
    </tr>
    <tr>
      <th>30468</th>
      <td>30471</td>
      <td>2015-06-30</td>
      <td>45</td>
      <td>NaN</td>
      <td>10.0</td>
      <td>20.0</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>12</td>
      <td>0</td>
      <td>1</td>
      <td>11</td>
      <td>1</td>
      <td>6970959</td>
    </tr>
    <tr>
      <th>30469</th>
      <td>30472</td>
      <td>2015-06-30</td>
      <td>64</td>
      <td>32.0</td>
      <td>5.0</td>
      <td>15.0</td>
      <td>1.0</td>
      <td>2003.0</td>
      <td>2.0</td>
      <td>11.0</td>
      <td>...</td>
      <td>22</td>
      <td>1</td>
      <td>1</td>
      <td>6</td>
      <td>31</td>
      <td>1</td>
      <td>4</td>
      <td>65</td>
      <td>7</td>
      <td>13500000</td>
    </tr>
    <tr>
      <th>30470</th>
      <td>30473</td>
      <td>2015-06-30</td>
      <td>43</td>
      <td>28.0</td>
      <td>1.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>1968.0</td>
      <td>2.0</td>
      <td>6.0</td>
      <td>...</td>
      <td>5</td>
      <td>2</td>
      <td>0</td>
      <td>7</td>
      <td>16</td>
      <td>0</td>
      <td>9</td>
      <td>54</td>
      <td>10</td>
      <td>5600000</td>
    </tr>
  </tbody>
</table>
<p>29779 rows × 292 columns</p>
</div>



<li> <b> Technique #3: impute the missing with constant values.</b>


```python
df_copy = df.copy()
numeric_cols = df_copy.select_dtypes(include=['number']).columns
df_copy[numeric_cols] = df_copy[numeric_cols].fillna(-999)
df_copy[non_numeric_cols] = df_copy[non_numeric_cols].fillna('_MISSING_')

```

<li> <b> Technique #4: impute the missing with statistics </b>
    


```python
#imputing numeric columns by median
med = df_copy[numeric_cols].median()
df_copy[numeric_cols] = df_copy[numeric_cols].fillna(med)
```


```python
# imputing non-numeric columns by mode
most_freq = df_copy[non_numeric_cols].mode()
df_copy[non_numeric_cols] = df_copy[non_numeric_cols].fillna(most_freq)
```


```python
most_freq
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
      <th>timestamp</th>
      <th>product_type</th>
      <th>sub_area</th>
      <th>culture_objects_top_25</th>
      <th>thermal_power_plant_raion</th>
      <th>incineration_raion</th>
      <th>oil_chemistry_raion</th>
      <th>radiation_raion</th>
      <th>railroad_terminal_raion</th>
      <th>big_market_raion</th>
      <th>nuclear_reactor_raion</th>
      <th>detention_facility_raion</th>
      <th>water_1line</th>
      <th>big_road1_1line</th>
      <th>railroad_1line</th>
      <th>ecology</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2014-12-16</td>
      <td>Investment</td>
      <td>Poselenie Sosenskoe</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>poor</td>
    </tr>
  </tbody>
</table>
</div>




```python
#to check for missing values
df_copy.isna().sum()
```




    id                    0
    timestamp             0
    full_sq               0
    life_sq               0
    floor                 0
                         ..
    mosque_count_5000     0
    leisure_count_5000    0
    sport_count_5000      0
    market_count_5000     0
    price_doc             0
    Length: 292, dtype: int64



# Irregular data (outliers)

Outliers could bias our data analysis results, providing a misleading representation of the data. Outliers could be real outliers or mistakes.

<ul><b> How to detect? </b>
<li><b> Method #1: descriptive statistics </b>


```python
df_copy.describe()
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
      <th>id</th>
      <th>full_sq</th>
      <th>life_sq</th>
      <th>floor</th>
      <th>max_floor</th>
      <th>material</th>
      <th>build_year</th>
      <th>num_room</th>
      <th>kitch_sq</th>
      <th>state</th>
      <th>...</th>
      <th>big_church_count_5000</th>
      <th>church_count_5000</th>
      <th>mosque_count_5000</th>
      <th>leisure_count_5000</th>
      <th>sport_count_5000</th>
      <th>market_count_5000</th>
      <th>price_doc</th>
      <th>year</th>
      <th>month</th>
      <th>weekday</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>2.977900e+04</td>
      <td>2.977900e+04</td>
      <td>2.977900e+04</td>
      <td>2.977900e+04</td>
      <td>2.977900e+04</td>
      <td>2.977900e+04</td>
      <td>2.977900e+04</td>
      <td>2.977900e+04</td>
      <td>2.977900e+04</td>
      <td>2.977900e+04</td>
      <td>...</td>
      <td>2.977900e+04</td>
      <td>2.977900e+04</td>
      <td>2.977900e+04</td>
      <td>2.977900e+04</td>
      <td>2.977900e+04</td>
      <td>2.977900e+04</td>
      <td>2.977900e+04</td>
      <td>29779.000000</td>
      <td>29779.000000</td>
      <td>29779.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>3.927294e-17</td>
      <td>1.133705e-15</td>
      <td>-6.050975e-16</td>
      <td>-3.694486e-15</td>
      <td>-3.424010e-14</td>
      <td>2.521536e-16</td>
      <td>6.337155e-16</td>
      <td>1.510536e-13</td>
      <td>-2.153204e-13</td>
      <td>1.240557e-13</td>
      <td>...</td>
      <td>1.864436e-15</td>
      <td>-1.152501e-16</td>
      <td>-2.969346e-15</td>
      <td>1.061662e-15</td>
      <td>-3.434236e-16</td>
      <td>3.142879e-17</td>
      <td>3.015190e-15</td>
      <td>2013.453105</td>
      <td>6.744014</td>
      <td>2.196783</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.000017e+00</td>
      <td>1.000017e+00</td>
      <td>1.000017e+00</td>
      <td>1.000017e+00</td>
      <td>1.000017e+00</td>
      <td>1.000017e+00</td>
      <td>1.000017e+00</td>
      <td>1.000017e+00</td>
      <td>1.000017e+00</td>
      <td>1.000017e+00</td>
      <td>...</td>
      <td>1.000017e+00</td>
      <td>1.000017e+00</td>
      <td>1.000017e+00</td>
      <td>1.000017e+00</td>
      <td>1.000017e+00</td>
      <td>1.000017e+00</td>
      <td>1.000017e+00</td>
      <td>0.962059</td>
      <td>3.523263</td>
      <td>1.576159</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-1.733558e+00</td>
      <td>-1.413996e+00</td>
      <td>-2.004501e+00</td>
      <td>-1.344496e+01</td>
      <td>-1.484404e+00</td>
      <td>-1.484503e+00</td>
      <td>-1.975412e-02</td>
      <td>-1.484507e+00</td>
      <td>-1.482597e+00</td>
      <td>-1.130673e+00</td>
      <td>...</td>
      <td>-5.234219e-01</td>
      <td>-6.453354e-01</td>
      <td>-7.320273e-01</td>
      <td>-4.259748e-01</td>
      <td>-1.165510e+00</td>
      <td>-1.251928e+00</td>
      <td>-1.477355e+00</td>
      <td>2011.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-8.634904e-01</td>
      <td>-4.234363e-01</td>
      <td>4.506506e-01</td>
      <td>1.039594e-02</td>
      <td>-1.484404e+00</td>
      <td>-1.484503e+00</td>
      <td>-1.975412e-02</td>
      <td>-1.484507e+00</td>
      <td>-1.482597e+00</td>
      <td>-1.130673e+00</td>
      <td>...</td>
      <td>-4.553321e-01</td>
      <td>-4.568299e-01</td>
      <td>-7.320273e-01</td>
      <td>-4.259748e-01</td>
      <td>-9.059867e-01</td>
      <td>-1.046875e+00</td>
      <td>-4.935775e-01</td>
      <td>2013.000000</td>
      <td>4.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>1.914127e-03</td>
      <td>-1.366954e-01</td>
      <td>4.748155e-01</td>
      <td>6.410995e-02</td>
      <td>6.657718e-01</td>
      <td>6.718609e-01</td>
      <td>5.709977e-03</td>
      <td>6.716512e-01</td>
      <td>6.609854e-01</td>
      <td>8.821739e-01</td>
      <td>...</td>
      <td>-2.851076e-01</td>
      <td>-3.102146e-01</td>
      <td>-7.320273e-01</td>
      <td>-3.297071e-01</td>
      <td>-1.057884e-01</td>
      <td>-2.266611e-01</td>
      <td>-1.863383e-01</td>
      <td>2014.000000</td>
      <td>6.000000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>8.653282e-01</td>
      <td>2.282476e-01</td>
      <td>5.013968e-01</td>
      <td>1.178240e-01</td>
      <td>6.807036e-01</td>
      <td>6.718609e-01</td>
      <td>5.916512e-03</td>
      <td>6.738074e-01</td>
      <td>6.759905e-01</td>
      <td>8.841867e-01</td>
      <td>...</td>
      <td>-1.148831e-01</td>
      <td>-5.887390e-02</td>
      <td>9.015939e-01</td>
      <td>-8.903773e-02</td>
      <td>4.781401e-01</td>
      <td>1.003659e+00</td>
      <td>2.398021e-01</td>
      <td>2014.000000</td>
      <td>10.000000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>1.732382e+00</td>
      <td>1.374207e+02</td>
      <td>1.848007e+01</td>
      <td>1.004105e+00</td>
      <td>8.961478e-01</td>
      <td>6.826427e-01</td>
      <td>1.725493e+02</td>
      <td>7.104621e-01</td>
      <td>4.976016e+00</td>
      <td>9.465850e-01</td>
      <td>...</td>
      <td>4.617358e+00</td>
      <td>4.590928e+00</td>
      <td>2.535215e+00</td>
      <td>4.676216e+00</td>
      <td>3.549171e+00</td>
      <td>3.054193e+00</td>
      <td>2.163833e+01</td>
      <td>2015.000000</td>
      <td>12.000000</td>
      <td>6.000000</td>
    </tr>
  </tbody>
</table>
<p>8 rows × 279 columns</p>
</div>



<li> <b> Method #2: histogram & box plot </b>


```python
df_copy['full_sq'].hist(bins=100)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x24be5f86cd0>




    
![[output_43_1.png]]
    



```python
sns.boxplot(df_copy['full_sq'])
```




    <matplotlib.axes._subplots.AxesSubplot at 0x24be865cc10>




    
![[output_44_1.png]]
    


<li> <b> Method #3: bar chart</b>


```python
# to check outliers in categorical attributes
df['ecology'].value_counts().plot(kind='bar')
 # But if there is a category with only one value called ‘extraordinary’, that could be considered an ‘outlier’.
```




    <matplotlib.axes._subplots.AxesSubplot at 0x24b80188dc0>




    
![[output_46_1.png]]
    


<li> <b> How to handle missing data </b>

<li> Unnecessary data

<li> <b>Unnecessary type #1: repetitive & uninformative </b>

When an extremely high percentage of the column has a repetitive value,


```python
num_rows = len(df_copy)

for col in df_copy.columns:
    cnts = df_copy[col].value_counts(dropna=False)
    top_pct = (cnts/num_rows).iloc[0]
    
    if top_pct > 0.999:
        print('{0}: {1:.2f}%'.format(col, top_pct*100))
        print(cnts)
        print()
```

<li> <b> Unnecessary type #2: irrelevant

 If features are not related to the question we are trying to solve, they are irrelevant. Use "drop()" method to drop such features

<li> <b> Unnecessary type #3: duplicates </b>
    <li>duplicate occurs when all the columns’ values within the observations are the same.


```python
df_copy[df_copy.duplicated()]
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
      <th>id</th>
      <th>timestamp</th>
      <th>full_sq</th>
      <th>life_sq</th>
      <th>floor</th>
      <th>max_floor</th>
      <th>material</th>
      <th>build_year</th>
      <th>num_room</th>
      <th>kitch_sq</th>
      <th>...</th>
      <th>cafe_count_5000_price_2500</th>
      <th>cafe_count_5000_price_4000</th>
      <th>cafe_count_5000_price_high</th>
      <th>big_church_count_5000</th>
      <th>church_count_5000</th>
      <th>mosque_count_5000</th>
      <th>leisure_count_5000</th>
      <th>sport_count_5000</th>
      <th>market_count_5000</th>
      <th>price_doc</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
<p>0 rows × 292 columns</p>
</div>




```python
#We first drop id, and then see if there are duplicated rows from the DataFrame

df_copy[df_copy.drop(columns=['id']).duplicated()]
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
      <th>id</th>
      <th>timestamp</th>
      <th>full_sq</th>
      <th>life_sq</th>
      <th>floor</th>
      <th>max_floor</th>
      <th>material</th>
      <th>build_year</th>
      <th>num_room</th>
      <th>kitch_sq</th>
      <th>...</th>
      <th>cafe_count_5000_price_2500</th>
      <th>cafe_count_5000_price_4000</th>
      <th>cafe_count_5000_price_high</th>
      <th>big_church_count_5000</th>
      <th>church_count_5000</th>
      <th>mosque_count_5000</th>
      <th>leisure_count_5000</th>
      <th>sport_count_5000</th>
      <th>market_count_5000</th>
      <th>price_doc</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4328</th>
      <td>4331</td>
      <td>2012-10-22</td>
      <td>61</td>
      <td>-999.0</td>
      <td>18.0</td>
      <td>-999.0</td>
      <td>-999.0</td>
      <td>-999.0</td>
      <td>-999.0</td>
      <td>-999.0</td>
      <td>...</td>
      <td>11</td>
      <td>2</td>
      <td>1</td>
      <td>5</td>
      <td>4</td>
      <td>0</td>
      <td>1</td>
      <td>32</td>
      <td>5</td>
      <td>8248500</td>
    </tr>
    <tr>
      <th>6991</th>
      <td>6994</td>
      <td>2013-04-03</td>
      <td>42</td>
      <td>-999.0</td>
      <td>2.0</td>
      <td>-999.0</td>
      <td>-999.0</td>
      <td>-999.0</td>
      <td>-999.0</td>
      <td>-999.0</td>
      <td>...</td>
      <td>3</td>
      <td>2</td>
      <td>0</td>
      <td>2</td>
      <td>16</td>
      <td>1</td>
      <td>0</td>
      <td>20</td>
      <td>4</td>
      <td>3444000</td>
    </tr>
    <tr>
      <th>8059</th>
      <td>8062</td>
      <td>2013-05-22</td>
      <td>68</td>
      <td>-999.0</td>
      <td>2.0</td>
      <td>-999.0</td>
      <td>-999.0</td>
      <td>-999.0</td>
      <td>-999.0</td>
      <td>-999.0</td>
      <td>...</td>
      <td>3</td>
      <td>2</td>
      <td>0</td>
      <td>2</td>
      <td>16</td>
      <td>1</td>
      <td>0</td>
      <td>20</td>
      <td>4</td>
      <td>5406690</td>
    </tr>
    <tr>
      <th>8653</th>
      <td>8656</td>
      <td>2013-06-24</td>
      <td>40</td>
      <td>-999.0</td>
      <td>12.0</td>
      <td>-999.0</td>
      <td>-999.0</td>
      <td>-999.0</td>
      <td>-999.0</td>
      <td>-999.0</td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>1</td>
      <td>4112800</td>
    </tr>
    <tr>
      <th>14004</th>
      <td>14007</td>
      <td>2014-01-22</td>
      <td>46</td>
      <td>28.0</td>
      <td>1.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>1968.0</td>
      <td>2.0</td>
      <td>5.0</td>
      <td>...</td>
      <td>10</td>
      <td>1</td>
      <td>0</td>
      <td>13</td>
      <td>15</td>
      <td>1</td>
      <td>1</td>
      <td>61</td>
      <td>4</td>
      <td>3000000</td>
    </tr>
    <tr>
      <th>17404</th>
      <td>17407</td>
      <td>2014-04-15</td>
      <td>134</td>
      <td>134.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5798496</td>
    </tr>
    <tr>
      <th>26675</th>
      <td>26678</td>
      <td>2014-12-17</td>
      <td>62</td>
      <td>-999.0</td>
      <td>9.0</td>
      <td>17.0</td>
      <td>1.0</td>
      <td>-999.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>371</td>
      <td>141</td>
      <td>26</td>
      <td>150</td>
      <td>249</td>
      <td>2</td>
      <td>105</td>
      <td>203</td>
      <td>13</td>
      <td>6552000</td>
    </tr>
    <tr>
      <th>28361</th>
      <td>28364</td>
      <td>2015-03-14</td>
      <td>62</td>
      <td>-999.0</td>
      <td>2.0</td>
      <td>17.0</td>
      <td>1.0</td>
      <td>-999.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>371</td>
      <td>141</td>
      <td>26</td>
      <td>150</td>
      <td>249</td>
      <td>2</td>
      <td>105</td>
      <td>203</td>
      <td>13</td>
      <td>6520500</td>
    </tr>
    <tr>
      <th>28712</th>
      <td>28715</td>
      <td>2015-03-30</td>
      <td>41</td>
      <td>41.0</td>
      <td>11.0</td>
      <td>17.0</td>
      <td>1.0</td>
      <td>2016.0</td>
      <td>1.0</td>
      <td>41.0</td>
      <td>...</td>
      <td>2</td>
      <td>2</td>
      <td>0</td>
      <td>2</td>
      <td>9</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
      <td>2</td>
      <td>4114580</td>
    </tr>
  </tbody>
</table>
<p>9 rows × 292 columns</p>
</div>




```python

df_dedupped = df.drop(columns=['id']).drop_duplicates()

print(df.shape)
print(df_dedupped.shape)

```

    (29779, 292)
    (29770, 291)
    

# Inconsistent data

<li> <b>Inconsistent type #1: capitalization </b>
Inconsistent use of upper and lower cases in categorical values is typical. We need to clean it since Python is case-sensitive.


```python
# to print full numpy array without ...
#import numpy as np
#import sys
#np.set_printoptions(threshold=sys.maxsize)


# to display the entire list without ...
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    display(df_copy['sub_area'].value_counts(dropna=False))

```


    Poselenie Sosenskoe          1617
    Nekrasovka                   1611
    Poselenie Vnukovskoe         1290
    Poselenie Moskovskij          925
    Poselenie Voskresenskoe       713
    Mitino                        679
    Tverskoe                      678
    Krjukovo                      518
    Mar'ino                       508
    Juzhnoe Butovo                451
    Poselenie Shherbinka          443
    Solncevo                      421
    Zapadnoe Degunino             410
    Poselenie Desjonovskoe        362
    Otradnoe                      353
    Nagatinskij Zaton             327
    Nagornoe                      305
    Bogorodskoe                   305
    Strogino                      301
    Izmajlovo                     300
    Tekstil'shhiki                298
    Ljublino                      297
    Gol'janovo                    295
    Severnoe Tushino              282
    Chertanovo Juzhnoe            273
    Birjulevo Vostochnoe          268
    Vyhino-Zhulebino              264
    Horoshevo-Mnevniki            262
    Zjuzino                       259
    Ochakovo-Matveevskoe          255
    Perovo                        247
    Ramenki                       241
    Jasenevo                      237
    Kosino-Uhtomskoe              237
    Bibirevo                      230
    Golovinskoe                   224
    Poselenie Filimonkovskoe      221
    Caricyno                      220
    Kuz'minki                     220
    Kon'kovo                      220
    Veshnjaki                     213
    Akademicheskoe                211
    Orehovo-Borisovo Juzhnoe      208
    Koptevo                       207
    Orehovo-Borisovo Severnoe     206
    Novogireevo                   201
    Chertanovo Severnoe           200
    Danilovskoe                   199
    Ivanovskoe                    197
    Mozhajskoe                    197
    Chertanovo Central'noe        196
    Pechatniki                    192
    Presnenskoe                   190
    Sokolinaja Gora               188
    Obruchevskoe                  185
    Kuncevo                       184
    Brateevo                      182
    Severnoe Butovo               182
    Rjazanskij                    180
    Hovrino                       178
    Losinoostrovskoe              177
    Juzhnoe Tushino               175
    Dmitrovskoe                   174
    Taganskoe                     173
    Severnoe Medvedkovo           167
    Beskudnikovskoe               166
    Teplyj Stan                   165
    Pokrovskoe Streshnevo         164
    Severnoe Izmajlovo            163
    Cheremushki                   158
    Nagatino-Sadovniki            158
    Troickij okrug                158
    Shhukino                      155
    Timirjazevskoe                154
    Vostochnoe Izmajlovo          154
    Preobrazhenskoe               152
    Novo-Peredelkino              149
    Filevskij Park                148
    Lomonosovskoe                 147
    Kotlovka                      147
    Juzhnoe Medvedkovo            143
    Poselenie Pervomajskoe        142
    Novokosino                    139
    Fili Davydkovo                137
    Horoshevskoe                  136
    Levoberezhnoe                 135
    Donskoe                       135
    Vojkovskoe                    131
    Sviblovo                      131
    Zjablikovo                    127
    Troparevo-Nikulino            126
    Lianozovo                     126
    Juzhnoportovoe                126
    Ajeroport                     123
    Babushkinskoe                 123
    Jaroslavskoe                  121
    Lefortovo                     119
    Vostochnoe Degunino           118
    Mar'ina Roshha                116
    Birjulevo Zapadnoe            115
    Matushkino                    111
    Savelki                       105
    Krylatskoe                    103
    Butyrskoe                     101
    Silino                        100
    Prospekt Vernadskogo          100
    Alekseevskoe                  100
    Moskvorech'e-Saburovo          99
    Basmannoe                      98
    Meshhanskoe                    94
    Staroe Krjukovo                92
    Hamovniki                      90
    Savelovskoe                    85
    Marfino                        85
    Jakimanka                      81
    Ostankinskoe                   79
    Gagarinskoe                    79
    Nizhegorodskoe                 77
    Sokol                          72
    Altuf'evskoe                   68
    Rostokino                      64
    Kurkino                        62
    Sokol'niki                     60
    Begovoe                        60
    Metrogorodok                   58
    Dorogomilovo                   56
    Zamoskvorech'e                 50
    Kapotnja                       49
    Vnukovo                        44
    Krasnosel'skoe                 37
    Severnoe                       37
    Poselenie Rogovskoe            30
    Poselenie Rjazanovskoe         26
    Poselenie Kokoshkino           20
    Poselenie Mosrentgen           19
    Poselenie Krasnopahorskoe      19
    Arbat                          15
    Vostochnoe                      7
    Poselenie Marushkinskoe         6
    Molzhaninovskoe                 3
    Poselenie Voronovskoe           2
    Name: sub_area, dtype: int64


 ‘Poselenie Sosenskoe’ and ‘pOseleNie sosenskeo’ could refer to the same district.

<li> <b> How to handle? </b>
To avoid this, we can lowercase (or uppercase) all letters.


```python
df_copy['sub_area_lower'] = df_copy['sub_area'].str.lower()
df_copy['sub_area_lower'].value_counts(dropna=False)
```




    poselenie sosenskoe        1617
    nekrasovka                 1611
    poselenie vnukovskoe       1290
    poselenie moskovskij        925
    poselenie voskresenskoe     713
                               ... 
    arbat                        15
    vostochnoe                    7
    poselenie marushkinskoe       6
    molzhaninovskoe               3
    poselenie voronovskoe         2
    Name: sub_area_lower, Length: 141, dtype: int64



<ul> <b> Inconsistent type #2: typos of categorical values </b>

A categorical column takes on a limited and usually fixed number of possible values. Sometimes it shows other values due to reasons like typos.

<ul> <b> How to find out? </b>
Let’s see an example. Within the code below:

<li> We generate a new DataFrame, df_city_ex
There is only one column that stores the city names. There are misspellings. For example, ‘torontoo’ and ‘tronto’ both refer to the city of ‘toronto’.
<li> The variable cities stores the 4 correct names of ‘toronto’, ‘vancouver’, ‘montreal’, and ‘calgary’.
<li> To identify typos, we use fuzzy logic matches. We use edit_distance from nltk, which measures the number of operations (e.g., substitution, insertion, deletion) needed to change from one string into another string.
<li> We calculate the distance between the actual values and the correct values.


```python
# Levenshtein Distance, Hamming distance
df_city_ex = pd.DataFrame(data={'city': ['torontooo', 'toronto', 'turonto', 'vancouver', 'vancover', 'vancouvr', 'montreal', 'calgary']})
df_city_ex['city'].value_counts()
```




    vancouvr     1
    montreal     1
    vancover     1
    turonto      1
    calgary      1
    vancouver    1
    torontooo    1
    toronto      1
    Name: city, dtype: int64




```python
#!pip install pyspellchecker

from spellchecker import SpellChecker
spell = SpellChecker()
i=0
for city in df_city_ex['city']:
    # Get the one `most likely` answer
    df_city_ex.at[i, 'city']= spell.correction(city)
    i=i+1
    #print(spell.correction(city))
df_city_ex['city']
```




    0      toronto
    1      toronto
    2      toronto
    3    vancouver
    4    vancouver
    5    vancouver
    6     montreal
    7      calgary
    Name: city, dtype: object




```python
df_city_ex['city'].value_counts()
```




    vancouver    3
    toronto      3
    montreal     1
    calgary      1
    Name: city, dtype: int64



---
Tags: [[!AMLIndex]]