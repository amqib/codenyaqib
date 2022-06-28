"Seorang Guru ingin membagikan jumlah permen yang dimilikinya kepada  murid muridnya"
"Anak pertama mendapatkan satu permen dan seterusnya mendapatkan kelipatan dua dari jumlah permen yang diterima anak sebelumnya"
"Print Semua anak mendapatkan permen dan jumlah permen sisa jika permen yang dimiliki guru tersebut cukup"
"Jika jumlah permen tidak cukup, print sisa anak yang tidak mendapatkan permen dan jumlah permen yang diterima oleh penerima terakhir jika jumlah yang diterima tidak sesuai"

import math

kid = int(input())
candy = int(input())

for i in range(kid):
    candy = candy - 2**i
    print(candy, 2**i)
    if candy<0:
        rem = kid - i - 1
        last_candy = candy + 2**i
        break
    
if candy>=0:
    print("All kids get candies, candy remain : ", candy)
elif last_candy == 0:
    print("not enough candy, kid remain: {}".format(rem + 1))
else :
    print("The last kid only get {0} candies, kid remain: {1}".format(last_candy, rem))