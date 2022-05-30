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