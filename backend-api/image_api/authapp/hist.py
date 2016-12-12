# coding:utf-8
import cv2

def Hist(im1, im2):
    hist1 = cv2.calcHist([im1], [0], None, [256], [0,256])
    hist2 = cv2.calcHist([im2], [0], None, [256], [0,256])
    # ヒストグラムの類似度を計算
    d = cv2.compareHist(hist1, hist2, 0)
    print d
    if d > 0.6:
        return 1
    return 0
        
