## Cara Menggunakan Scripts berikut ini

#### IMPORTANT!!!
1. Jangan lupa sediakan folder image backup in case salah implemen dari script scirpt ini

#### Script 1
##### limit_image.py
script ini berguna buat ngelimit jumlah image yang ada di dalam satu folder
![Step1](https://cdn.discordapp.com/attachments/463595205308841984/1114495903601016903/image.png)

Buat script ini cuma perlu perhatiin line 5 dan 6
<code>train_folder</code> ini specify folder yang mau di limit apa. Misalnya mau limit folder training, maka ganti jadi path menuju folder training kalian.

<code>max_images_per_subfolder</code>: adalah jumlah maximum image di dalam folder tersebut

#### Script 2
##### move_image.py
Script ini berguna buat otomatisasi memindahkan image secara random untuk keperluan testing

train
  - Manggo
  - cherry

testing
  - (kosong)

Letakan seluruh image kalian di folder training. Lalu buat sebuah folder testing. Maka script ini bisa randomly mindahin data ke testing
Diatas adalah skema foldernya. 
sebelum runing scriptnya biarkan isi folder "testing" kosong. nanti dia otomatis buat folder dan move imagenya sekaligus
![Step2](https://cdn.discordapp.com/attachments/463595205308841984/1114497467292074025/image.png)

Buat script ini cuma perlu perhatiin line 4, 5 dan 6
<code>train_folder</code> Specify folder training dimana terletak folder-folder imagenya

<code>test_folder</code> ini path dimana letak folder "test". Di folder ini akan dibuat folder-folder baru sesuai dengan folder di  "train". Nanti akan dipindahkan image buat testing secara random dari folder train ke folder ini.

<code>num_images_to_move</code> jumlah image per class yang mau digunakan untuk testing.

#### Script 2
##### scriptrename.py
Script ini berguna buat otomatisasi ganti nama seluruh image

train
  - Manggo
  - cherry


scirpt ini akan rename seluruh image di folder testing

![Step3](https://cdn.discordapp.com/attachments/463595205308841984/1114498705186373772/image.png)

Buat script ini cuma perlu perhatiin line 3
<code>train_folder</code> Specify folder yang mau di rename image imagenya


