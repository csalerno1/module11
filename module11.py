import pandas as pd

df = pd.read_excel (r'C:\Users\caitl\Downloads\COVID19_03242020_ByCounty.xlsx')


import statsmodels.api as sm
x = df['PUIsTotal']
y = df['PUIAgeAvrg']
x = sm.add_constant(x)

print(x)
model = sm.OLS(y, x).fit()
print(model.summary())


import requests
import urllib.request
import time
from bs4 import BeautifulSoup
url = 'http://courses.washington.edu/b517/Datasets/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
soup.findAll('a')
one_a_tag = soup.findAll('a')[1]
link = one_a_tag['href']
download_url = 'http://courses.washington.edu/b517/Datasets/' + link
urllib.request.urlretrieve(download_url,'./'+link[link.find('/sharklengths')+1:])