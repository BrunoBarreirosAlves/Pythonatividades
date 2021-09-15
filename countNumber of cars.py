import cv

import matplotlib.pylot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
im = cv.imread('carros_imagem.jpeg')


def cvimagedetect_common_objects(im):
    pass


bbox, label, conf = cvimagedetect_common_objects(im)
output_image = draw_bbox(im, bbox, label, conf)
plt.imshow(output_image)
plt.show()
print('numero de carros nas imagens', str(label.count('carro')))