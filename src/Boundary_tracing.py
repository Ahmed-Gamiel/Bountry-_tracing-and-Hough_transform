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
        self.threshold_value.valueChanged.connect(self.binarizing_image)

        self.boundary_btn.clicked.connect(self.boundary_tracing)

    def load_original_image(self, image_path):
        self.Gray_img = cv2.imread(image_path,0)
        self.draw(self.original_image,self.Gray_img)
        self.binarizing_image()

    def draw(self,layout,image):
        layout.draw_image(image)   

    def binarizing_image(self):
        _,self.Gray_img_binary=cv2.threshold(self.Gray_img,self.threshold_value.value(),255,cv2.THRESH_BINARY_INV) 
        self.thershold_value.setText(str(self.threshold_value.value()))  
        self.draw(self.Binary_image ,self.Gray_img_binary)
  
    def boundary_tracing(self):
        p0 , p1, dire= self.get_p1_p0(self.Gray_img_binary)
        bourder = self.get_boundry(self.Gray_img_binary, p0, p1, dire)
        bourder_img= self.make_bourder_img(bourder)
        self.draw(self.Boundary_tracing,bourder_img)

    def get_p1_p0(self,image):
        p0 = [0, 0]
        p1 = [0, 0]
        dire = 0
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                if image[i, j] == 255:
                    p0[0] = i
                    p0[1] = j
                    break
            else:
                continue
            break
        dire = (dire + 3) % 4
        curr_p = p0.copy()
        movies = [[curr_p[0], curr_p[1] + 1], [curr_p[0] - 1, curr_p[1]], [curr_p[0], curr_p[1] - 1],
                  [curr_p[0] + 1, curr_p[1]]]
        for i in range(4):
            move = movies[i]
            if (image[move[0], move[1]] == 255):
                p1 = move

        return p0, p1, dire    

    def get_boundry(self, image, p0, p1, dire):
        perv_p = []
        boundry = []
        curr_point = p1.copy()
        while (1):
            movies = [[curr_point[0], curr_point[1] + 1], [curr_point[0] - 1, curr_point[1]],
                      [curr_point[0], curr_point[1] - 1],
                      [curr_point[0] + 1, curr_point[1]]]
            dire = (dire + 3) % 4
            for i in range(4):
                move = movies[dire]
                if (image[move[0], move[1]] == 255):
                    perv_p = curr_point.copy()
                    curr_point[0], curr_point[1] = move[0], move[1]
                else:
                    dire = (dire + 1) % 4
            boundry.append(curr_point.copy())

            if (curr_point == p1 and boundry[-2] == p0):
                print("prev:", boundry[-2])
                print(boundry[-1])
                break
        return boundry   

    def make_bourder_img(self,bourder):
        new_image = np.zeros(self.Gray_img.shape)
        for i in bourder:
            new_image[i[0], i[1]] = 255
        return new_image     