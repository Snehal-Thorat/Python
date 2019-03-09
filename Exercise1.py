#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
warnings.simplefilter('ignore')


# In[2]:


import pandas as pd
data = pd.read_csv("us_perm_visas.csv")


# In[3]:


data.info()


# In[4]:


data.head()


# In[5]:


data.shape


# In[7]:


data.ix[:,"country_of_citizenship":"country_of_citzenship"]


# In[3]:


data["country_of_citizenship"][data["country_of_citizenship"].isnull()] = data["country_of_citzenship"]


# In[8]:


#data["country_of_citzenship"].isnull()


# In[9]:


#for i in data.columns:
#    print(i)


# In[13]:


#Q1. What is the count of applications submitted by each country?


# In[4]:


data.groupby("country_of_citizenship").country_of_citizenship.count()


# In[15]:


#Q2. List top 3 countries with highest number of applications and also show number of applications by them.


# In[6]:


data.groupby("country_of_citizenship").country_of_citizenship.count().nlargest(3)


# In[12]:


#Q3. How many applications were denied?


# In[9]:


data[data.case_status=="Denied"].case_number.count()


# In[19]:


#Q4. How many applicants holding H-1B visas were certified for Permenant Residency? 
#(Consider all forms used for writing "H1-B" in data. Consider only H1-B, not H1-B1)


# In[18]:


data.class_of_admission.unique()


# In[35]:


data[(data.application_type=="PERM") & ((data.class_of_admission=="H-1B") | (data.class_of_admission=="H1-B"))].case_no.count()


# In[42]:


data[(data.application_type=="PERM") & (data.class_of_admission=="H-1B")].case_no.count()


# In[38]:


data[((data.class_of_admission=="H-1B") | (data.class_of_admission=="H1-B"))].case_no.count()


# In[39]:


data[(data.class_of_admission=="H1-B")].case_no.count()


# In[40]:


data[data.class_of_admission!="H-1B"].case_no.count()


# In[84]:


#data[(data['employer_name'].str.contains("Edelman ")==True)].employer_name


# In[22]:


#data[(data.case_no != data.case_number) & (data.case_status=="Denied")]


# In[20]:


#Incomplete #Q5. Sort columns in descending order according to number of missing values in them.


# In[11]:


data.isnull().sum().sort_values(ascending=False)


# In[12]:


#data_isnull[data_isnull.class_of_admission == True].class_of_admission.count()


# In[26]:


#Incomplete #Q6. List top 10 cities from which employers have submitted the most applications. How many applicarions were submitted by them?


# In[25]:


data.groupby("agent_city").agent_city.count().nlargest(3)


# In[21]:


#Q7. Which are the top 10 employers who have submitted the highest number of applications? How many?


# In[12]:


data.groupby("employer_name").employer_name.count().nlargest(3)


# In[ ]:


#Q8. What is the average time of processing the applications?


# In[13]:


data['decision_date'] = pd.to_datetime(data['decision_date'])
data['case_received_date'] = pd.to_datetime(data['case_received_date'])
data["processing_time"] = (data['decision_date'] - data['case_received_date']).dt.days
data.processing_time.mean()


# In[ ]:


#data.time


# In[ ]:


diff_dates(data["case_received_date"],data["decision_date"])


# In[ ]:


#data.decision_date


# In[ ]:


#processing_time = data.case_received_date - data.decision_date


# In[ ]:


#Q9. What is count of applications for each case status(e.g. Certified, Denied etc) for applicants with "Doctorate" degree?


# In[ ]:


data[data.foreign_worker_info_education == "Doctorate"].groupby("case_status").case_status.count()


# In[ ]:


#Q.10 What are the top 3 economic sectors that has maximum applicants? How many applications are submitted from these sectors? 
#(Use case_no column here, instead of case_number)


# In[ ]:


data.groupby("us_economic_sector").case_no.count()


# In[ ]:


#Q.11 What is the mean wage of all the certified visa applications?


# In[16]:


data[(data.case_status=="Certified") & (data.wage_offer_unit_of_pay_9089 == "yr")].wage_offer_from_9089.mean()


# In[ ]:


data[(data.case_status=="Certified") & ((data.wage_offer_unit_of_pay_9089 == "yr") | (data.wage_offer_unit_of_pay_9089 == "Year"))].wage_offer_from_9089.mean()


# In[ ]:


data.wage_offer_unit_of_pay_9089.unique()


# In[ ]:


data[(data.wage_offer_unit_of_pay_9089 == "yr")].wage_offer_from_9089.mean()


# In[ ]:


#data[(data.wage_offer_unit_of_pay_9089 == "Week")].wage_offer_from_9089.mean()


# In[ ]:


#Q.12 Show one instresting finding of your own which is not covered above. Show the code and write your finding as comment.


# In[17]:


data[(data.application_type=="PERM") & (data.class_of_admission=="H-1B") | (data.class_of_admission=="H1B")].case_no.count()


# In[48]:


data[(data.application_type=="PERM") & (data.class_of_admission=="H-1B")].wage_offer_from_9089.mean()


# In[ ]:


data.groupby("us_economic_sector").case_no.count()


# In[56]:


data.groupby("employer_name").employer_name.count().nlargest(10)


# In[55]:


#Q.13 Write a report on your analysis of this dataset. 
#(Around 200 words, but quality of your report will be taken into account more than count of words)


# In[58]:


data.groupby("case_status").case_number.count()


# In[60]:


data.groupby("class_of_admission").case_number.count().sort_values(ascending = False)


# In[61]:


data.groupby("employer_state").case_number.count().nlargest(10)


# In[66]:


data['decision_date'] = pd.to_datetime(data['decision_date'])
data['case_received_date'] = pd.to_datetime(data['case_received_date'])
data["processing_time"] = (data['decision_date'] - data['case_received_date']).dt.days
data.processing_time.max()


# In[75]:


data[data.foreign_worker_info_education == "Master's"].groupby("case_status").case_status.count()


# In[72]:


data.foreign_worker_info_education.unique()


# In[76]:


data.groupby("us_economic_sector").case_no.count().sort_values(ascending = False)


# In[ ]:




