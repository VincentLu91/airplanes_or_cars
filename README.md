# Airplanes or Automobiles

The simple binary image classification application distinguishes between two popular types of transport: airplanes or autombiles.

It uses a VGG16 pre-trained model from the Keras library and replaces the fully connected layers of the trained VGG model with the new classifier part to interpret the output with a stochastic gradient descent optimizer. As well, the classification app runs a test harness to estimate the performance of the custom-trained  model.

The application is written in streamlit for the front-end. Accompanying libraries include Pillow for loading/processing images, and keras for defining and configuring the deep learning image classification model.

## How to access the data app

### Deployed App

You can use the following link here: https://airplanes-or-cars.herokuapp.com

### You can also set up a Docker container to run the application

After cloning the repo, cd to the repo and run:

```
docker build -t  airplanes_or_cars_stapp:v1 .
```

Then:
```
docker run -p 8501:8501 airplanes_or_cars_stapp:v1
```

You may see the suggested Network and External URLs. Ignore those - go to the browser and enter:
```http://localhost:8501/```

You should be able to view the containerized application.

### Alternatively, you can access the application in development environment

Libraries and their versions are included in requirements.txt. To install the virtual environment, run the following:

```
python3 -m venv env # or python -m venv env
source env/bin/activate
pip3 install -r requirements.txt # or pip install -r requirements.txt
```

At this point the environment should be set up with required libraries to run the application. To run the app, enter:

```
streamlit run app.py
```
Then in the browser, enter ```localhost:8501/```

## How to use the data app

Upload an image or drag and drop it to the file picker:

![martymcfly](https://user-images.githubusercontent.com/3411100/86633685-f686f880-bf9e-11ea-94d3-45607d88d644.png)

Click "Process". The image uploaded will be displayed, along with the result that it is either a plane, automobile, or neither.

![martymcfly](https://user-images.githubusercontent.com/3411100/86633903-38b03a00-bf9f-11ea-8b40-ebc7c28b8c1f.png)
