from bs4 import BeautifulSoup
import requests, re

res = requests.get('http://vestnikrayona.ru/map-site/')
#soup = BeautifulSoup(res.text, features="html.parser")
#news = soup.find_all('li')
news = re.findall("<li><a .+?\.html'>.+?<\/a><\/li>", res.text, re.S)
hrefs = [re.findall(r"href='(.+?)'", r, re.S)[0]for r in news]

with open ('laba2.txt', 'w', encoding='utf-8') as f:
    for url in hrefs:
        source = '"Вестник района"'
        url = str(url)
        url = 'http://vestnikrayona.ru/' + url
        res2 = requests.get(url)
        res3 = res2.text
        date = (re.findall(r"<div class='date'>(.+?)</div>", res3, re.S))
        if not date:
            continue
        else:
            date = date[0]
        res3 = res3.replace("\n", "")
        res_soup = BeautifulSoup(res3, features="html.parser")
        author = res_soup.find('h4').get_text()
        if author == 'Каталог организаций': 
            author = 'Автор не указан'
        author = re.sub(r'[.,]$', '', author)
        name = (re.findall(r"<meta name='description' content='(.+?)' />", res2.text))[0]
        text = res_soup.find(class_='bigtext')
        if not text:
            text = 'текст отсутствует'
        else:
            text = text.get_text() 
            text = text.strip()
            text = text.replace("Продолжение Вы можете прочитать в электронной версии газеты.", "")
            text = text.replace('Полную версию статьи читайте в газете "Вестник района"', '')
            
        unit = '====='+'\n'+str(url)+'\n'+str(source)+'\n'+str(date)+'\n'+str(author)+'\n'+str(name)+'\n'+str(text)+'\n'
        f.write(unit)
