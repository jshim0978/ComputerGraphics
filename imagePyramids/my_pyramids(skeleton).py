import cv2
import numpy as np

def my_pyramids(src):
    '''
    :param src: image pyramids를 생성할 이미지 원본.
    :return: Gaussian pyramids 이미지 list, Laplacian pyramids 이미지 list
    '''
    # 각각 List에 4개의 이미지가 들어가도록 만들면 됩니다.
    gList = []
    lList = []

    for i in range(3):
     # 피라미드를 만들어 List에 추가하는 코드를 작성해주세요.

    return gList, lList

def my_recon(gList, lList):
    '''
    :param gList: gaussian pyramids 이미지 List
    :param lList: Laplacian pyramids 이미지 List
    :return: Laplacian pyramids로 복원된 이미지 List.
    '''
    # 복원된 이미지 List는 3개입니다.
    recon = []

    for i in range(2,-1, -1):
        #cv2.resize 함수 사용 금지.
        #gList의 이미지를 확대해, lList의 이미지를 더하세요.
        #두 피라미드를 이용해 이미지를 복원하는 코드를 작성해주세요.

    return recon

src = cv2.imread('Lena.png')

gList, lList = my_pyramids(src)
a = ['g1','g2','g3','g4']
b = ['l1', 'l2', 'l3', 'l4']

recon = my_recon(gList, lList)

for i in range(4): #확인용
    cv2.imshow(a[i], gList[i])
    cv2.imshow(b[i], lList[i])

#for i in range(3): #확인용
    #cv2.imshow(a[i], recon[i])

cv2.waitKey()
cv2.destroyAllWindows()