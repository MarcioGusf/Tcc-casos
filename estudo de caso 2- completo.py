#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import time
import os
import datetime
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}

options.add_experimental_option("prefs",prefs)

#navegador=webdriver.Chrome('C:\\Program Files\\Google\\Chrome\\Application\\chrome')
#navegador=webdriver.Chrome('C:\\Users\\Rasca\\.cache\\selenium\\chromedriver\\win64\\116.0.5845.96\\chromedriver.exe', chrome_options=chrome_options)
navegador=webdriver.Chrome(options=options)



# In[2]:


#abre a pagina do whatss para colocar o qr code
navegador.get("https://web.whatsapp.com/")
time.sleep(30)


# In[9]:


#escolha de entradas
mensagem='esta mensagem sera enviada as 22 e 38'
foto= "C:\\Users\\Rasca\\Downloads\\tcc im.png"
contato ='TCC'


# In[10]:


##entradas para as escolhas da data de postagem
ano=2023
mes=9
dia=18
h=22
minu=38
s=0
##pega a data e o tempo atual
agora= datetime.datetime.now()
#define quando sera a postagem pelas escolhas das entrada
diadapostagem=datetime.datetime(ano,mes,dia,h,minu,s)
m=diadapostagem-agora
print(diadapostagem)
print(agora)
print("o tempo que falta para a postagem é de:",m)
parar=0
#laço de repetiçao para a constante atualizaçao da data, caso a atualizaçao ja tenha passado da data, as entradas serao psotadas,
##caso nao a postagem n sera feita e havera uma nova atualizaçao de quanto tempo falta até a permissao da postagem
while parar==0:
      agora= datetime.datetime.now()
      if diadapostagem<=agora:
            parar=1
            print('hora de enviar')
            navegador.find_element('xpath','//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys(contato)
            time.sleep(2)
            navegador.find_element('xpath','//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
            time.sleep(2)
            navegador.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(mensagem)
            time.sleep(1)
            navegador.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.ENTER)
      else:
                print('repetir')
                m=diadapostagem-agora
                print("o tempo que falta para a postagem é de:",m)
                time.sleep(60)
      


# In[ ]:




