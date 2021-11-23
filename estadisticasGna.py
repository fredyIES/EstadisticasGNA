import pandas as pd

def lenVentana(len_muestras, num_entradas=1):
  return len_muestras*num_entradas

def ventanaValida(len_total, len_ventana, cant_grupos=10):
  return len_total >= len_ventana * cant_grupos

def listaEnventanada(df,len_ventana, nombre_columna):
  L=df[nombre_columna].to_numpy()
  newL= []
  fin=len_ventana
  ini=0
  for i in range(len(df)//len_ventana):
    newL.append(list(L[ini:fin]))
    ini=fin
    fin+=len_ventana
  return newL

def listaEnventanadaAleatoria(L, cant_grupos):
  from random import choice
  newL=[]
  for i in range(cant_grupos):
    r=choice(L)
    newL.append(r)
    L.remove(r)
  return newL

def dicInicial(num_muestras):
  dic={}
  for i in range(1, num_muestras+1):
    dic[str(i)]=0
  return dic

def tablaFrecuencias(L, num_muestras, len_ventana):
  print()
  dic=dicInicial(num_muestras)
  lista_datos=[]
  for i in L:
    for j in i:
      if str(j) in dic:
        dic[str(j)]+=1
    
    P=len_ventana/num_muestras
    error_absoluto=0
    aux=dic.values()
    for j in aux:
        error_absoluto+=abs(P-j)

    error_absoluto=error_absoluto/len_ventana
    error_relativo=(error_absoluto/P)*100
    lista_datos.append([str(dic),P,error_relativo])

    print(dic)
    print("teórico =", P)
    print("Porcentaje de error=",error_relativo)
    print()
    print("---------------*****---------------")
    print()
    dic=dicInicial(num_muestras)
  df_datos=pd.DataFrame(lista_datos,
                  columns=["Tabla de frecuencias", "Promedio", "Teoria"])
  return df_datos

def guardarDatos(df,nombre_archivo):
  df.to_csv(nombre_archivo+".csv", index=False, sep=";", encoding="utf-8")

def frecuenciaParcial(df, num_entradas=1, cant_grupos=10):
  num_muestras = len(df.value_counts())
  len_ventana = lenVentana(num_muestras, num_entradas)
  print("Número de muestas:", num_muestras, "Tamaño de la ventana:",len_ventana)
  if (ventanaValida(len(df), len_ventana,cant_grupos)):
    print("Posible")
    L=listaEnventanada(df, len_ventana, 'gna')
    print("Lista enventanada:", L)
    L=listaEnventanadaAleatoria(L, cant_grupos)
    print("Lista enventanada aleatoria:", L)
    df_result=tablaFrecuencias(L,num_muestras, len_ventana)
    guardarDatos(df_result,"data_ruleta")
  else:
    print("No es posible realizar esta prueba")



ruta = "GNA_ruleta.csv"
df = pd.read_csv(ruta)

frecuenciaParcial(df, 4, 10)