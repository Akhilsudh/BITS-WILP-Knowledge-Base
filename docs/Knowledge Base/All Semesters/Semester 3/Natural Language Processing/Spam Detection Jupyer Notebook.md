# Spam Detection Jupyter Notebook

```python

import pandas as pd

  

sms_spam = pd.read_csv('SMSSpamCollection', sep='\t',

header=None, names=['Label', 'SMS'])

  

print(sms_spam.shape)

sms_spam.head()

```

  

    (5572, 2)

  
  
  
  

<div>

<table border="1" class="dataframe">

  <thead>

    <tr style="text-align: right;">

      <th></th>

      <th>Label</th>

      <th>SMS</th>

    </tr>

  </thead>

  <tbody>

    <tr>

      <th>0</th>

      <td>ham</td>

      <td>Go until jurong point, crazy.. Available only ...</td>

    </tr>

    <tr>

      <th>1</th>

      <td>ham</td>

      <td>Ok lar... Joking wif u oni...</td>

    </tr>

    <tr>

      <th>2</th>

      <td>spam</td>

      <td>Free entry in 2 a wkly comp to win FA Cup fina...</td>

    </tr>

    <tr>

      <th>3</th>

      <td>ham</td>

      <td>U dun say so early hor... U c already then say...</td>

    </tr>

    <tr>

      <th>4</th>

      <td>ham</td>

      <td>Nah I don't think he goes to usf, he lives aro...</td>

    </tr>

  </tbody>

</table>

</div>

  
  
  
  

```python

sms_spam['Label'].value_counts(normalize=True)

```

  
  
  
  

    ham     0.865937

    spam    0.134063

    Name: Label, dtype: float64

  
  
  
  

```python

# Randomize the dataset

data_randomized = sms_spam.sample(frac=1, random_state=1)

  

# Calculate index for split

training_test_index = round(len(data_randomized) * 0.8)

  

# Split into training and test sets

training_set = data_randomized[:training_test_index].reset_index(drop=True)

test_set = data_randomized[training_test_index:].reset_index(drop=True)

  

print(training_set.shape)

print(test_set.shape)

```

  

    (4458, 2)

    (1114, 2)

  
  

```python

training_set['Label'].value_counts(normalize=True)

```

  
  
  
  

    ham     0.86541

    spam    0.13459

    Name: Label, dtype: float64

  
  
  
  

```python

test_set['Label'].value_counts(normalize=True)

```

  
  
  
  

    ham     0.868043

    spam    0.131957

    Name: Label, dtype: float64

  
  
  
  

```python

# Before cleaning

training_set.head(3)

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

      <th>Label</th>

      <th>SMS</th>

    </tr>

  </thead>

  <tbody>

    <tr>

      <th>0</th>

      <td>ham</td>

      <td>Yep, by the pretty sculpture</td>

    </tr>

    <tr>

      <th>1</th>

      <td>ham</td>

      <td>Yes, princess. Are you going to make me moan?</td>

    </tr>

    <tr>

      <th>2</th>

      <td>ham</td>

      <td>Welp apparently he retired</td>

    </tr>

  </tbody>

</table>

</div>

  
  
  
  

```python

# After cleaning

training_set['SMS'] = training_set['SMS'].str.replace(

   '\W', ' ') # Removes punctuation

training_set['SMS'] = training_set['SMS'].str.lower()

training_set.head(3)

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

      <th>Label</th>

      <th>SMS</th>

    </tr>

  </thead>

  <tbody>

    <tr>

      <th>0</th>

      <td>ham</td>

      <td>yep  by the pretty sculpture</td>

    </tr>

    <tr>

      <th>1</th>

      <td>ham</td>

      <td>yes  princess  are you going to make me moan</td>

    </tr>

    <tr>

      <th>2</th>

      <td>ham</td>

      <td>welp apparently he retired</td>

    </tr>

  </tbody>

</table>

</div>

  
  
  
  

```python

training_set['SMS'] = training_set['SMS'].str.split()

  

vocabulary = []

for sms in training_set['SMS']:

   for word in sms:

      vocabulary.append(word)

  

vocabulary = list(set(vocabulary))

```

  
  

```python

len(vocabulary)

```

  
  
  
  

    7783

  
  
  
  

```python

word_counts_per_sms = {'secret': [2,1,1],

                       'prize': [2,0,1],

                       'claim': [1,0,1],

                       'now': [1,0,1],

                       'coming': [0,1,0],

                       'to': [0,1,0],

                       'my': [0,1,0],

                       'party': [0,1,0],

                       'winner': [0,0,1]

                      }

  

word_counts = pd.DataFrame(word_counts_per_sms)

word_counts.head()

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

      <th>secret</th>

      <th>prize</th>

      <th>claim</th>

      <th>now</th>

      <th>coming</th>

      <th>to</th>

      <th>my</th>

      <th>party</th>

      <th>winner</th>

    </tr>

  </thead>

  <tbody>

    <tr>

      <th>0</th>

      <td>2</td>

      <td>2</td>

      <td>1</td>

      <td>1</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

    </tr>

    <tr>

      <th>1</th>

      <td>1</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>1</td>

      <td>1</td>

      <td>1</td>

      <td>1</td>

      <td>0</td>

    </tr>

    <tr>

      <th>2</th>

      <td>1</td>

      <td>1</td>

      <td>1</td>

      <td>1</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>1</td>

    </tr>

  </tbody>

</table>

</div>

  
  
  
  

```python

word_counts_per_sms = {unique_word: [0] * len(training_set['SMS']) for unique_word in vocabulary}

  

for index, sms in enumerate(training_set['SMS']):

   for word in sms:

      word_counts_per_sms[word][index] += 1

```

  
  

```python

word_counts = pd.DataFrame(word_counts_per_sms)

word_counts.head()

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

      <th>indyarocks</th>

      <th>port</th>

      <th>eg</th>

      <th>surly</th>

      <th>trained</th>

      <th>voda</th>

      <th>organise</th>

      <th>vu</th>

      <th>leg</th>

      <th>06</th>

      <th>...</th>

      <th>imposter</th>

      <th>gee</th>

      <th>4882</th>

      <th>reduce</th>

      <th>sexual</th>

      <th>nange</th>

      <th>conducts</th>

      <th>noworriesloans</th>

      <th>taxes</th>

      <th>book</th>

    </tr>

  </thead>

  <tbody>

    <tr>

      <th>0</th>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>...</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

    </tr>

    <tr>

      <th>1</th>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>...</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

    </tr>

    <tr>

      <th>2</th>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>...</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

    </tr>

    <tr>

      <th>3</th>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>...</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

    </tr>

    <tr>

      <th>4</th>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>...</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

    </tr>

  </tbody>

</table>

<p>5 rows × 7783 columns</p>

</div>

  
  
  
  

```python

training_set_clean = pd.concat([training_set, word_counts], axis=1)

training_set_clean.head()

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

      <th>Label</th>

      <th>SMS</th>

      <th>indyarocks</th>

      <th>port</th>

      <th>eg</th>

      <th>surly</th>

      <th>trained</th>

      <th>voda</th>

      <th>organise</th>

      <th>vu</th>

      <th>...</th>

      <th>imposter</th>

      <th>gee</th>

      <th>4882</th>

      <th>reduce</th>

      <th>sexual</th>

      <th>nange</th>

      <th>conducts</th>

      <th>noworriesloans</th>

      <th>taxes</th>

      <th>book</th>

    </tr>

  </thead>

  <tbody>

    <tr>

      <th>0</th>

      <td>ham</td>

      <td>[yep, by, the, pretty, sculpture]</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>...</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

    </tr>

    <tr>

      <th>1</th>

      <td>ham</td>

      <td>[yes, princess, are, you, going, to, make, me,...</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>...</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

    </tr>

    <tr>

      <th>2</th>

      <td>ham</td>

      <td>[welp, apparently, he, retired]</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>...</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

    </tr>

    <tr>

      <th>3</th>

      <td>ham</td>

      <td>[havent]</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>...</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

    </tr>

    <tr>

      <th>4</th>

      <td>ham</td>

      <td>[i, forgot, 2, ask, ü, all, smth, there, s, a,...</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>...</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

      <td>0</td>

    </tr>

  </tbody>

</table>

<p>5 rows × 7785 columns</p>

</div>

  
  
  
  

```python

# Isolating spam and ham messages first

spam_messages = training_set_clean[training_set_clean['Label'] == 'spam']

ham_messages = training_set_clean[training_set_clean['Label'] == 'ham']

  

# P(Spam) and P(Ham)

p_spam = len(spam_messages) / len(training_set_clean)

p_ham = len(ham_messages) / len(training_set_clean)

  

# N_Spam

n_words_per_spam_message = spam_messages['SMS'].apply(len)

n_spam = n_words_per_spam_message.sum()

  

