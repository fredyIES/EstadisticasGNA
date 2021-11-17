import pandas as pd

df = pd.read_csv("random.csv")
print(df)
counts = df.value_counts()

print(counts)
print(dict(counts))

""" ini = 0
fin = 5

sub = df[0:5]
print(sub)

sub = df[ini:fin]
print(sub)
 """

def partialFrecuency(dataFrame,sizeGroups,maxGroups=10):
    print("----------------")
    ini = 0
    end = sizeGroups
    for i in range(maxGroups):
        print(ini + sizeGroups)
        newDf = dataFrame[ini:end].value_counts()
        print(dict(newDf))
        ini = end
        end = end + sizeGroups
        print(newDf[0])


partialFrecuency(df,5)