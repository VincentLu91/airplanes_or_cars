# Airplanes or Automobiles

Docker/Flask version of application deployed on Heroku: https://github.com/VincentLu91/airplanes-or-cars-docker-flask

## About the Project

The simple binary image classification application distinguishes between two popular types of transport: airplanes or autombiles.

It uses a VGG16 pre-trained model from the Keras library and replaces the fully connected layers of the trained VGG model with the new classifier part to interpret the output with a stochastic gradient descent optimizer. As well, the classification app runs a test harness to estimate the performance of the custom-trained  model.

The application is written in streamlit for the front-end. Accompanying libraries include Pillow for loading/processing images, and keras for defining and configuring the deep learning image classification model.

Limitation: it can only resize images of certain sizes to 224 * 224 * 3

I have written up a blog post on the IG Content Generator in great detail here: https://vincentlu91.github.io/2020/07/06/Image-Classification-Planes-or-Automobiles.html

## How to access the data app

### Deployed App

You can use the following link here: https://airplanes-or-cars.herokuapp.com

### You can also set up a Docker container to run the application

You can pull the docker image from the Docker Hub repository: https://hub.docker.com/r/vincelu299/airplanes_or_cars

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
Then in the browser, enter ```localhost:8501/```.

## How to use the data app

Upload an image (has to be size 224*224*3) or drag and drop it to the file picker:

![martymcfly](https://user-images.githubusercontent.com/3411100/86633685-f686f880-bf9e-11ea-94d3-45607d88d644.png)

Example images:
![airplane](https://user-images.githubusercontent.com/3411100/194626766-72180dec-c48f-4aa4-a607-11df01c1c8e8.jpg)
![car](https://user-images.githubusercontent.com/3411100/194626816-6684532d-c547-4749-b224-574fac0d939e.jpg)
![graphicstock-an-african-american-fat-man-holding-tray-with-fast-food-young-smiling-man-having-a-lunch-in-a-fast-food-restaurant-happy-plump-man-with-fast-food-vector-flat-design-illustration-square-layout_SXqB-sL8W_thumb](https://user-images.githubusercontent.com/3411100/194626830-7b99e260-e6f6-4493-b6c8-4e6ca53896e1.jpg)

Click "Process". The image uploaded will be displayed, along with the result that it is either a plane, automobile, or neither.

![martymcfly](https://user-images.githubusercontent.com/3411100/86633903-38b03a00-bf9f-11ea-8b40-ebc7c28b8c1f.png)
