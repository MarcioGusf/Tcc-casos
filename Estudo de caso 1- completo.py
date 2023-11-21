#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import time
import os
#Modificando as opções do navegador antes de abrir, estamos desligando as notificações do navegador, 
#para acelerar a velocidade do processo e não haver interrupções
options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}

options.add_experimental_option("prefs",prefs)
#Formas antigas de salvar um navegador na máquina, varia de cada versão
#navegador=webdriver.Chrome('C:\\Program Files\\Google\\Chrome\\Application\\chrome')
#navegador=webdriver.Chrome('C:\\Users\\Rasca\\.cache\\selenium\\chromedriver\\win64\\116.0.7777.97
#\\chromedriver.exe', chrome_options=chrome_options)
navegador=webdriver.Chrome(options=options)


# In[71]:


#escolha das entradas
mensagem='Teste tcc'
foto= "C:\\Users\\Rasca\\Downloads\\tcc im.png"


# In[72]:


###Instagram


# In[73]:


#entra na pagina inicial do instagram
navegador.get("https://www.instagram.com/")
time.sleep(4)
#escreve na caixa de texto o nome de usuario
navegador.find_element('xpath','//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("tccteste123")
time.sleep(1)
#escreve na box da senha a senha
navegador.find_element('xpath','//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("tccteste123##")
time.sleep(1)
#clica no botão de login
navegador.find_element('xpath','//*[@id="loginForm"]/div/div[3]/button').click()
time.sleep(10)


# In[74]:


#recusa a primeira informaçao do instagran
navegador.find_element('xpath','/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div').click()
time.sleep(4)


# In[75]:


#notnow click , n foi necessario pq removemos notificaçoes do google
#navegador.find_element('xpath','/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
##time.sleep(2)


# In[76]:


#clicka no botao para a publicaçao
navegador.find_element('xpath','/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/span/div/a/div').click()
time.sleep(20)


# In[77]:


#Arrasta a foto
navegador.find_element('xpath','/html/body/div[8]/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/form/input').send_keys(foto)

time.sleep(15)


# In[78]:


## segue as etapas "next" para publicar
navegador.find_element('xpath','/html/body/div[8]/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/div').click()
time.sleep(10)
navegador.find_element('xpath','/html/body/div[8]/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/div').click()
time.sleep(10)
##escreve a msg
navegador.find_element('xpath','/html/body/div[8]/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[1]').send_keys(mensagem)
time.sleep(10)
navegador.find_element('xpath','/html/body/div[8]/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/div').click()
time.sleep(10)


# In[79]:


##Facebook


# In[80]:


#Navega para a pagina do Facebook 
navegador.get("https://www.facebook.com/")
time.sleep(4)
#escreve o login na box de nome de usuario
navegador.find_element('xpath','/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input').send_keys("tccteste@outlook.com.br")
time.sleep(1)
#escreve a senha na box da senha
navegador.find_element('xpath','/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input').send_keys("tccteste##")
time.sleep(1)
#clica no login
navegador.find_element('xpath','/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()
time.sleep(4)


# In[81]:


#navega para a pagina principal de postagem do face
navegador.get("https://www.facebook.com/")
#rascunho caso seja feito via botao,achei mt lento por isso fiz via navegaçao msm
#navegador.find_element('xpath','//*[@id="mount_0_0_Z0"]/div/div[1]/div/div[2]/div[4]/div/div[1]/div[1]/ul/li[1]/span/div/a').click()
#time.sleep(3)
#navegador.find_element('xpath','/html/body/div[1]/div/div[1]/div/div[2]/div[1]/a').click()
time.sleep(2)
#processo para a postagem
navegador.find_element('xpath','/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div').click()
time.sleep(4)
navegador.find_element('xpath','/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]').click()
time.sleep(3)

navegador.find_element('xpath','/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[1]/div[1]/div').click()
time.sleep(3)
navegador.find_element('xpath','/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[2]/div/div/div/div[2]/div[1]/div/div/div').click()
time.sleep(5)


# In[82]:


#envio da foto pelo face
navegador.find_element('xpath','/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/div/div/input').send_keys(foto)
time.sleep(5)


# In[83]:


#mensagem escolhida
navegador.find_element('xpath','/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div[1]').send_keys(mensagem)
time.sleep(3)


# In[84]:


#botao de postagem
navegador.find_element('xpath','/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div/div/div[1]/div/span').click()
time.sleep(3)


# In[85]:


##(X)Twitter


# In[86]:


#navega para a pagina do twiter(X)
navegador.get("https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJsYW5nIjoicHQifQ%3D%3D%22%7D")
time.sleep(2)


# In[87]:


#preenche o login
navegador.find_element('xpath','//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys("tccteste123")
time.sleep(3)


# In[88]:


#clica em seguir para ser possivel colocar a senha
navegador.find_element('xpath','//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span').click()
time.sleep(5)


# In[89]:


#coloca a senha
navegador.find_element('xpath','//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys("tccteste123##")
time.sleep(2)


# In[90]:


#clica no botao de login
navegador.find_element('xpath','//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span').click()
time.sleep(5)


# In[91]:


#adiciona a foto e mensagem diretamente sem clicar na box o site X possui uma facilidade a mais
navegador.find_element('xpath','//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div').send_keys(mensagem)
time.sleep(1)
navegador.find_element('xpath','//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/input').send_keys(foto)
time.sleep(1)


# In[92]:


#clica no botao de publicar
navegador.find_element('xpath','//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/span').click()
time.sleep(2)


# In[93]:


#sai do navegador
navegador.quit()


# In[ ]:





# In[ ]:




