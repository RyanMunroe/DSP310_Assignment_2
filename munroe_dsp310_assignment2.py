#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pandas as pd
import numpy
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
student_df=pd.read_csv("student_performance_factors.csv")
print(student_df.head())
print("--------------------------------------------------------------------------")
print(student_df.mode())
print("--------------------------------------------------------------------------")


print(student_df.describe())


# In[34]:


plt.figure()
student_df.loc[:,'Hours_Studied'].plot.hist(bins=5,color='slategray')
plt.title('Hours_Studied')
plt.xlabel('Hours')
plt.figure()
student_df.loc[:,'Attendance'].plot.hist(bins=5,color='gray')
plt.title('Attendance')
plt.xlabel('Days')
plt.figure()
student_df.loc[:,'Sleep_Hours'].plot.hist(bins=5,color='darkgray')
plt.title('Sleep_Hours')
plt.xlabel('Hours')
plt.figure()
student_df.loc[:,'Previous_Scores'].plot.hist(bins=5,color='dimgray')
plt.title('Previous_Scores')
plt.xlabel('Scores')
plt.figure()
student_df.loc[:,'Tutoring_Sessions'].plot.hist(bins=5,color='silver')
plt.title('Tutoring_Sessions')
plt.xlabel('# Of Sessions')
plt.figure()
student_df.loc[:,'Physical_Activity'].plot.hist(bins=5,color='lightsteelblue')
plt.title('Physical_Activity')
plt.xlabel('Hours')
plt.figure()
student_df.loc[:,'Exam_Score'].plot.hist(bins=5,color='lightslategray')
plt.title('Exam_Score')
plt.xlabel('Scores')

plt.show()


# In[35]:


student_df.loc[:,'Parental_Involvement'].value_counts().plot.bar(color='slategray')
plt.figure()
student_df.loc[:,'Access_to_Resources'].value_counts().plot.bar(color='gray')
plt.figure()
student_df.loc[:,'Extracurricular_Activities'].value_counts().plot.bar(color='darkgray')
plt.figure()
student_df.loc[:,'Motivation_Level'].value_counts().plot.bar(color='dimgray')
plt.figure()
student_df.loc[:,'Internet_Access'].value_counts().plot.bar(color='silver')
plt.figure()
student_df.loc[:,'Family_Income'].value_counts().plot.bar(color='lightsteelblue')
plt.figure()
student_df.loc[:,'Teacher_Quality'].value_counts().plot.bar(color='lightslategray')
plt.figure()
student_df.loc[:,'School_Type'].value_counts().plot.bar(color='slategray')
plt.figure()
student_df.loc[:,'Peer_Influence'].value_counts().plot.bar(color='gray')
plt.figure()
student_df.loc[:,'Learning_Disabilities'].value_counts().plot.bar(color='darkgray')
plt.figure()
student_df.loc[:,'Parental_Education_Level'].value_counts().plot.bar(color='dimgray')
plt.figure()
student_df.loc[:,'Distance_from_Home'].value_counts().plot.bar(color='silver')
plt.figure()
student_df.loc[:,'Gender'].value_counts().plot.bar(color='lightsteelblue')

plt.show()


