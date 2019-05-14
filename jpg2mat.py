from keras.applications.resnet50 import ResNet50   #
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np

model = ResNet50(weights='imagenet', include_top=True)

img_path = './gkx.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

features = model.predict(x)

print('features=',features)