# N_Ham

n_words_per_ham_message = ham_messages['SMS'].apply(len)

n_ham = n_words_per_ham_message.sum()

  

# N_Vocabulary

n_vocabulary = len(vocabulary)

  

# Laplace smoothing

alpha = 1

```

  
  

```python

# Initiate parameters

parameters_spam = {unique_word:0 for unique_word in vocabulary}

parameters_ham = {unique_word:0 for unique_word in vocabulary}

  

# Calculate parameters

for word in vocabulary:

   n_word_given_spam = spam_messages[word].sum() # spam_messages already defined

   p_word_given_spam = (n_word_given_spam + alpha) / (n_spam + alpha*n_vocabulary)

   parameters_spam[word] = p_word_given_spam

  

   n_word_given_ham = ham_messages[word].sum() # ham_messages already defined

   p_word_given_ham = (n_word_given_ham + alpha) / (n_ham + alpha*n_vocabulary)

   parameters_ham[word] = p_word_given_ham

```

  
  

```python

import re

  

def classify(message):

   '''

   message: a string

   '''

  

   message = re.sub('\W', ' ', message)

   message = message.lower().split()

  

   p_spam_given_message = p_spam

   p_ham_given_message = p_ham

  

   for word in message:

      if word in parameters_spam:

         p_spam_given_message *= parameters_spam[word]

  

      if word in parameters_ham:

         p_ham_given_message *= parameters_ham[word]

  

   print('P(Spam|message):', p_spam_given_message)

   print('P(Ham|message):', p_ham_given_message)

  

   if p_ham_given_message > p_spam_given_message:

      print('Label: Ham')

   elif p_ham_given_message < p_spam_given_message:

      print('Label: Spam')

   else:

      print('Equal proabilities, have a human classify this!')

```

  
  

```python

classify('WINNER!! This is the secret code to unlock the money: C3421.')

```

  

    P(Spam|message): 1.3481290211300841e-25

    P(Ham|message): 1.9368049028589875e-27

    Label: Spam

  
  

```python

classify("Sounds good, Tom, then see u there")

```

  

    P(Spam|message): 2.4372375665888117e-25

    P(Ham|message): 3.687530435009238e-21

    Label: Ham

  
  

```python

def classify_test_set(message):

   '''

   message: a string

   '''

  

   message = re.sub('\W', ' ', message)

   message = message.lower().split()

  

   p_spam_given_message = p_spam

   p_ham_given_message = p_ham

  

   for word in message:

      if word in parameters_spam:

         p_spam_given_message *= parameters_spam[word]

  

      if word in parameters_ham:

         p_ham_given_message *= parameters_ham[word]

  

   if p_ham_given_message > p_spam_given_message:

      return 'ham'

   elif p_spam_given_message > p_ham_given_message:

      return 'spam'

   else:

      return 'needs human classification'

```

  
  

```python

test_set['predicted'] = test_set['SMS'].apply(classify_test_set)

test_set.head()

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

      <th>Label</th>

      <th>SMS</th>

      <th>predicted</th>

    </tr>

  </thead>

  <tbody>

    <tr>

      <th>0</th>

      <td>ham</td>

      <td>Later i guess. I needa do mcat study too.</td>

      <td>ham</td>

    </tr>

    <tr>

      <th>1</th>

      <td>ham</td>

      <td>But i haf enuff space got like 4 mb...</td>

      <td>ham</td>

    </tr>

    <tr>

      <th>2</th>

      <td>spam</td>

      <td>Had your mobile 10 mths? Update to latest Oran...</td>

      <td>spam</td>

    </tr>

    <tr>

      <th>3</th>

      <td>ham</td>

      <td>All sounds good. Fingers . Makes it difficult ...</td>

      <td>ham</td>

    </tr>

    <tr>

      <th>4</th>

      <td>ham</td>

      <td>All done, all handed in. Don't know if mega sh...</td>

      <td>ham</td>

    </tr>

  </tbody>

</table>

</div>

  
  
  
  

```python

correct = 0

total = test_set.shape[0]

  

for row in test_set.iterrows():

   row = row[1]

   if row['Label'] == row['predicted']:

      correct += 1

  

print('Correct:', correct)

print('Incorrect:', total - correct)

print('Accuracy:', correct/total)

```

  

    Correct: 1100

    Incorrect: 14

    Accuracy: 0.9874326750448833

  
  

```python

  

```


---
tags: [[!NLPIndex]]