# How many columns are there? -> 20
# 
# 
# How many rows are there? -> 6607
# 
# 
# Are the columns numerical, categorical, or both? -> Both
# 
# 
# Are there columns that provide no information? Just constant or unique values for all observations. -> 
#       No missing values. No unique values.
# 
# 
# For each categorical columns compute the mode. -> Parental_Involvement=Medium Access_to_Resources=Medium 
# Extracurricular_Activities=Yes Motivation_Level=Medium Internet_Access=Yes Family_Income=Low Teacher_Quality=Medium School_Type=Public Peer_Influence=Positive Learning_Disabilities=No Parental_Education_Level=High School Distance_from_Home=Near Gender=Male 
# 
# 
# For each numerical column compute the mean (average), max, and min values. -> Hours_Studied=19.98,44.00,1.00   Attendance=79.98,100.00,60.00  Sleep_Hours=7.03,10.00,4.00  Previous_Scores=75.07,100.00,50.00 Tutoring_Sessions=1.49,8.00,0.00  Physical_Activity=2.97,6.00,0.00   Exam_Score=67.24,101.00,55.00
# 
# 
# Plot histograms for numerical columns -- comment on the distribution (normal, multi-modal etc) -> Hours_Studied=Unimodal, slight right skew   Attendance=Uniform, slight left skew  Sleep_Hours=Unimodal, normal  Previous_Scores=Uniform, slight left skew  Tutoring_Sessions=Unimodal, right skew  Physical_Activity=Unimodal, normal   Exam_Score=Unimodal, slight right skew
# 
# 
# Plot bar plots for categorical columns. -- comment on whether the data set is balanced in terms of the representation of the various labels in the categorical columns. -> I do believe the data set is balanced in terms of representation of various labels in the categorical column. Most of the information that is categorical are either yes/no or had minimal (2-3) options for the category. Along with the fact that there are 13 categorical columns, I believe this information is large enough and easy enough to work with that I can claim it is balanced.

# In[30]:


import pandas as pd
import numpy
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
customer_df=pd.read_csv("customer_purchasing_behaviors.csv")
print(customer_df.head())
print("--------------------------------------------------------------------------")
print(customer_df.mode())
print("--------------------------------------------------------------------------")


print(customer_df.describe())


# In[31]:


plt.figure()
customer_df.loc[:,'age'].plot.hist(bins=5,color='slategray')
plt.title('age')
plt.xlabel('Age')
plt.figure()
customer_df.loc[:,'annual_income'].plot.hist(bins=5,color='gray')
plt.title('annual_income')
plt.xlabel('Income')
plt.figure()
customer_df.loc[:,'purchase_amount'].plot.hist(bins=5,color='darkgray')
plt.title('purchase_amount')
plt.xlabel('Amount')
plt.figure()
customer_df.loc[:,'loyalty_score'].plot.hist(bins=5,color='dimgray')
plt.title('loyalty_score')
plt.xlabel('Score')
plt.figure()
customer_df.loc[:,'purchase_frequency'].plot.hist(bins=5,color='silver')
plt.title('purchase_frequency')
plt.xlabel('Frequency')

plt.show()


# In[32]:


customer_df.loc[:,'user_id'].value_counts().plot.bar(color='slategray')
plt.figure()
customer_df.loc[:,'region'].value_counts().plot.bar(color='gray')
plt.figure()

plt.show()


# How many columns are there? -> 7
# 
# How many rows are there? -> 238
# 
# Are the columns numerical, categorical, or both? -> Both
# 
# Are there columns that provide no information? Just constant or unique values for all observations. -> No missing values. Contains both constant and unique values.
# 
# For each categorical columns compute the mode. -> region=North
# 
# For each numerical column compute the mean (average), max, and min values. -> age=38.68,55.00,22.00  annual_income=57407.56,75000.00,30,000.00  purchase_amount=425.00,640.00,150.00  loyalty_score=6.80,9.500,3.00 purchase_frequency=19.80,28.00,10.00
# 
# Plot histograms for numerical columns -- comment on the distribution (normal, multi-modal etc) ->  age= Roughly uniform(could be considered bimodal), slight left skew  annual_income=Unimodal, heavy left skew  purchase_amount=Bimodal, left skew  loyalty_score=Unimodal, left skew  purchase_frequency=Unimodal, left skew
# 
# Plot bar plots for categorical columns. -- comment on whether the data set is balanced in terms of the 
# representation of the various labels in the categorical columns. -> I believe there could be more categorical data for this data set that could enhance our understanding of it as a whole. We only have one column of categorical data, and although I do believe that the variety of the labels is balanced within this bar chart, we should have more categorical data. user_id is a column of unique values, which is why it looks so strange. The most important piece of information that we need to remember from this bar chart is simply the fact that user_id is only keeping track of the unique values partaining to each customer, which our variables are then attributed to.
