# racial_classification

## Description
This AI project is centered around creating a classification program in order to have a more efficient solution to calculating racial demographics (calculation program not included). The data used for the project includes seven sets of races: Black, East Asian, Indian, Latino/Hispanic, Middle Eastern, Southeast Asian, and White. The dataset used was provided by FairFace.

**NOTE: Due to technical errors causing me limited time on this project, it is highly recommended that you train the model on your own for higher accuracy, and train with the full FairFace dataset (in total around 80,000). The current model has a minimal amount of training, and I trained with only 800, so for better results it's recommended that you train on your own. 

![320](https://github.com/LPF116/racial_classification/assets/103634016/04a552d6-6810-4e30-b06c-9148328b0110)


## The Algorithm
This project was developed using Jetson Nano and is a retrained ResNet-18 model focused on detecting the race of a person in the provided image. 800 images from FairFace were used for the training. Files used were "test", "train", "val", and "labels.txt". In order to avoid organizing and selecting the images manually, I created python scripts to do it automatically and create a list of the labels (see "list_labels.py", "copy_val_data.py", "copy_train_data.py"). Then, I used these to train the model and test images.

## Running the Project
Ensure that ResNet-18 is download on the Jetson.
To train: 

In the jetson-inference folder, run ./docker/run.sh

Change directories into jetson-inference/python/training/classification

Run the training script with python3 train.py --model-dir=models/fairface_clean data/fairface_clean

After having finished needed training, change directories into jetson-inference/python/training/classification

To classify the image, modify the example code below by editing it to match your specific image. (Changable parts would be "black" and "326.jpg").

Example for running: imagenet.py --model=models/fairface_clean/fairface_model.onnx --input_blob=input_0 --output_blob=output_0 --labels=data/fairface_clean/labels.txt data/fairface_clean/test/black/326.jpg 326.jpg


video here:
https://youtu.be/GYsUSVvbR68
