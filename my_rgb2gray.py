import cv2
import numpy as np
import matplotlib.pyplot as plt

def rgb2gray(rgb):
    #강의 자료에 나온 인간눈에 적합한 3 곱셈수를 곱하여 더하는 행렬곱셈 식
    return np.dot(rgb[..., :3], [0.2125, 0.7154, 0.0721])



img = plt.imread('B:/iu.png')
# jpg 파일에서는 안먹히고 png파일에서만 먹히는이유가 아마도 jpg파일을 양자화할때 rgb값이 훼손되어서 일것
# 이미지의 픽셀 행렬을 읽어오는 plt.imread <> 이미지 원본을 가져오는 cv2.imread
# np.dot : 행렬 연산을위해 함수 검색
gray = rgb2gray(img)
print(gray)

cv2.imshow('gray', gray)

cv2.waitKey()
cv2.destroyAllWindows()
