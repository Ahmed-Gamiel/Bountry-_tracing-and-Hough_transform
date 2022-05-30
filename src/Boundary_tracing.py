from PyQt5 import QtWidgets as qtw
from PyQt5 import uic
import cv2
import numpy as np
from viewer import Viewer


class boundary_tracing(qtw.QWidget):

    def __init__(self):
        super().__init__()

        uic.loadUi("src/ui/Boundary_tracing.ui", self)
        self.original_image = Viewer()
        self.image_layout.addWidget(self.original_image)
        self.Binary_image = Viewer()
        self.Binary_image_layout.addWidget(self.Binary_image)
        self.Boundary_tracing = Viewer()
        self.Boundary_tracing_layout.addWidget(self.Boundary_tracing)
        # self.kernal_viewer = Viewer()
        # self.Image_mode = "gray"
        self.threshold_value.valueChanged.connect(self.binarizing_image)
        # self.binarization_btn.clicked.connect(self.binarizing_image)

        # self.modes_list.activated.connect(self.image_transformation)
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
  