#FYOLA WAHYU KANAYA SALSABILA
#12220031
#tugas plot grafik

import string
import matplotlib.pyplot as plt
from PIL import Image
import streamlit as st

st.set_page_config(layout="wide")  # this needs to be the first Streamlit command called
st.title("Statistik Jumlah Penumpang TransJakarta Tahun 2019")
st.markdown("*Sumber data berasal dari [Jakarta Open Data](https://data.jakarta.go.id/dataset/data-jumlah-penumpang-trans-jakarta-tahun-2019-kpi)*")
punc = string.punctuation

#membuka file txt
file = open('preambule-uud-1945.txt')
file=file.read().lower()
unik={}

#mencari huruf unik dengan tidak memperhatikan tanda baca dan besar kecil huruf
for huruf in file:
    if huruf not in punc:
        if huruf != " " and huruf !="\n":
            unik[huruf] = unik.get(huruf, 0) + 1

list=[]
#melakukan input tuple kedalam sebuah list
for k, v in unik.items():
    list.append((v, k))

#sortir dari huruf yang paling banyak
list = sorted(list, reverse=True)

sbx = []
sby = []
#output huruf unik
for value, key in list:
    print ("huruf" , key, "ada", value)
    #input key dan value ke sebuah list
    sbx.append(key) 
    sby.append(value)

# Code untuk membuat bar charts 
plt.bar(sbx, sby, color ='green',width = 0.7)
plt.xlabel("Huruf Unik")
ax.set_xlabel("Huruf unik", fontsize=12)
plt.ylabel("Jumlah Huruf Unik")
plt.title("Huruf Unik dan Jumlahnya")
plt.savefig("Bar Plot Hitung Huruf")
plt.show()

ax.set_ylabel("Jumlah Huruf Unik", fontsize=12)
