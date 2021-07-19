import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
dir = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

from os import listdir
from detectron2.config import get_cfg
from detectron2.engine import DefaultPredictor
from detectron2.utils.visualizer import ColorMode
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog
from htmlGenerator.generator import *
import cv2

cfg = get_cfg()
cfg.merge_from_file('model/config.yml')
cfg.MODEL.WEIGHTS = 'model/model_final.pth'
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.6   # set the testing threshold for this model
cfg.MODEL.ROI_HEADS.NUM_CLASSES = 14
predictor = DefaultPredictor(cfg)

sample_metadata = MetadataCatalog.get("experiment")
sample_metadata.thing_classes = ['Image', 'RadioButton', 'CheckBox', 'Label', 
    'Table', 'Textarea', 'Link', 'Select', 'Heading', 'Button', 'Paragraph', 
    'Pagination', 'Carousel','Textbox']


def detectObject(image):

    # img = cv2.resize(image, (800, 800))
    outputs = predictor(image)
    v = Visualizer(image[:, :, ::-1],
        metadata=sample_metadata, 
        scale=0.8, 
        instance_mode=ColorMode.IMAGE_BW   # remove the colors of unsegmented pixels
    )
    instances = outputs['instances'].to('cpu')

    v = v.draw_instance_predictions(instances)
    im = cv2.resize(v.get_image()[:, :, ::-1], (900,600))
    return im, outputs


def genareteHTML(image, output):

    instances = output['instances'].to('cpu')
    classes = instances.pred_classes.tolist()
    pred_boxes = instances.pred_boxes

    boxes = []
    for cor in pred_boxes:
        boxes.append(cor.numpy())
    
    myPage = ''
    myElements = htmlElemets()

    for i in range(len(classes)):
        if i == len(classes)-1: 
            myPage = createPage(myElements,image, classes[i], pred_boxes[i].get_centers().numpy()[0], boxes[i], True)
        else:
            createPage(myElements,image, classes[i], pred_boxes[i].get_centers().numpy()[0], boxes[i])

    name = 'myPage.html'
    if os.path.exists(dir + "\\" + name):
        os.remove(dir + "\\" + name)
    
    with open(dir + "\\" + name, 'w') as file:
            file.writelines(myPage)
            file.close()

            return True

