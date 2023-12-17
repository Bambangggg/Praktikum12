'''import pandas as pd
data = {"Negara": ["Indonesia", "Jepang", "India", "China", "Amerika Serikat", "Brazil"],
        "ibukota": ["jakarta", "Tokyo", "New Delhi", "Beijing", "Washington D.C", "Brazilia"],
        "benua" : ["Asia", "Asia", "Asia", "Asia", "Amerika", "Amerika"],
        "Luas": [11905, 377, 3287, 9597, 9834, 85151],
        "Populasi": [1264, 143, 1252, 1357, 329, 2101] 
        }
df = pd. DataFrame(data)
mean = df. groupby( ['Benua' ]).mean ()
std = df. groupby([ 'Benua']).std()

print(df)
print (mean)'''

import pandas as pd

df = pd.read_csv('negara.csv', index_col=0)
mean = df.groupby(['Benua']).mean(numeric_only=True)
std = df.groupby(["Benua"]).std(numeric_only=True)

print("maka data nya :")
print(df)
print("\nmaka mean nya : ")
print(mean)
print("\n maka deviasi nya :")
print(std)


