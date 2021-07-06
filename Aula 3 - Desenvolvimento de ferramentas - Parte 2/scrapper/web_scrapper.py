from bs4 import BeautifulSoup
import requests

site = requests.get("https://www.climatempo.com.br").content

#objeto site recebendo o conteudo da requisicao
soup = BeautifulSoup(site, "html.parser")
#objeto soup baixando o html do site
#print(soup.prettify())
#transforma o html em string

risco = soup.find("a", class_="actTriggerGA")

print(risco.string)
print(soup.title)
print(soup.title.string)
print(soup.a)
print(soup.p.string)
print(soup.find("admin"))