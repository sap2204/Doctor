#!/usr/bin/env python
# coding: utf-8

# In[6]:


import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import pandas as pd
import xlsxwriter


# In[9]:


# Создание рандомного фейкового юзер-агента 
user = UserAgent().random
header = {'user-agent': user}


# In[21]:


# Исходные данные по поликлиникам
hospitals = ['Медорганизация: СПб ГБУЗ "Детская городская поликлиника №49" Детское поликлиническое отделение "София"',
            'Медорганизация: СПб ГБУЗ "Детская городская поликлиника №49" Детское поликлиническое отделение "Павловск"',
            'Медорганизация: СПб ГБУЗ "Детская городская поликлиника №49" Детское поликлиническое отделение "Шушары"',
            'Медорганизация: СПб ГБУЗ "Детская городская поликлиника №49" Детское поликлиническое отделение "Славянка"',
            'Медорганизация: СПб ГБУЗ "Детская городская поликлиника №49" Отделение врачей специалистов',
            'Медорганизация: СПб ГБУЗ "Детская городская поликлиника №49" Отделение медицинской реабилитации и абилитации',
            'Медорганизация: СПб ГБУЗ "Детская городская поликлиника №49" Педиатрическое отделение №2',
            'Медорганизация: СПб ГБУЗ "Детская городская поликлиника №49" Педиатрическое отделение №1',
            'Медорганизация: СПб ГБУЗ "Детская городская поликлиника №49" Педиатрическое отделение №3']

urls = ['https://www.gorzdrav.spb.ru/service-free-schedule#%5B%7B%22district%22:%2216%22%7D,%7B%22lpu%22:%22305%22%7D%5D',
      'https://www.gorzdrav.spb.ru/service-free-schedule#%5B%7B%22district%22:%2216%22%7D,%7B%22lpu%22:%22606%22%7D%5D',
      'https://www.gorzdrav.spb.ru/service-free-schedule#%5B%7B%22district%22:%2216%22%7D,%7B%22lpu%22:%22608%22%7D%5D',
      'https://www.gorzdrav.spb.ru/service-free-schedule#%5B%7B%22district%22:%2216%22%7D,%7B%22lpu%22:%22609%22%7D%5D',
      'https://www.gorzdrav.spb.ru/service-free-schedule#%5B%7B%22district%22:%2216%22%7D,%7B%22lpu%22:%22610%22%7D%5D',
      'https://www.gorzdrav.spb.ru/service-free-schedule#%5B%7B%22district%22:%2216%22%7D,%7B%22lpu%22:%221133%22%7D%5D',
      'https://www.gorzdrav.spb.ru/service-free-schedule#%5B%7B%22district%22:%2216%22%7D,%7B%22lpu%22:%221147%22%7D%5D',
      'https://www.gorzdrav.spb.ru/service-free-schedule#%5B%7B%22district%22:%2216%22%7D,%7B%22lpu%22:%221148%22%7D%5D',
      'https://www.gorzdrav.spb.ru/service-free-schedule#%5B%7B%22district%22:%2216%22%7D,%7B%22lpu%22:%221155%22%7D%5D']


# In[36]:


# Поочередный запрос к страницам сайта
number = 0
while number < 9:
    responce = requests
'''
for url in urls:
    responce = requests.get(url, headers = header)
    if responce.ok == True: #Проверка статуса ответа сервера и начало сбора инф-ции
        
        print('OK')
        # Получение текста страницы и выделение тегов
        #soup = BeautifulSoup(responce.text, 'lxml')
        '''


# In[ ]:




