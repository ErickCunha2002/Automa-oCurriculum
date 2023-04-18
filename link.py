from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

EMAIL='erick-pirata4@hotmail.com'
SENHA='Erick1@3$5'

url='https://www.linkedin.com/jobs/search/?currentJobId=3551928327&f_LF=f_AL&geoId=106057199&keywords=desenvolvedor%20python&location=Brazil&refresh=true'


def Enviar_Curriculum():
    drive=webdriver.Chrome()
    drive.get(url=url)

    botao = drive.find_element(By.LINK_TEXT, "Entrar")
    botao.click()

    email_input = drive.find_element(By.ID, "username")
    email_input.send_keys(EMAIL)

    senha_input = drive.find_element(By.ID, "password")
    senha_input.send_keys(SENHA)

    botao_entrar = drive.find_element(By.XPATH, "//button[@type='submit']")
    botao_entrar.click()

    botao_easy_apply = WebDriverWait(drive, 3).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='Easy Apply']/ancestor::button"))
    )
    botao_easy_apply.click()

    botao_next = drive.find_element(By.CSS_SELECTOR,"button[data-easy-apply-next-button='']")
    botao_next.click()

    botao_next2 = drive.find_element(By.CSS_SELECTOR,'button#ember384.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view')
    botao_next2.click()

    sleep(500)

Enviar_Curriculum()