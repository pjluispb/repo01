# importing pandas as pd
import pandas as pd
 
# Creating the dataframe
####df = pd.read_csv("Prondanmin23.csv", index_col='cedula')
df = pd.read_csv("Prondanmin23B.csv", index_col='cedula')
print(df.head(10))
###print(df.dtypes)
# Agrega fila al principio del df
#newRow = pd.DataFrame({'correo':'bettymar@ro.ck','Apellidos':'Marmol','Nombres':'Betty','cedula':int(7875554),'Teléfono':'0274 2447575','Distrito':'Andino','catAsp':'S/A','modalidad':'S/A','STATUS':'S/A'}, index=[0])
#df = pd.concat([newRow, df]).reset_index(drop = True)
# df.head(5)
#print(df.head(5))
# # Graba el df a un csv
#df.to_csv('Prondanmin23B.csv', encoding='utf-8', index=False)
try:
    first = df.loc[555333]
    
except:
    print('cedula No existe')
else:
    print(first)
# second = df.loc[7788]

# print(second)
 

