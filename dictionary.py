>>> #masukkan data nomor telpon
>>> no_telpon = { "nama" : ["Jane doe", "John Smith", "Bob Stone"], "Telephone Number" : ["+27 555 5367", "+27 555 6254", "+27 555 5689"] }
>>> #ubah nomor telpon Jane dengan nomor +27 555 1024
>>> no_telpon["Telephone Number"][0] = "+27 555 1024"
>>> no_telpon
{'nama': ['Jane doe', 'John Smith', 'Bob Stone'], 'Telephone Number': ['+27 555 1024', '+27 555 6254', '+27 555 5689']}
>>> #tambahkan data baru dengan nama Anna Cooper dengan no telpon +27 555 3237
>>> no_telpon.update({ "nama" : ["Jane doe", "John Smith", "Bob Stone", "Anna Cooper"], "Telephone Number" : ["+27 555 1024", "+27 555 6254", "+27 555 5689", "+27 555 3237"] })
>>> no_telpon
{'nama': ['Jane doe', 'John Smith', 'Bob Stone', 'Anna Cooper'], 'Telephone Number': ['+27 555 1024', '+27 555 6254', '+27 555 5689', '+27 555 3237']}
>>> #cetak nomor telpon Bob
>>> no_telpon["Telephone Number"][2]
'+27 555 5689'
>>> #cetak semua Key dari dictionary
>>> no_telpon.keys()
['nama', 'Telephone Number']
>>> #cetak semua Value dari dictionary
>>> no_telpon.values()
[['Jane doe', 'John Smith', 'Bob Stone', 'Anna Cooper'], ['+27 555 5367', '+27 555 6254', '+27 555 5689', '+27 555 3237']]
>>> 
