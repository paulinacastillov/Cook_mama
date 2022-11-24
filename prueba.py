from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

lista_ingredientes = []
paso_receta = []

driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\chromedriver.exe")
driver.get("https://www.recetasgratis.net/")

def buscando():
	buscar_ing = driver.find_element(By.ID, "q")
	buscar_ing.send_keys("pan")
	buscar_ing.send_keys(Keys.ENTER)

def hacer_click(lista_ingredientes,paso_receta):
	result = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div[2]/div[1]/div/div[3]")
	result.click()
	obtener_ingredientes(lista_ingredientes)
	obtener_pasos(paso_receta)

def obtener_ingredientes(lista_ingredientes):
	ingredientes =  driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/article/div[2]/div[4]/div[4]")
	ingredientes = ingredientes.text
	lista_ingredientes.append(ingredientes)

def obtener_pasos(paso_receta):
	pasos =  driver.find_element(By.XPATH, "//*[@id='anchor_0']/p[1]")
	pasos = pasos.text
	paso_receta.append(pasos)
	driver.back()

buscando()
hacer_click(lista_ingredientes,paso_receta)

print(lista_ingredientes,type(lista_ingredientes))
print(paso_receta)