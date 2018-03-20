>>> #buat tuple a yang berisi 4 bilangan positif pertama dan tuple b yang berisi 4 bilangan bulat positif berikutnya
>>> a = (1, 2, 3, 4)
>>> b = (5, 6, 7, 8)
>>> #buat tuple c yang menggabungkan semua angka a dan b
>>> c = a+b;
>>> print c
(1, 2, 3, 4, 5, 6, 7, 8)
>>> #buat tuple d yang merupakan salinan dari c
>>> d = c;
>>> print d
(1, 2, 3, 4, 5, 6, 7, 8)
>>> #cetak elemen ketiga d
>>> print d[2]
3
>>> #cetak 3 elemen terakhir dari d tanpa menggunakan panjangnya
>>> print d[-3:8]
(6, 7, 8)
>>> #cetak panjang d
>>> print len(d)
8
>>> 
