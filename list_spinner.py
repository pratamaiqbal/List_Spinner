def counterClokcwise(listinput):
    hasil = [[],[],[]]
    for i in listinput: # for ini untuk mengakses data atau list dalam list input iterasi 1 : [1,2.3] 2 : [4,5,6] 3 : [7,8,9]
        for j in i: # for ini untuk mengakses data dalam i, iterasi pertama pada i awal adalah 1, kedua adalah 2 , ketiga adalah 3, dan seterusnya hingga i akhir iterasi ketiga 
            if i.index(j) == 2 : # jika indeks j pada i adalah 2, maka data akan ditambahkan pada list hasil di indeks ke 0
                hasil[0].append(j)
            elif i.index(j) == 1 : # jika indeks j pada i adalah 1, maka data akan ditambahkan pada list hasil di indeks ke 1
                hasil[1].append(j)
            elif i.index(j) == 0 : # jika indeks j pada i adalah 0, maka data akan ditambahkan pada list hasil di indeks ke 2
                hasil[2].append(j)
    return hasil


listawal = [[1,2,3],
            [4,5,6],
            [7,8,9]]

a = counterClokcwise(listawal) # untuk menampung list hasil
print(counterClokcwise(listawal)) # hasil list setelah diputar
print("")
print(f"[{a[0]},\n{a[1]},\n{a[2]}]") # hasil agar terlihat list sudah diputar berlawanan jarum jam

