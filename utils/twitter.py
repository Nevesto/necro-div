import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



def twitter():
    print("Nunca use sua conta principal, compre uma ou crie para fazer sua div.")
    user = input('Coloque o user da sua conta: ')   
    password = input('Coloque a senha da sua conta: ') 
    message = input("Mensagem a ser enviada: ")

    perfis = [
        'https://twitter.com/nosredreal',
        'https://twitter.com/Choquei_Trap',
        'https://twitter.com/bbb',
        'https://twitter.com/ladroesfora',
        'https://twitter.com/pessoascfu'
    ]
    
    driver = webdriver.Chrome()

    for link in perfis:
        driver.get(link)
        print('Entrando no pagina: {link}')
        time.sleep(2)
        login_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[1]/div/div/div/div/div/div/div/div[1]/a")
        login_button.click()
        time.sleep(5)
        user_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        user_input.send_keys(user)
        time.sleep(1)
        next_user_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div")
        next_user_button.click()
        time.sleep(3)
        password_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        password_input.send_keys(password)
        time.sleep(1)
        next_password_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div")
        next_password_button.click()
        print('Login finalizado na conta:' + user)
        time.sleep(8)
        post = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[1]/div/div/article/div/div/div[2]/div[1]')
        post.click()
        print('Starting div on:' + link)
        time.sleep(10)
        comment_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[5]/div/div/div[1]/div')
        comment_button.click()
        time.sleep(5)
        comment_input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div/span')
        time.sleep(3)
        # comment_input.click()
        comment_input.send_keys(message)
        time.sleep(10)
        reply_input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/span/span')
        reply_input.click()
        print('Mensagem enviada: ' + message + ' no perfil: ' + link)
    driver.close()