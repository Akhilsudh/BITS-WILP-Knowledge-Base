# Applied ML Assignment 1
#### (This notebook along with it's PDF version can be found in this [Github Repo](https://github.com/Akhilsudh/BITS-Assignment/tree/master/Semester%202/Applied%20Machine%20Learning))
---
# Heart Attack Analaysis
## Introduction
 A heart attack occurs when an artery supplying your heart with blood and oxygen becomes blocked. A blood clot can form and block your arteries, causing a heart attack. This Heart Attack Analysis helps to understand the chance of attack occurrence in persons based on varied health conditions.

## Dataset
The dataset is `Heart_Attack_Analysis_Data.csv`. It has been uploaded to elearn. 
This dataset contains data about some hundreds of patients mentioning: 
- Age 
- Sex
- Exercise Include Angina(1=YES, 0=NO) 
- CP_Type (Chest Pain) (Value 1: typical angina, Value 2: atypical angina, Value 3: non-anginal pain, Value 4: asymptomatic) 
- ECG Results
- Blood Pressure 
- Cholesterol 
- Blood Sugar 
- Family History (Number of persons affected in the family) 
- Maximum Heart Rate 
- Target (0 = LESS CHANCE , 1 = MORE CHANCE)

## Aim
- Building a Predictive Model using Naïve Bayesian Approach (Which features decide heart attack?)
- Comment on the performance of this model using AUC-ROC, Precision, Recall, F_score, Accuracy

You need to 
1. Preprocess the data to enhance quality
2. Carry out descriptive summarization of data and make observations
3. Identify relevant, irrelevant attributes for building model. 
4. Use data visualization tools and make observations
5. Carry out the chosen analytic task. Show results including intermediate results, as needed
6. Evaluate the solution

Following are some points for you to take note of, while doing the assignment in Jupyter Notebook:
- State all your assumptions clearly
- List all intermediate steps and learnings
- Mention your observations/findings

---

## Submission Plan

The following will be done in this notebook:
1. Verify the datatypes of the values given in the dataset and validate with the information given in the document.
2. Check for invalid values based on domain knowledge by checking if values are present in humanly possible ranges.
3. Figure out which columns are numeric and categorical based on the unique values each column has and based on information given in the assignment document.
4. Check for trends among numerical features and among categorical features to see if feature reduction can be done (via pairplots etc)
5. Check which numerical attributes are relevant and which are irrelevant and drop irrelevant ones.
6. Scale numerical attributes with a standard scaler.
7. Train a gnb **MODEL 1** where it is fit with data where only scaling is done to numerical data.
8. Check for outliers via boxplots and remove them with IQR method.
9. Train a gnb **MODEL 2** where it is fit with data where scaling is done to numerical data, and outliers are removed using the IQR method.
10. One hot encode categorical data.
11. Train a gnb **MODEL 3** where it is fit with data where scaling is done to numerical data, outliers are removed using the IQR method and one hot encoding is done to categorical data.

We will then **compare the accuracy, Precision, Recall, F-Score and AOC-ROC of three models trained**.


## My Submission
### Importing necessary packages


```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
import seaborn as sb
import warnings

from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, confusion_matrix, ConfusionMatrixDisplay, precision_recall_fscore_support, roc_auc_score, roc_curve
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler

warnings.filterwarnings('ignore')
```

### Viewing Data
Check the shape of the dataframe loaded into memory from the CSV file and see the datatypes used in the dataset given


