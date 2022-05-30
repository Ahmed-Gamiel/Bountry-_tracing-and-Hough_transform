from PyQt5 import QtWidgets as qtw
from PyQt5 import uic
import cv2
from numpy.fft import fft2, fftshift
import numpy as np
from viewer import Viewer


class hough_transform(qtw.QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("src/ui/Hough_transform.ui", self)
        self.original_image = Viewer()
        self.image_layout.addWidget(self.original_image)
        self.Binary_image = Viewer()
        self.Binary_image_layout.addWidget(self.Binary_image)
        self.Hough_transform = Viewer()
        self.Hough_transform_layout.addWidget(self.Hough_transform)
        # self.binarization_btn.clicked.connect(self.binarizing_image)
        self.threshold_value.valueChanged.connect(self.binarizing_image)


    def load_original_image(self, image_path):
        self.Gray_img = cv2.imread(image_path,0)
        self.draw(self.original_image,self.Gray_img)
        self.binarizing_image()

    def draw(self,layout,image):
        layout.draw_image(image)
 
    # def setting_thershold_value(self):
    #     self.thershold_value.setText(str(self.threshold_value.value()))  

    def binarizing_image(self):
        _,self.Gray_img_binary=cv2.threshold(self.Gray_img,self.threshold_value.value(),255,cv2.THRESH_BINARY)
        self.thershold_value.setText(str(self.threshold_value.value()))  
        self.draw(self.Binary_image ,self.Gray_img_binary)

                  