Creează un program Python care generează un set de date simplu, îl salvează într-un fișier CSV și apoi creează un grafic din aceste date folosind biblioteca Matplotlib.import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Generarea unui set de date simplu
data = {
    'X': np.arange(1, 11),
    'Y': np.random.randint(1, 100, 10)
}
df = pd.DataFrame(data)
# Salvarea setului de date într-un fișier CSV
csv_file = 'date_simplu.csv'   
df.to_csv(csv_file, index=False)
print(f'Setul de date a fost salvat în fișierul {csv_file}')
# Crearea unui grafic din datele salvate
plt.figure(figsize=(10, 6))
plt.plot(df['X'], df['Y'], marker='o')
plt.title('Grafic simplu din datele CSV')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.savefig('grafic_simplu.png')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
# Citirea datelor din fișierul CSV  
# df = pd.read_csv(csv_file)
# Crearea unui grafic din datele citite
# plt.figure(figsize=(10, 6))
# plt.plot(df['X'], df['Y'], marker='o')
# plt.title('Grafic simplu din datele CSV')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.grid()
# plt.savefig('grafic_simplu.png')
# plt.show()
# Notă: Linia de cod pentru citirea datelor din fișierul CSV și crearea graficului din aceste date este comentată, deoarece datele sunt deja disponibile în DataFrame-ul `df`. Dacă doriți să citiți din fișierul CSV, puteți decomenta acele linii.
# Acest program generează un set de date cu valori aleatoare, le salvează într-un fișier CSV și creează un grafic liniar din aceste date, salvând graficul ca imagine PNG.import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Generarea unui set de date simplu
# data = {
#     'X': np.arange(1, 11),        
#    'Y': np.random.randint(1, 100, 10)
# }
# df = pd.DataFrame(data)
# Salvează DataFrame-ul în fișiere CSV.
# csv_file = 'date_simplu.csv'
# df.to_csv(csv_file, index=False)
# print(f'Setul de date a fost salvat în fișierul {csv_file}')
# Crearea unui grafic din datele salvate    
# plt.figure(figsize=(10, 6))
# plt.plot(df['X'], df['Y'], marker='o')
# plt.title('Grafic simplu din datele CSV')
# 
# Adaugă valori numerice deasupra fiecărui punct din grafic.plt.xlabel('X')
# plt.ylabel('Y') 
# plt.grid()
# 
# Adaugă etichete de valori deasupra punctelor
 for i in range(len(df)):
   plt.text(df['X'][i], df['Y'][i] + 1, str(df['Y'][i]), ha='center')
 plt.savefig('grafic_simplu.png')
 plt.show()
# Salvează graficul în fișierul "vanzari_grafic.png" 
# Notă: Linia de cod pentru citirea datelor din fișierul CSV și crearea graficului din aceste date este comentată, deoarece datele sunt deja disponibile în DataFrame-ul `df`. Dacă doriți să citiți din fișierul CSV, puteți decomenta acele linii.
# Acest program generează un set de date cu valori aleatoare, le salvează într-un fișier CSV și creează un grafic liniar din aceste date, salvând graficul ca imagine PNG.
 import pandas as pd
 
import matplotlib.pyplot as plt
import numpy as np
Generarea unui set de date simplu
  
data = {
     'X': np.arange(1, 11),
    'Y': np.random.randint(1, 100, 10)
}
 df = pd.DataFrame(data)
Salvează DataFrame-ul în fișiere CSV.
 csv_file = 'date_simplu.csv'
 df.to_csv(csv_file, index=False)   
print(f'Setul de date a fost salvat în fișierul {csv_file}')
Crearea unui grafic din datele salvate    
 plt.figure(figsize=(10, 6))
 plt.plot(df['X'], df['Y'], marker='o')
 plt.title('Grafic simplu din datele CSV')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid()
