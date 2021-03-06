from PIL import ImageGrab, Image
import numpy as np
import cv2
import collections

def get_aspect(m, n):
    w = m
    h = n
    while n > 0:
        tmp = n
        n = m % n
        m = tmp

    return w//m, h//m

def pil2cv(image):
    ''' PIL -> OpenCV '''
    new_img = np.array(image, dtype=np.uint8)
    if new_img.ndim == 2:  # モノクロ
        pass
    elif new_img.shape[2] == 3:  # カラー
        new_img = cv2.cvtColor(new_img, cv2.COLOR_RGB2BGR)
    elif new_img.shape[2] == 4:  # 透過
        new_img = cv2.cvtColor(new_img, cv2.COLOR_RGBA2BGRA)
    return new_img

def cv2pil(image):
    ''' OpenCV型 -> PIL型 '''
    new_image = image.copy()
    if new_image.ndim == 2:  # モノクロ
        pass
    elif new_image.shape[2] == 3:  # カラー
        new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB)
    elif new_image.shape[2] == 4:  # 透過
        new_image = cv2.cvtColor(new_image, cv2.COLOR_BGRA2RGBA)
    new_image = Image.fromarray(new_image)
    return new_image

#クリップボードから画像を取得
im = ImageGrab.grabclipboard()

#PIL -> cv2に変換
new_cv2 = pil2cv(im)

#2px大きいブランク画像を生成
height, width, channels = new_cv2.shape[:3]
blank = np.zeros((height+2, width+2))

#輪郭検出の前処理
new_gray = cv2.cvtColor(new_cv2, cv2.COLOR_BGR2GRAY)
im_blur = cv2.GaussianBlur(new_gray, (11, 11), 0)
th1 = cv2.threshold(new_gray, 5, 255, cv2.THRESH_BINARY_INV)[1]

#色を反転
im_not = cv2.bitwise_not(th1)

#反転させた画像を2px大きいブランク画像の上に貼り付け
bk_pil = cv2pil(im_not)
blank_pil = cv2pil(blank)
blank_pil.paste(bk_pil, (1,1))
fin_cv2 = pil2cv(blank_pil)

#輪郭検出
contours = cv2.findContours(fin_cv2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

# 検知したエリアを面積でフィルター
th_area = new_cv2.shape[0] * new_cv2.shape[1] / 50
contours_large = list(filter(lambda c:cv2.contourArea(c) > th_area, contours))

#頂点の高さ情報をリストに
y_ls = []

for i in range(len(contours_large[0])):
    y_ls.append(contours_large[0][i][0][1])

#頻度の高い値から黒帯の座標を検出

cnt = collections.Counter(y_ls)
cnt_common = cnt.most_common()
add_big = []
add_small = []
for i in range(len(cnt_common)):
    if cnt_common[i][0]>540:
        add_big.append(cnt_common[i][0])
    elif cnt_common[i][0]<540:
        add_small.append(cnt_common[i][0])
    

#映像スペースを計算 

ms = (round(np.mean(add_big))) - (round(np.mean(add_small)))
mo_perc = ms / height #縦の占有率(百分率)
print(mo_perc)
result = round(mo_perc, 3)*100
print('{:.1f}%'.format(result))

#アスペクト比の計算

try:
    width1, height1 = im.size
except AttributeError:
    print('クリップボードに画像がありません。')
    

width1 = round(width1, -1)
height1 = round(height1, -1)


asp = get_aspect(width1,height1)
print("アスペクト比は",asp[0],':',asp[1])

#画像の表示
imf = cv2.resize(fin_cv2,(1440,810))

cv2.imshow('image', imf)
cv2.waitKey(0)
cv2.destroyAllWindows()

        
