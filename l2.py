from bs4 import BeautifulSoup
import requests, re

res = requests.get('http://vestnikrayona.ru/arhiv/2016/02/')
soup = BeautifulSoup(res.text, features="html.parser")
news = soup.find_all('h2')

with open ('laba2.txt', 'w', encoding='utf-8') as f:

    for url in news:
        source = '"Вестник района"'
        url = re.findall('href=\"(.+html)\"', str(url))
        url = 'http://vestnikrayona.ru/' + str(url[0])
        res2 = requests.get(url)
        res3 = res2.text
        res3 = res3.replace("\n", "")
        res_soup = BeautifulSoup(res3, features="html.parser")
        date = (re.findall(r"<div class='date'>(.+?)</div>", res2.text, re.S))[0]    
        author = res_soup.find('h4').get_text()
        if author == 'Каталог организаций': 
            author = 'Автор не указан'
        author = re.sub(r'[.,]$', '', author)
        name = (re.findall(r"<meta name='description' content='(.+?)' />", res2.text))[0]
        text = res_soup.find(class_='bigtext').get_text() 
        text = text.strip()
        text = text.replace("Продолжение Вы можете прочитать в электронной версии газеты.", "")
        text = text.replace('Полную версию статьи читайте в газете "Вестник района"', '')
        text = re.sub(r"\n*", "", text)
        
        unit = '====='+'\n'+str(url)+'\n'+str(source)+'\n'+str(date)+'\n'+str(author)+'\n'+str(name)+'\n'+str(text)+'\n'
        f.write(unit)
