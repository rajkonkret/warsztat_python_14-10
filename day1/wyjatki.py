# wyjątki
# błedy wykonywania programu
# należy obsłużyć
try:
    print("12" + 34)
except Exception as e:
    print("Bład", e)  # Bład can only concatenate str (not "int") to str
else:
    print("Wykonuje się gdy nie ma błedu")
finally:
    print("Wykona się zawsze")
print("Program nadal działa")  # Program nadal działa
# Bład can only concatenate str (not "int") to str
# Wykona się zawsze
# Program nadal działa
