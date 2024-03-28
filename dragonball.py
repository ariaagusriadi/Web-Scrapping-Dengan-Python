import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

alamat = "https://en.wikipedia.org/wiki/List_of_Dragon_Ball_episodes"
req = Request(alamat, headers={'User-Agent': 'Mozilla/5.0'})

html = urlopen(req).read()
data = BeautifulSoup(html, 'html.parser')
table = data.find_all('table', {'class': 'wikitable'})[0]
rows = table.findAll('tr')

hasil = []
for row in rows:
   cols = row.find_all('td')
   cols = [ele.text.strip() for ele in cols]
   hasil.append(cols)
   
df_hasil = pd.DataFrame(hasil)
df_hasil = df_hasil.drop([0], axis=0) # menghapus baris pertama
df_hasil.columns = ['Episodes', 'First Eps', 'Last Eps'] # memberi judul kolom tabel


# print(table)
# df_hasil = df_hasil.drop([0], axis=1) # menghapus kolom pertama
# df_hasil = df_hasil.drop([1], axis=0) # menghapus baris pertama
# print(df_hasil)

df_hasil.to_excel('test.xlsx', index=False)
print('Success')

