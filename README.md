# This is Readme how to use model
###### Don't forget to create branch 

##### NOTES
buat model resnet masih sangat kurang
gua belum tau cara optimize resnet
kalo bisa sambil di eksplore dan open buat bikin model-model baru oke ges


##Ini berlaku kesemua model

#### Step 1
![Step1](https://cdn.discordapp.com/attachments/463595205308841984/1114490564163936277/image.png)

Ubah variable <code>source_path_train</code> dan <code>source_path_test</code>
kearah folder train dan test kalian

#### Step 2

perlu diperhatikan tidak semua image kita itu sesuai. Ada kemungkinan image kita merupakan corrupt file.
![Step5](https://cdn.discordapp.com/attachments/463595205308841984/1114499891398443008/image.png)

block kode itu ada di fungsi <code>train_val_generator</code>. 
Jadi nanti dia akan print letak serta nama file yang corrupt
setelah tau file yang corrupt, delete file itu secara manual

![Step6](https://cdn.discordapp.com/attachments/463595205308841984/1114500496330342451/image.png)

nanti setelah kalian run block ini akan terlihat file apa yang corrupt. 
Kebetulan disini tidak ada file corrupt jadi dia tidak print file apa apa.

Ubah variable <code>source_path_train</code> dan <code>source_path_test</code>
kearah folder train dan testing kalian

#### Step 3
Pada bagian function <code>create_final_model</code>
![Step3](https://cdn.discordapp.com/attachments/463595205308841984/1114492702256545904/image.png)

Ubah parameter di block <code>x = layers.Dense(16, activation='softmax')(x)</code>
"16" nya ganti sesuai dengan jumlah class tumbuhan yang kalian ingin klasifikasi (sejumlah folder train dan testing)


#### Step 4
Kalau sudah training pengen nyoba buat ngepredict make gambar sendiri pada bagian code dibawah ini perhatikan:
![Step4](https://cdn.discordapp.com/attachments/463595205308841984/1114492868137070674/image.png)
Variable <code>image_path</code> ganti pathnya sesuai sama path dari image yang mau di predict.
