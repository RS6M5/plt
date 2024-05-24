import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# URL страницы, которую будем парсить
url = 'https://www.divan.ru/category/divany'

# Получение HTML-кода страницы
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Поиск всех элементов, содержащих информацию о цене
prices = []
for price_tag in soup.find_all(class_='price-class'):  # Замените 'price-class' на реальный класс цены на сайте
    price = price_tag.text.strip()
    price = int(price.replace(' ', '').replace('₽', ''))  # Удаление пробелов и символа рубля
    prices.append(price)

# Сохранение данных в CSV файл
df = pd.DataFrame(prices, columns=['Price'])
df.to_csv('sofa_prices.csv', index=False)

# Вычисление средней цены
mean_price = df['Price'].mean()
print(f'Средняя цена на диваны: {mean_price} рублей')

# Построение гистограммы цен
plt.hist(df['Price'], bins=30, edgecolor='black')
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена (рубли)')
plt.ylabel('Частота')
plt.show()