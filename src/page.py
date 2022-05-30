from calendar import c
from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw
from PyQt5 import uic

from Hough_transform import hough_transform
from Boundary_tracing import boundary_tracing

class Page (qtw.QTabWidget):
    def __init__ (self):
        super().__init__()

        uic.loadUi("src/ui/page.ui", self)

        
        self.hough_transform = hough_transform()
        self.boundary_tracing = boundary_tracing()


        self.Hough_transform_layout.addWidget(self.hough_transform)
        self.Boundray_tracing_layout.addWidget(self.boundary_tracing)

    # def load_image(self, image_path):
    #     self.filter_studio.load_original_image(image_path)
    #     self.equalizer.load_original_image(image_path)
        

        