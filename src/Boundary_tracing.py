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
        # self.filters_list.activated.connect(self.image_transformation)
        # self.modes_list.activated.connect(self.image_transformation)