import openpyxl
import pandas as pd

df = pd.DataFrame({'Osoba': ["Michał Jakub", "Ewa Noga", 'Krzysztof Zawierucha'],
                   'Wynik': [15, 38, 21]})


def sprawdz(punkty):
    if punkty > 20:
        return 'Zdany'
    else:
        return 'Oblany'


print(df)
df.Wynik = df.Wynik.apply(sprawdz)
print(df)
#                   Osoba  Wynik
# 0          Michał Jakub     15
# 1              Ewa Noga     38
# 2  Krzysztof Zawierucha     21
#                   Osoba   Wynik
# 0          Michał Jakub  Oblany
# 1              Ewa Noga   Zdany
# 2  Krzysztof Zawierucha   Zdany

df.to_csv("wynik.csv")
df.to_excel("wynik.xlsx")
df.to_excel("wynik2.xlsx", index=False)
