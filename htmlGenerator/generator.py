import cv2, numpy as np
from htmlGenerator.elements import htmlElemets
from htmlGenerator.getTableInfo import getTableInfo
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\sonih\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'
custom_config = r'--oem 3 --psm 6'

def createPage(myElements,image, element, center, box, isEnd = False):

    corX, corY = center
    xMin, yMin, xMax, yMax = box
    width = xMax - xMin
    height = yMax - yMin

    if element == 0:
        myElements.Image(int(corX), int(corY), int(width), int(height))

    if element == 1:
        myElements.RadioButton(int(corX), int(corY))

    if element == 2:
        myElements.CheckBox(int(corX), int(corY))

    if element == 3:
        myElements.Label(int(corX), int(corY))

    if element == 4:
        myElements.Table(2,2, int(corX), int(corY))

    if element == 5:
        myElements.textArea(int(corX), int(corY), int(width), int(height))

    if element == 6:
        myElements.Link(int(corX), int(corY))

    if element == 7:
        myElements.Select(int(corX), int(corY))

    if element == 8:
        myElements.Heading(int(corX), int(corY))

    if element == 9:
        myElements.Button(int(corX), int(corY), int(width), int(height))
    
    if element == 10:
        myElements.Paragraph(int(corX), int(corY))

    if element == 11:
        myElements.Pagination(int(corX), int(corY))

    if element == 12:
        myElements.Carousel()

    if element == 13:
        myElements.TextBox(int(corX), int(corY), int(width), int(height))

    if isEnd:
        html = myElements.isEnd()
        return html
