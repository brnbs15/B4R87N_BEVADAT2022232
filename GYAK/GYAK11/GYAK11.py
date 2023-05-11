import numpy as np

# Hozz létre egy bemeneti "képet" (numpy array-t)  (5x5)
# Az értékei legyenek 0 vagy 1
# dtype legyen np.float32
picture = np.array([[0,0,0,1,1],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1],[1,1,0,0,0]], dtype=np.float32)
width, height =  picture.shape[1],picture.shape[0]
# Hozz létre egy kernelt (numpy array-t)(3x3)
# Az értékei legyenek 0 vagy 1
# dtype legyen np.float32

# Mentsd el két külön változóba a létrehozott "kép" (5x5)
# dimenzióinak méretét (height,width)
kernel = np.array([[0, 1, 0],[1, 0, 1],[0, 1, 0]], dtype=np.float32)

# Mentsd el két külön változóba a létrehozott kernel (3x3)
# dimenzióinak méretét (height,width)
kernel_height,kernel_width = kernel.shape[0], kernel.shape[1]

# Számold ki a kimeneti "kép" dimenzióinak a méretét
padding = 0
stride = 1
# A magasságot és szélességet két külön változóba mentsd el
# NOTE: használd az előbb kiszámolt "kép" és kernel szélességet és magasságot
finalpict_height = (height-kernel_width)+(padding * 2)+ stride
finalpict_width = (width-kernel_height)+(padding * 2)+ stride


# Hozz létre egy az előbb kiszámolt kimeneti "kép"
# dimenziójával megegyező 0-kal feltöltött numpy array-t
finalpicture = np.zeros(shape=(finalpict_height,finalpict_width),dtype=np.float32)

# Hajts végire konvolúciót a bemeneti "képen"
# az eredményt az előbb létrehozott kimeneti "képbe" mentsd el
# NOTE: a kimeneti "kép" 1 db pixel értéke a bemeneti kép n darab értékének összegéből jön létre (n = amennyi nem 0 érték van a kernelben)
for i in range(finalpict_height):
    for j in range(finalpict_width):
        finalpicture[i,j] = np.sum(picture[i:i+kernel_height,j:j+kernel_width])


# printeld ki a bemeneti "képet", kernelt és a végeredményül kapott "képet"
print(f' picture:\n{picture}')
print(f'\n kernel:\n{kernel}')
print(f'\n final picture:\n{finalpicture}')


# Ellenőrizd le, hogy tényleg jó működik a kódod (nem kell semmit írni, csak a printelt értékeket ellenőrizd le)