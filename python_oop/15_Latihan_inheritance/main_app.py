# Latihan inheritance

# pada materi latihan encapsulasi sebelumnya
# kita sudah membuat sistem level dan experiencce ke dalam program Servant kita

# latihan kali ini kita akan mencoba menggunakan tipe-tipe sub class dari Servant
# seperti saber, archer, dan lancer yang memiliki sifat dan attribute yang berbeda-beda

from Servant import ServantSaber, ServantArcher, ServantLancer

artoria = ServantSaber('Artoria')
gilgamesh = ServantArcher('Gilgamesh')
chu_chulain = ServantLancer('Chu Chulain')

artoria.showInfo()
gilgamesh.showInfo()
chu_chulain.showInfo()

artoria.gainExp = 300
gilgamesh.gainExp = 350
chu_chulain.gainExp = 400

artoria.showInfo()
gilgamesh.showInfo()
chu_chulain.showInfo()





