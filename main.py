from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import yagmail #pip install yagmail
import time as t 
from meusdados_1 import MeusDados



def conexao():
    
    global navegador
    
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    navegador.get(r'https://web.whatsapp.com/') 

             
    while True:
        try:
            navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]').click()
            break

        except:
            
            print('Aguardando Login via QR Code...')
            t.sleep(15)
            

    print('Prosseguindo...\n\n')



def adaptar_item(item):
    if item < 10:
        
        return '0' + str(item)
    else:
        return item  



def hora_setup():
    return f'{adaptar_item(dia)}/{adaptar_item(mes)}/{ano} - {adaptar_item(hora)}:{adaptar_item(minuto)}'



def msg_wpp():
    dual_text = ['\nPreparando para iniciar...', f'Enviando MENSAGEM para {nome_destino}']
    print('\n'.join(dual_text))
    
    
    try:
        
        global cont_dose
        
        ####### Dado Referência 
        with open('DadosMutaveis.txt','r') as cont_dose:
            cont_dose = int(cont_dose.read())
        
          
        cont_dose_atual = cont_dose + 1
        texto = f'não esqueça de tomar o seu remédio!\n{cont_dose_atual}º dose'


        navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]').send_keys(nome_destino, Keys.ENTER)
        navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(texto, Keys.ENTER)
        
        print('Mensagem Enviada!')
        
        
        ############ Dado Mutávei
        with open('DadosMutaveis.txt','w') as f:
            f.write(str(cont_dose_atual))
        
        
    except:
        return 'Não foi possível enviar a mensagem'
    
    
    finally:
        print('Passando para a próxima tarefa.\n\n')



def enviar_email():
    
    
    print(f'Preparando para iniciar o processo de enviar EMAIL para {nome_destino}')
    
    meu_email = MeusDados()
    minha_senha = MeusDados(2) 
    usuario = yagmail.SMTP(user=meu_email,password=minha_senha)


    assunto_email ='remedioooo'

    html = f"""
    <h1>OLá, {nome_destino}!</h1>
    
    Não esquece de tomar seu remédio
    
    
    Atenciosamente,
    Fulano de Tal
    """
    yagmail.inline('algumaimg.jpg')


    try:
        usuario.send(
        to=email,
        subject=assunto_email,
        contents=html) 
        print('Email Enviado!')
    
    
    except:
        print('Não foi possível enviar o Email')

    
    

############ Dados Destino        
nome_destino = 'fulano'
email = 'fulano@gmail.com'



########## execução
conexao() 

contador  = 0
while True:
    
    data_atual = t.localtime()
    ano, mes, dia, hora, minuto, seg, dia_semana, dia_ano, isdst = data_atual
    
    
    if hora in [23, 7, 15]:
        
        msg_wpp()
        enviar_email()
        
        print('Funcionamento do programa entrará em repouso por 1hr.') # pois senão ficará enviando mensagem toda hora
        t.sleep(3601)
                
        
    else:
        contador += 1
        print(f'No aguardo da hora correta. {contador}º tentativa - Feita às {hora_setup()}')
        t.sleep(30)