```python
df = pd.read_csv("./Heart_Attack_Analysis_Data.csv")
print("Dataframe Shape: {}".format(df.shape))
print("----------------------------------\n")
print("With following data types:\n")
df.info()
print("----------------------------------\n")
print("First 5 rows of Dataframe:")
df.head()
```

    Dataframe Shape: (303, 11)
    ----------------------------------
    
    With following data types:
    
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 303 entries, 0 to 302
    Data columns (total 11 columns):
     #   Column          Non-Null Count  Dtype
    ---  ------          --------------  -----
     0   Age             303 non-null    int64
     1   Sex             303 non-null    int64
     2   CP_Type         303 non-null    int64
     3   BloodPressure   303 non-null    int64
     4   Cholestrol      303 non-null    int64
     5   BloodSugar      303 non-null    int64
     6   ECG             303 non-null    int64
     7   MaxHeartRate    303 non-null    int64
     8   ExerciseAngina  303 non-null    int64
     9   FamilyHistory   303 non-null    int64
     10  Target          303 non-null    int64
    dtypes: int64(11)
    memory usage: 26.2 KB
    ----------------------------------
    
    First 5 rows of Dataframe:
    




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
      <th>Age</th>
      <th>Sex</th>
      <th>CP_Type</th>
      <th>BloodPressure</th>
      <th>Cholestrol</th>
      <th>BloodSugar</th>
      <th>ECG</th>
      <th>MaxHeartRate</th>
      <th>ExerciseAngina</th>
      <th>FamilyHistory</th>
      <th>Target</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>63</td>
      <td>1</td>
      <td>3</td>
      <td>145</td>
      <td>233</td>
      <td>1</td>
      <td>0</td>
      <td>150</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>37</td>
      <td>1</td>
      <td>2</td>
      <td>130</td>
      <td>250</td>
      <td>0</td>
      <td>1</td>
      <td>187</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>41</td>
      <td>0</td>
      <td>1</td>
      <td>130</td>
      <td>204</td>
      <td>0</td>
      <td>0</td>
      <td>172</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>56</td>
      <td>1</td>
      <td>1</td>
      <td>120</td>
      <td>236</td>
      <td>0</td>
      <td>1</td>
      <td>178</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>57</td>
      <td>0</td>
      <td>0</td>
      <td>120</td>
      <td>354</td>
      <td>0</td>
      <td>1</td>
      <td>163</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
print("Stats on Dataframe:")
df.describe()
```

    Stats on Dataframe:
    




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
      <th>Age</th>
      <th>Sex</th>
      <th>CP_Type</th>
      <th>BloodPressure</th>
      <th>Cholestrol</th>
      <th>BloodSugar</th>
      <th>ECG</th>
      <th>MaxHeartRate</th>
      <th>ExerciseAngina</th>
      <th>FamilyHistory</th>
      <th>Target</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>303.000000</td>
      <td>303.000000</td>
      <td>303.000000</td>
      <td>303.000000</td>
      <td>303.000000</td>
      <td>303.000000</td>
      <td>303.000000</td>
      <td>303.000000</td>
      <td>303.000000</td>
      <td>303.000000</td>
      <td>303.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>54.366337</td>
      <td>0.683168</td>
      <td>0.966997</td>
      <td>131.623762</td>
      <td>246.264026</td>
      <td>0.148515</td>
      <td>0.528053</td>
      <td>149.646865</td>
      <td>0.326733</td>
      <td>1.204620</td>
      <td>0.544554</td>
    </tr>
    <tr>
      <th>std</th>
      <td>9.082101</td>
      <td>0.466011</td>
      <td>1.032052</td>
      <td>17.538143</td>
      <td>51.830751</td>
      <td>0.356198</td>
      <td>0.525860</td>
      <td>22.905161</td>
      <td>0.469794</td>
      <td>1.096825</td>
      <td>0.498835</td>
    </tr>
    <tr>
      <th>min</th>
      <td>29.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>94.000000</td>
      <td>126.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>71.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>47.500000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>120.000000</td>
      <td>211.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>133.500000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>55.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>130.000000</td>
      <td>240.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>153.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>61.000000</td>
      <td>1.000000</td>
      <td>2.000000</td>
      <td>140.000000</td>
      <td>274.500000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>166.000000</td>
      <td>1.000000</td>
      <td>2.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>77.000000</td>
      <td>1.000000</td>
      <td>3.000000</td>
      <td>200.000000</td>
      <td>564.000000</td>
      <td>1.000000</td>
      <td>2.000000</td>
      <td>202.000000</td>
      <td>1.000000</td>
      <td>5.000000</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>



All columns are `integer` type and all columns have a value for all rows (303 not null), which means that all values are filled and there are no missing values.

### Data Preprocessing
#### Now to check certain columns with humanly possible ranges based on domain knowledge
The following are the assumed ranges for these columns:
1. 0 < Age <= 100 years
2. 90 <= BloodPressure <= 200
3. 60 <= MaxHeartRate <= 220


```python
print("\nMinimum Age = {}".format(df["Age"].min()))
print("Maximum Age = {}".format(df["Age"].max()))

print("\nMinimum Blood Pressure = {}".format(df["BloodPressure"].min()))
print("Maximum Blood Pressure = {}".format(df["BloodPressure"].max()))

print("\nMinimum Heart Rate = {}".format(df["MaxHeartRate"].min()))
print("Maximum Heart Rate = {}".format(df["MaxHeartRate"].max()))
```

    
    Minimum Age = 29
    Maximum Age = 77
    
    Minimum Blood Pressure = 94
    Maximum Blood Pressure = 200
    
    Minimum Heart Rate = 71
    Maximum Heart Rate = 202
    

**All** of the mentioned columns have values within acceptable ranges.

#### Checking number of unique values for each column
`Column Name -> Unique Number count`


```python
for column in list(df.columns):
    print("{} -> {}".format(column, df[column].value_counts().shape[0]))
```

    Age -> 41
    Sex -> 2
    CP_Type -> 4
    BloodPressure -> 49
    Cholestrol -> 152
    BloodSugar -> 2
    ECG -> 3
    MaxHeartRate -> 91
    ExerciseAngina -> 2
    FamilyHistory -> 6
    Target -> 2
    

**Taking columns that have a maximum of 4 unique values (And based on information given in assignment document) as categorical and the rest as numeric:**


```python
category_list = ["Sex", "CP_Type", "BloodSugar", "ECG", "ExerciseAngina"]
numeric_list = ["Age", "BloodPressure", "Cholestrol", "MaxHeartRate", "FamilyHistory"]
```

#### Checking for trends in numeric features through Pair Plots


```python
df_number = df.loc[:, numeric_list]
df_number["Target"] = df["Target"]
sb.pairplot(df_number, hue = "Target", palette="husl")
plt.show()
```


    
![png](output_13_0.png)
    


The pair plots do not show any particular trends that can be used to reduce numerical features. We do see a slight relation between age and max heart rate but the plot is scattered enough to not relate them together.

#### Checking frequncy of each categorical feature wrt target column to check how well it is balanced 


```python
df_category = df.loc[:, category_list]
df_category["Target"] = df["Target"]
for i in category_list:
    plt.figure()
    sb.countplot(x = i, data = df_category, hue = "Target", palette="husl")
    plt.title(i)
```


    
![png](output_16_0.png)
    



    
![png](output_16_1.png)
    



    
![png](output_16_2.png)
    



    
![png](output_16_3.png)
    



    
![png](output_16_4.png)
    


#### Here we see that there is very little rows that have ECG value = 2 and similarly very little rows for BloodSugar value = 1.

### Checking relevant numerical features

To do this we shall use the `f_oneway` function from `scipy.stats`. This function performs [one-way ANOVA(Analysis of Variance)](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.f_oneway.html) to test the null hypothesis that two groups of data have the same population mean. 

A feature is only relevant if the sample from a particular feature for a target category is statistically very different from another sample from the same feature for another target category.

#### Checking relevance of Age


```python
result = stats.f_oneway(df["Age"][df["Target"] == 0],
               df["Age"][df["Target"] == 1])
result.pvalue
```




    7.524801303442268e-05



The pvalue is < 0.05. This shows that the means of the two distributions (One with Age wrt less chance of getting heart attack and the other with more chance of getting heart attack) are significantly different statistically, hence **Age is relevant**

#### Checking relevance of BloodPressure


```python
result = stats.f_oneway(df["BloodPressure"][df["Target"] == 0],
               df["BloodPressure"][df["Target"] == 1])
result.pvalue 
```




    0.011546059200233376



The pvalue is < 0.05. This shows that the means of the two distributions (One with BloodPressure wrt less chance of getting heart attack and the other with more chance of getting heart attack) are significantly different statistically, hence **BloodPressure is relevant**

#### Checking relevance of Cholestrol


```python
result = stats.f_oneway(df["Cholestrol"][df["Target"] == 0],
               df["Cholestrol"][df["Target"] == 1])
result.pvalue
```




    0.1387903269560108



The pvalue is > 0.05. This shows that the means of the two distributions (One with Cholestrol wrt less chance of getting heart attack and the other with more chance of getting heart attack) are not significantly different statistically, hence **Cholestrol is irrelevant**

#### Checking relevance of MaxHeartRate


```python
result = stats.f_oneway(df["MaxHeartRate"][df["Target"] == 0],
               df["MaxHeartRate"][df["Target"] == 1])
result.pvalue
```




    1.6973376386560805e-14



The pvalue is < 0.05. This shows that the means of the two distributions (One with MaxHeartRate wrt less chance of getting heart attack and the other with more chance of getting heart attack) are significantly different statistically, hence **MaxHeartRate is relevant**

#### Checking relevance of FamilyHistory


```python
result = stats.f_oneway(df["FamilyHistory"][df["Target"] == 0],
               df["FamilyHistory"][df["Target"] == 1])
result.pvalue
```




    0.6172651404419242



The pvalue is > 0.05. This shows that the means of the two distributions (One with FamilyHistory wrt less chance of getting heart attack and the other with more chance of getting heart attack) are not significantly different statistically, hence **FamilyHistory is irrelevant**

#### Dropping the irrelevant features


```python
df.drop(["Cholestrol"], axis = 1, inplace= True)
df.drop(["FamilyHistory"], axis = 1, inplace= True)
numeric_list.remove("Cholestrol")
numeric_list.remove("FamilyHistory")
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
      <th>Age</th>
      <th>Sex</th>
      <th>CP_Type</th>
      <th>BloodPressure</th>
      <th>BloodSugar</th>
      <th>ECG</th>
      <th>MaxHeartRate</th>
      <th>ExerciseAngina</th>
      <th>Target</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>63</td>
      <td>1</td>
      <td>3</td>
      <td>145</td>
      <td>1</td>
      <td>0</td>
      <td>150</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>37</td>
      <td>1</td>
      <td>2</td>
      <td>130</td>
      <td>0</td>
      <td>1</td>
      <td>187</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>41</td>
      <td>0</td>
      <td>1</td>
      <td>130</td>
      <td>0</td>
      <td>0</td>
      <td>172</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>56</td>
      <td>1</td>
      <td>1</td>
      <td>120</td>
      <td>0</td>
      <td>1</td>
      <td>178</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>57</td>
      <td>0</td>
      <td>0</td>
      <td>120</td>
      <td>0</td>
      <td>1</td>
      <td>163</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



#### Scaling the numeric attributes in the dataframe with a standard scaler


```python
scaler = StandardScaler()
df[numeric_list] = scaler.fit_transform(df[numeric_list])
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
      <th>Age</th>
      <th>Sex</th>
      <th>CP_Type</th>
      <th>BloodPressure</th>
      <th>BloodSugar</th>
      <th>ECG</th>
      <th>MaxHeartRate</th>
      <th>ExerciseAngina</th>
      <th>Target</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.952197</td>
      <td>1</td>
      <td>3</td>
      <td>0.763956</td>
      <td>1</td>
      <td>0</td>
      <td>0.015443</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-1.915313</td>
      <td>1</td>
      <td>2</td>
      <td>-0.092738</td>
      <td>0</td>
      <td>1</td>
      <td>1.633471</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-1.474158</td>
      <td>0</td>
      <td>1</td>
      <td>-0.092738</td>
      <td>0</td>
      <td>0</td>
      <td>0.977514</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.180175</td>
      <td>1</td>
      <td>1</td>
      <td>-0.663867</td>
      <td>0</td>
      <td>1</td>
      <td>1.239897</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.290464</td>
      <td>0</td>
      <td>0</td>
      <td>-0.663867</td>
      <td>0</td>
      <td>1</td>
      <td>0.583939</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



## Model 1
### Training a Guassian Naive Bayes model with the data (With scaling done to numerical features)


```python
df1 = df.copy()
X = df1.drop(["Target"], axis = 1)
y = df1[["Target"]]
```

#### Split X and y to training and test data


```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 3)
print("X_train: {}".format(X_train.shape))
print("y_train: {}".format(y_train.shape))
print("X_test: {}".format(X_test.shape))
print("y_test: {}".format(y_test.shape))
```

    X_train: (242, 8)
    y_train: (242, 1)
    X_test: (61, 8)
    y_test: (61, 1)
    

#### Prediction Analysis:
The following is the analysis for a naive bayes model that was trained with the following done on the data:
1. Scale the numerical features with a standard scaler
2. Split the data into training and test data with a 20% test data


```python
gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_pred = gnb.predict(X_test)

print("Model 1 Results:")
print("----------------------------------\n")
ns_probs = [0 for _ in range(len(y_test))]
ns_auc = roc_auc_score(y_test, ns_probs)
ns_fpr, ns_tpr, _ = roc_curve(y_test, ns_probs)

y_probs = gnb.predict_proba(X_test)
gnb_probs = y_probs[:, 1]
gnb_auc = roc_auc_score(y_test, gnb_probs)
gnb_fpr, gnb_tpr, temp = roc_curve(y_test, gnb_probs)
plt.plot(ns_fpr, ns_tpr, linestyle='--', label='No Skill')
plt.plot(gnb_fpr, gnb_tpr, marker='.', label='Gaussian NB')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend()
plt.show()
print("----------------------------------\n")
print("AUC-ROC Score: {0:0.2f}%".format(roc_auc_score(y_test, gnb_probs) * 100))
print("Precision Score: {0:0.2f}%".format(precision_score(y_test,y_pred) * 100))
print("Recall Score: {0:0.2f}%".format(recall_score(y_test,y_pred) * 100))
print("F Score: {0:0.2f}%".format(f1_score(y_test,y_pred) * 100))
print("Accuracy Score: {0:0.2f}%".format(accuracy_score(y_test,y_pred) * 100))

print("\n----------------------------------\n")
print("Confusion matrix:")
cm = confusion_matrix(y_pred,y_test)
ConfusionMatrixDisplay(cm,display_labels =["Less Chance","More Chance"]).plot()
plt.show()
```

    Model 1 Results:
    ----------------------------------
    
    


    
![png](output_42_1.png)
    


    ----------------------------------
    
    AUC-ROC Score: 85.71%
    Precision Score: 82.50%
    Recall Score: 82.50%
    F Score: 82.50%
    Accuracy Score: 77.05%
    
    ----------------------------------
    
    Confusion matrix:
    


    
![png](output_42_3.png)
    


---
### Investigating dataset for outliers
#### Analyzing the boxplot for scaled numeric attributes to check for outliers


```python
plt.figure(figsize=(10,8))
sb.boxplot(data=df[numeric_list], palette="husl")
plt.show()
print("\n----------------------------------\n")
```


    
![png](output_44_0.png)
    


    
    ----------------------------------
    
    

We can see some outlier values for blood pressure and max heart rate. we can drop these outliers using the IQR method.

#### Dropping outliers with IQR method 
Going with $+/- 1.6 \times IQR$ to accomodate data upto $3\sigma$ from the mean to remove the outliers.


```python
print("Original shape of dataframe: {}".format(df.shape))
for i in numeric_list:
    Q25 = np.percentile(df.loc[:, i],25)
    Q75 = np.percentile(df.loc[:, i],75)
    IQR = Q75 - Q25
    upper_bound = np.where(df.loc[:, i] >= (Q75 + 1.6*IQR))
    lower_bound = np.where(df.loc[:, i] <= (Q25 - 1.6*IQR))
    df.drop(upper_bound[0], inplace = True)
    df.drop(lower_bound[0], inplace = True)
print("Shape of dataframe after dropping outliers: {}".format(df.shape))
```

    Original shape of dataframe: (303, 9)
    Shape of dataframe after dropping outliers: (293, 9)
    

## Model 2
### Training a Guassian Naive Bayes model with the data (With scaling done to numerical features and removing outliers)


```python
df2 = df.copy()
X = df2.drop(["Target"], axis = 1)
y = df2[["Target"]]
```

#### Split X and y to training and test data


```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 3)
print("X_train: {}".format(X_train.shape))
print("y_train: {}".format(y_train.shape))
print("X_test: {}".format(X_test.shape))
print("y_test: {}".format(y_test.shape))
```

    X_train: (234, 8)
    y_train: (234, 1)
    X_test: (59, 8)
    y_test: (59, 1)
    

#### Prediction Analysis:
The following is the analysis for a naive bayes model that was trained with the following done on the data:
1. Scale the numerical features with a standard scaler
2. Remove outliers 1.6 times IQR below and above the Q1 and Q3 respectively
3. Split the data into training and test data with a 20% test data


```python
gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_pred = gnb.predict(X_test)
print("Model 2 Results:")
print("----------------------------------\n")
ns_probs = [0 for _ in range(len(y_test))]
ns_fpr, ns_tpr, _ = roc_curve(y_test, ns_probs)

y_probs = gnb.predict_proba(X_test)
gnb_probs = y_probs[:, 1]
gnb_fpr, gnb_tpr, temp = roc_curve(y_test, gnb_probs)
plt.plot(ns_fpr, ns_tpr, linestyle='--', label='No Skill')
plt.plot(gnb_fpr, gnb_tpr, marker='.', label='Gaussian NB')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend()
plt.show()
print("----------------------------------\n")
print("AUC-ROC Score: {0:0.2f}%".format(roc_auc_score(y_test, gnb_probs) * 100))
print("Precision Score: {0:0.2f}%".format(precision_score(y_test,y_pred) * 100))
print("Recall Score: {0:0.2f}%".format(recall_score(y_test,y_pred) * 100))
print("F Score: {0:0.2f}%".format(f1_score(y_test,y_pred) * 100))
print("Accuracy Score: {0:0.2f}%".format(accuracy_score(y_test,y_pred) * 100))
print("\n----------------------------------\n")
print("Confusion matrix:")
cm = confusion_matrix(y_pred,y_test)
ConfusionMatrixDisplay(cm,display_labels =["Less Chance","More Chance"]).plot()
plt.show()
```

    Model 2 Results:
    ----------------------------------
    
    


    
![png](output_53_1.png)
    


    ----------------------------------
    
    AUC-ROC Score: 85.92%
    Precision Score: 84.21%
    Recall Score: 80.00%
    F Score: 82.05%
    Accuracy Score: 76.27%
    
    ----------------------------------
    
    Confusion matrix:
    


    
![png](output_53_3.png)
    


---
### Finding correlation between features through a heatmap


```python
corr_features = set()
corr_matrix = df.corr()
plt.figure(figsize = (10,8))
sb.heatmap(corr_matrix, annot = True, cmap="magma")
plt.show()

for i in range(len(corr_matrix .columns)):
    for j in range(i):
        if abs(corr_matrix.iloc[i, j]) > 0.5:
            colname = corr_matrix.columns[i]
            corr_features.add(colname)
print("\n----------------------------------\n")
print("The number of correlating features: {}".format(len(corr_features)))
print("The correlating features are: {}".format(corr_features))
print("\n----------------------------------\n")
```


    
![png](output_55_0.png)
    


    
    ----------------------------------
    
    The number of correlating features: 0
    The correlating features are: set()
    
    ----------------------------------
    
    

None of the features seem to correlate with each other and hence we cannot do feature reduction

## Model 3
### Training a Guassian Naive Bayes model with the data (With scaling done to numerical features, outliers removed and one hot encoding categorical features)

#### Original dataframe:


```python
df3 = df.copy()
df3.head()
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
      <th>Age</th>
      <th>Sex</th>
      <th>CP_Type</th>
      <th>BloodPressure</th>
      <th>BloodSugar</th>
      <th>ECG</th>
      <th>MaxHeartRate</th>
      <th>ExerciseAngina</th>
      <th>Target</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.952197</td>
      <td>1</td>
      <td>3</td>
      <td>0.763956</td>
      <td>1</td>
      <td>0</td>
      <td>0.015443</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-1.915313</td>
      <td>1</td>
      <td>2</td>
      <td>-0.092738</td>
      <td>0</td>
      <td>1</td>
      <td>1.633471</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-1.474158</td>
      <td>0</td>
      <td>1</td>
      <td>-0.092738</td>
      <td>0</td>
      <td>0</td>
      <td>0.977514</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.180175</td>
      <td>1</td>
      <td>1</td>
      <td>-0.663867</td>
      <td>0</td>
      <td>1</td>
      <td>1.239897</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.290464</td>
      <td>0</td>
      <td>0</td>
      <td>-0.663867</td>
      <td>0</td>
      <td>1</td>
      <td>0.583939</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



#### One hot encoded dataframe:


```python
df3 = pd.get_dummies(df3, columns = category_list, drop_first = True)
df3.head()
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
      <th>Age</th>
      <th>BloodPressure</th>
      <th>MaxHeartRate</th>
      <th>Target</th>
      <th>Sex_1</th>
      <th>CP_Type_1</th>
      <th>CP_Type_2</th>
      <th>CP_Type_3</th>
      <th>BloodSugar_1</th>
      <th>ECG_1</th>
      <th>ECG_2</th>
      <th>ExerciseAngina_1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.952197</td>
      <td>0.763956</td>
      <td>0.015443</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-1.915313</td>
      <td>-0.092738</td>
      <td>1.633471</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-1.474158</td>
      <td>-0.092738</td>
      <td>0.977514</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.180175</td>
      <td>-0.663867</td>
      <td>1.239897</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.290464</td>
      <td>-0.663867</td>
      <td>0.583939</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
X = df3.drop(["Target"], axis = 1)
y = df3[["Target"]]
```

