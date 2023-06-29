# racial_classification

## Description
This AI project is centered around creating a classification program in order to have a more efficient solution to calculating racial demographics (calculation program not included). The data used for the project includes seven sets of races: Black, East Asian, Indian, Latino/Hispanic, Middle Eastern, Southeast Asian, and White. The dataset used was provided by FairFace.

**NOTE: Due to technical errors causing me limited time on this project, it is highly recommended that you train the model on your own for higher accuracy. The current model has a minimal amount of training, so for better results it's recommended that you train on your own. 

## The Algorithm
This project was developed using Jetson Nano and is a retrained ResNet-18 model focused on detecting the race of a person in the provided image. 800 images from FairFace were used for the training. Files used were "test", "train", "val", and "labels.txt". In order to avoid organizing and selecting the images manually, I created python scripts to do it automatically and create a list of the labels (see "list_labels.py", "copy_val_data.py", "copy_train_data.py"). Then, I used these to train the model and test images.

## Running the Project
Ensure that ResNet-18 is download on the Jetson.
To train: 

In the jetson-inference folder, run ./docker/run.sh

Change directories into jetson-inference/python/training/classification

Run the training script with python3 train.py --model-dir=models/fairface_clean data/fairface_clean

After having finished needed training, change directories into jetson-
