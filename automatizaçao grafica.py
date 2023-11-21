#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import time
import os
import datetime
import schedule
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option("prefs",prefs)

#navegador=webdriver.Chrome('C:\\Program Files\\Google\\Chrome\\Application\\chrome')
#navegador=webdriver.Chrome('C:\\Users\\Rasca\\.cache\\selenium\\chromedriver\\win64\\116.0.5845.96\\chromedriver.exe', chrome_options=chrome_options)



# In[ ]:


#FUNÇÃO QUE SERÁ EXECUTADA COMO PENDENCIA PELO SCHEDULE
def fazer():
 #ABRE O NAVEGADOR
    navegador=webdriver.Chrome(options=options)
    #ABRE A PÁGINA DO GRÁFICO
    navegador.get("https://br.tradingview.com/chart/?symbol=BMFBOVESPA%3AIBOV")
    time.sleep(2)
    #CLICA NAS OPÇÕES PARA DOWLOAD
    navegador.find_element('xpath','//*[@id="header-toolbar-screenshot"]/span').click()
    time.sleep(2)
    navegador.find_element('xpath','//*[@id="overlap-manager-root"]/div/span/div[1]/div/div/div[2]/span[1]').click()
    time.sleep(5)
    #SAI DO NAVEGADOR
    navegador.quit()
    time.sleep(10)
#schedule.every(4).weeks.at("07:00").do(fazer)    
schedule.every(50).seconds.do(fazer)
#SEMPRE EM EXECUÇAO
while True:
    ##navegador=webdriver.Chrome(options=options)
    schedule.run_pending()
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




