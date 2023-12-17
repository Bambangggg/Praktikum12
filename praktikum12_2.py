import pandas as pd

df = pd.read_csv('negara.csv', index_col=0)

mean = df.groupby(['Benua']).mean(numeric_only=True)[['Luas', 'Populasi']]
std = df.groupby(['Benua']).std(numeric_only=True)[['Luas', 'Populasi']]

mean.to_csv('NegaraMean.csv')
std.to_csv('NegaraStandarDeviasi.csv')

print("Data Mean:")
print(mean)
print("\nData Standar Deviasi:")
print(std)
