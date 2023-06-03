# This is Readme how to use model
###### Don't forget to create branch ges

Untuk menggunakan model model ini buat testing kita perlu ada beberapa yang diganti yak.
##### NOTES
buat model resnet masih sangat kurang
gua belum tau cara optimize resnet
kalo bisa sambil di eksplore dan open buat bikin model-model baru oke ges


##### Ini berlaku kesemua model

#### Step 1
![Step1](https://cdn.discordapp.com/attachments/463595205308841984/1114490564163936277/image.png)

Ubah variable <code>source_path_train</code> dan <code>source_path_test</code>
kearah folder train dan testing kalian

#### Step 2

perlu diperhatikan tidak semua image kita itu akan bisa dibuka. Ada kemungkinan image kita merupakan corrupt file.
![Step5](https://cdn.discordapp.com/attachments/463595205308841984/1114499891398443008/image.png)

block kode itu ada di fungsi <code>train_val_generator</code>. Jadi nanti dia akan nge print letak serta anam file yang corrupt

![Step6](https://cdn.discordapp.com/attachments/463595205308841984/1114500496330342451/image.png)

nanti setelah kalian run ini akan keliatan file apa yang corrutp. kebetulan disini tidak ada jadi dia tidak print file apa apa.

Ubah variable <code>source_path_train</code> dan <code>source_path_test</code>
kearah folder train dan testing kalian

#### Step 3
Pada bagian function <code>create_final_model</code>
![Step3](https://cdn.discordapp.com/attachments/463595205308841984/1114492702256545904/image.png)

ubah parameter di block <code>x = layers.Dense(16, activation='softmax')(x)</code>
16 nya ganti sesuai dengan jumlah class tumbuhan yang kalian ingin klasifikasi (sejumlah folder train dan testing)


#### Step 4
Kalau sudah training pengen nyoba buat ngepredict make gambar sendiri pada bagian code dibawah ini perhatikan:
![Step4](https://cdn.discordapp.com/attachments/463595205308841984/1114492868137070674/image.png)
Variable <code>image_path</code> ganti pathnya sesuai sama path dari image yang mau di predict.