#### Split X and y to training and test data


```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 3)
print("X_train: {}".format(X_train.shape))
print("y_train: {}".format(y_train.shape))
print("X_test: {}".format(X_test.shape))
print("y_test: {}".format(y_test.shape))
```

    X_train: (234, 11)
    y_train: (234, 1)
    X_test: (59, 11)
    y_test: (59, 1)
    

### Prediction Analysis:
The following is the analysis for a naive bayes model that was trained with the following done on the data:
1. One hot encode categorical features
2. Scale the numerical features with a standard scaler
3. Remove outliers 1.6 times IQR below and above the Q1 and Q3 respectively
4. Split the data into training and test data with 20% test data


```python
gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_pred = gnb.predict(X_test)
print("Model 3 Results:")
print("----------------------------------\n")
ns_probs = [0 for _ in range(len(y_test))]
ns_fpr, ns_tpr, _ = roc_curve(y_test, ns_probs)

y_probs = gnb.predict_proba(X_test)
gnb_probs = y_probs[:, 1]
gnb_fpr, gnb_tpr, temp = roc_curve(y_test, gnb_probs)
plt.plot(ns_fpr, ns_tpr, linestyle='--', label='No Skill')
plt.plot(gnb_fpr, gnb_tpr, marker='.', label='Gaussian NB')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend()
plt.show()
print("----------------------------------\n")
print("AUC-ROC Score: {0:0.2f}%".format(roc_auc_score(y_test, gnb_probs) * 100))
print("Precision Score: {0:0.2f}%".format(precision_score(y_test,y_pred) * 100))
print("Recall Score: {0:0.2f}%".format(recall_score(y_test,y_pred) * 100))
print("F Score: {0:0.2f}%".format(f1_score(y_test,y_pred) * 100))
print("Accuracy Score: {0:0.2f}%".format(accuracy_score(y_test,y_pred) * 100))
print("\n----------------------------------\n")
print("Confusion matrix:")
cm = confusion_matrix(y_pred,y_test)
ConfusionMatrixDisplay(cm,display_labels =["Less Chance","More Chance"]).plot()
plt.show()
```

    Model 3 Results:
    ----------------------------------
    
    


    
![png](output_64_1.png)
    


    ----------------------------------
    
    AUC-ROC Score: 90.53%
    Precision Score: 85.00%
    Recall Score: 85.00%
    F Score: 85.00%
    Accuracy Score: 79.66%
    
    ----------------------------------
    
    Confusion matrix:
    


    
![png](output_64_3.png)
    


# Comparing the results of the three models:

From the results obtained from above prediction analysis, we can tabulate them together below:

| Model/Metric | AUC-ROC | Precision | Recall | F_Score | Accuracy |
| ------------ | ------- | --------- | ------ | ------- | -------- |
| Model 1      | 85.71%  | 82.50%    | 82.50% | 82.05%  | 77.05%   |
| Model 2      | 85.92%  | 84.21%    | 80.00% | 82.05%  | 76.27%   |
| Model 3      | 90.53%  | 85.00%    | 85.00% | 85.00%  | 79.66%   |

This shows that the **maximum Accuracy is obtained when scaling is applied on numerical attributes with outliers being dropped and one hot encoding is done to the categorical features (Model 3)**.

We can also see that **Model 2 has lesser accuracy but higher Precision than Model 1**. This shows that Model 1 is overfitted.

We know that:

$Precision = \frac{True Positive}{True Positive + False Positive}$

and

$Recall = \frac{True Positive}{True Positive + False Negative}$

Upon viewing the confusion matrix for each model it is clear that **lesser false negatives and false positives are recorded in Model 3** in comparison to Model 1 and Model 2 which attributes to the **better Precision and Recall scores in Model 3**.

Finally, we know that:

$F = 2 \times \frac{Precision \times Recall}{Precision + Recall}$

This goes to show why Model 3 has better F score since its recall and precision is better than the other two models.

---
Tags: [[!AMLIndex]]