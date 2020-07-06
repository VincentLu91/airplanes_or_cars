from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import streamlit as st
import os
from PIL import Image

st.title('Airplanes or Automobiles')

st.header('This is a simple classifier that differentiates whether an object in the photograph uploaded is a plane or an automobile.')
st.header('Please upload an image. After that, click "Process" and it will return the classified result.')

input_buffer = st.file_uploader("Upload a file", type=("png", "jpg"))

# load and prepare the image
def load_image(filename):
	# load the image
	img = load_img(filename, target_size=(224, 224))
	# convert to array
	img = img_to_array(img)
	# reshape into a single sample with 3 channels
	img = img.reshape(1, 224, 224, 3)
	# center pixel data
	img = img.astype('float32')
	img = img - [123.68, 116.779, 103.939]
	return img

# load an image and predict the class
def run_example(image):
    # load the image
    img = Image.open(image)
    # load model
    model = load_model('model.h5')
    # predict the class
    result = model.predict(img)    
    if result[0] == [0.]:
        return 'The object identified in the photo is a plane'
    elif result[0] == [1.]:
        return 'The object identified in the photo is an automobile'
    else:
        return 'The object identified in the photo is neither a plane nor an automobile'

if st.button('Process'):
    result = run_example(input_buffer)
    st.image(input_buffer, width=None)
    st.write(result)