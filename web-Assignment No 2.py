#!/usr/bin/env python
# coding: utf-8

# # Batch - DS2405

# # Assignment - 2

# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
import time
from selenium.webdriver.common.by import By


# In[3]:


driver=webdriver.Chrome()


# In[4]:


driver.get('https://www.naukri.com/')


# In[5]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input ")
designation.send_keys("Data Scientist")


# In[6]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
location.send_keys("Delhi")


# In[7]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[8]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[9]:


title_tags=driver.find_elements(By.XPATH,'//div[@class="cust-job-tuple layout-wrapper lay-2 sjw__tuple "]/div/a')
for i in title_tags:
    if i.text is None:
        job_title.append('Not')
    else:
        job_title.append(i.text)
job_title[:10]
   


# In[10]:


location_tags=driver.find_elements(By.XPATH,'//span[@class="locWdth"]')
for i in location_tags:
    job_location.append(i.text)
job_location[:10]


# In[11]:


company_tags=driver.find_elements(By.XPATH,'//div[@class=" row2"]/span/a[1]')
for i in company_tags:
    company_name.append(i.text)
company_name[:10]
   


# In[12]:


experience_tags=driver.find_elements(By.XPATH,'//span[@class="expwdth"]')
for i in experience_tags:
    experience_required.append(i.text)
experience_required[:10]
    


# In[13]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[14]:


df=pd.DataFrame({'Title':job_title,'Location':job_location,'Company_name':company_name,'Experience':experience_required})
df


# In[15]:


Ad=pd.DataFrame({})
Ad['Title']=job_title[:10]
Ad['Location']=job_location[:10]
Ad['Company_Name']=company_name[:10]
Ad['Experience']=experience_required[:10]
Ad


# # Q: Scrape data forfirst 100 sneakers you find whenyouvisitflipkart.com and search for “sneakers” inthe search
# field.
# You have to scrape 3 attributes of each sneaker:
# 1. Brand
# 2. ProductDescription
# 3. Price

# In[16]:


driver=webdriver.Chrome()


# In[17]:


url="https://www.flipkart.com/"
driver.get(url)


# In[18]:


search_s=driver.find_element(By.XPATH,"//input[@type='text']")
search_s


# In[19]:


search_s.send_keys('sneakers')


# In[20]:


search_btn=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input")
search_btn


# In[21]:


search_btn=driver.find_element(By.CLASS_NAME,"_2SmNnR")
search_btn.click()


# In[22]:


B_name=[]
Price=[]
P_desc=[]


# In[30]:


for i in range(3):
    b_name=driver.find_elements(By.XPATH,"//div[@class='syl9yP']")
    price =driver.find_elements(By.XPATH,"//div[@class='Nx9bqj']")
    p_desc=driver.find_elements(By.XPATH,"//div[@class='hCKiGj']")
    
    for j in b_name:
        B_name.append(j.text)
    B_name[:100]
    
    for l in price:
        Price.append(l.text)
    Price[:100]
    
    for k in p_desc:
        P_desc.append(k.text)
    P_desc[:100]


# In[34]:


print(len(B_name[:100])),print(len(Price[:100])),print(len(P_desc[:100]))


# In[37]:


Adi_1=pd.DataFrame({})
Adi_1['Brand_name']=B_name[:100]
Adi_1['P_Price']=Price[:100]
Adi_1['Product_Description']=P_desc[:100]
Adi_1


# In[ ]:





# # Q: Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. You have to scrape the
# 
# job-title, job-location, company_name, experience_required. You have to scrape first 10 jobs data.
# This task will be done in following steps:
# 1. First get the webpage https://www.shine.com/
# 2. Enter “Data Analyst” in “Job title, Skills” field and enter “Bangalore” in “enter the location” field.
# 3. Then click the searchbutton.
# 4. Then scrape the data for the first 10 jobs results you get.
# 5. Finally create a dataframe of the scraped data.

# In[143]:


driver=webdriver.Chrome()


# In[144]:


driver.get(' https://www.shine.com/')


# In[ ]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[ ]:


title_tags=driver.find_elements(By.XPATH,'')
for i in title_tags:
    if i.text is None:
        job_title.append('Not')
    else:
        job_title.append(i.text)
job_title[:10]


# In[ ]:





# # Q: Go to webpage https://www.amazon.in/ Enter “Laptop” in the search field and then click the search icon. Then set CPU
# Type filter to “Intel Core i7” as shown in the below image:
# 
# Aftersetting the filters scrape first 10 laptops data. You have to scrape 3 attributes for each laptop:
# 1. Title
# 2. Ratings
# 3. Price

# In[35]:


driver=webdriver.Chrome()


# In[36]:


url = " https://www.amazon.in/ "
driver.get(url)


# In[37]:


search_a=driver.find_element(By.XPATH,"//input[@type='text']")
search_a


# In[38]:


search_a.send_keys('Laptop')


# In[41]:


search_di=driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']")
search_di


# In[42]:


search_di=driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']")
search_di.click()


# In[43]:


Title=[]
Rating=[]
Price=[]


# In[98]:


for i in range(3):
    title_1=driver.find_elements(By.XPATH,"//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2']")
    rating_1=driver.find_elements(By.XPATH,"//span[@class='a-icon-alt']")
    price_1=driver.find_elements(By.XPATH, "//span[@class='a-price-whole']")  
    
    for j in title_1:
        Title.append(j.text)
    Title[:10]
    
    for k in rating_1:
        Rating.append(k.text)
    Rating[:10]
    
    for l in price_1:
        Price.append(l.text)
    Price[:10]


# In[99]:


print(len(title_1[:10])),print(len(rating_1[:10])),print(len(price_1[:10]))


# In[100]:


Adi_2=pd.DataFrame({})
Adi_2['Title']=Title[:10]
Adi_2['Rating']=Rating[:10]
Adi_2['Price']=Price[:10]
Adi_2


# # Q: Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link:
# 
# https://www.flipkart.com/apple-iphone-11-black-64-gb/product-
# reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&marketplace=F
# 
# LIPKART
# 
# As shown in the above page you have to scrape the tick marked attributes. These are:
# 1. Rating
# 2. Review summary
# 3. Full review
# 4. You have to scrape this data for first 100reviews.

# In[6]:


get_ipython().system('pip install selenium')


# In[7]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
import time
from selenium.webdriver.common.by import By


# In[50]:


driver=webdriver.Chrome()


# In[51]:


url='https://www.flipkart.com/apple-iphone-11-black-64-gb/product-'
driver.get(url)


# In[53]:


search_f=driver.find_element(By.XPATH,"//input[@class='Pke_EE']")
search_f


# In[111]:


search_f.send_keys('iphone-11-black-64-gb')


# In[112]:


search_ab=driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")
search_ab


# In[58]:


search_di=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/header/div[1]/div[2]/form/div/button")
search_di.click()


# In[59]:


Rating=[]
Review_summary=[]
Full_review=[]


# In[60]:


for i in range(3):
    rating_1=driver.find_elements(By.XPATH,"//div[@class='XQDdHH Ga3i8K']")
    for j in rating_1:
        Rating.append(j.text)
    Rating[:100]


# In[137]:


print(len(rating_1[:100]))


# In[132]:


for i in range(3):
    review_s=driver.find_elements(By.XPATH,"//p[@class='z9E0IG']")
    
    for k in review_s:
        Review_summary.append(k.text)
    Rating[:100]
    


# In[133]:


print(len(review_s[:100]))


# In[139]:


full_r=driver.find_elements(By.XPATH, "//div[@class='ZmyHeo']")
for l in full_r:
    Full_review.append(l.text)
Full_review[:100]


# In[140]:


print(len(full_r))


# In[ ]:





# # Q:Write a python program to scrape data for Top 1000 Quotes of All Time.
# The above task will be done in following steps:
# 1. First get the webpagehttps://www.azquotes.com/
# 2. Click on TopQuote
# 3. Than scrap a)Quote b) Author c) Type Of Quotes

# In[8]:


driver=webdriver.Chrome()


# In[9]:


driver.get("https://www.azquotes.com/")

