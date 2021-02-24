from PIL import ImageGrab, Image
import numpy as np
import cv2
import collections
import statistics


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

class Finder:
    def __init__(self):
        pass

    #AspFinder
    def AspFinder(self):
        #クリップボードから画像を取得
        im = ImageGrab.grabclipboard()
        try:
            width, height = im.size
        except AttributeError:            
            result = 'クリップボードに画像がありません'
            return result

        width = round(width, -1)
        height = round(height, -1)


        asp = get_aspect(width,height)
        result = "アスペクト比 "+str(asp[0])+':'+str(asp[1])
        return result

    #BBFinder
    def BBFinder(self):
        #クリップボードから画像を取得
        im = ImageGrab.grabclipboard()

        #PIL -> cv2に変換
        new_cv2 = pil2cv(im)

        #2px大きいブランク画像を生成
        height, width, channels = new_cv2.shape[:3]
        blank = np.zeros((height+2, width+2))

        #輪郭検出の前処理
        show = cv2.resize(new_cv2,(1280, 720))
        #cv2.imshow('ima',show)
        new_gray = cv2.cvtColor(new_cv2, cv2.COLOR_BGR2GRAY)
        #new_gray = cv2.GaussianBlur(new_gray, (11, 11), 0)
        th1 = cv2.threshold(new_gray, 2, 255, cv2.THRESH_BINARY_INV)[1]

        #色を反転
        im_not = cv2.bitwise_not(th1)

        #反転させた画像を2px大きいブランク画像の上に貼り付け
        bk_pil = cv2pil(im_not)
        blank_pil = cv2pil(blank)
        blank_pil.paste(bk_pil, (1,1))
        fin_cv2 = pil2cv(blank_pil)

         

        #輪郭検出
        contours = cv2.findContours(fin_cv2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]

        # 検知したエリアを面積でフィルター
        th_area = new_cv2.shape[0] * new_cv2.shape[1] / 25
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
        lim = height / 2 #1080時、540
        for i in range(len(cnt_common)):
            if cnt_common[i][0]>lim:
                add_big.append(cnt_common[i][0])
            elif cnt_common[i][0]<lim:
                add_small.append(cnt_common[i][0])

        #リスト内をフィルター
         

        
        cv2.imwrite('tmp.png',fin_cv2)
        fin_cv2 = cv2.resize(fin_cv2,(1280, 720))
        #cv2.imshow('image',fin_cv2)
        
        t_big = statistics.mode(add_big)
        t_small = statistics.mode(add_small)
        """print(add_big)
        print(add_small)
        print(statistics.mode(add_big))
        print(statistics.mode(add_small))"""

        #映像スペースを計算 

        ms = (round(np.mean(t_big))) - (round(np.mean(t_small)))
        mo_perc = ms / (height+2) #縦の占有率(百分率)
        
        result = '占有率: ' + str(round(mo_perc*100, 1)) + '%'
        
        return result    





        
