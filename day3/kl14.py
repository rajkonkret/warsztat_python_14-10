import pickle

lista = [1, 2, 3, 4, 5]
print(type(lista))  # <class 'list'>
# ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
# context manager - ułatwia bezpieczną pracę z plikami
with open('lista.txt', 'w') as f:
    f.write(str(lista))

with open('lista.txt', "r") as fh:
    lines = fh.read()

print(lines)  # [1, 2, 3, 4, 5]
print(lines[0])  # [
print(type(lines))  # <class 'str'>

# serializacja - zamian obiektu na bajty
# wb - zapis bajtowy
with open('lista.pickle', 'wb') as f:
    pickle.dump(lista, f)

# deserializacja
with open('lista.pickle', 'rb') as fh:
    p = pickle.load(fh)

print(p)  # [1, 2, 3, 4, 5]
print(type(p))  # <class 'list'>

lista_ser = pickle.dumps(lista)
print(lista_ser)  # b'\x80\x04\x95\x0f\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03K\x04K\x05e.'
print(type(lista_ser))  # <class 'bytes'>
print(pickle.loads(lista_ser))  # [1, 2, 3, 4, 5]

for i in pickle.loads(lista_ser):
    print(i, sep=" : ", end=" : ")  # sep=' ', 1 : 2 : 3 : 4 : 5 :
