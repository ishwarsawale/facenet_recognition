# Face Recognition
Face Recognition Based on Facenet

Built using [Facenet](https://github.com/davidsandberg/facenet)'s state-of-the-art face recognition
built with deep learning. The model has an accuracy of 99.2% on the
[Labeled Faces in the Wild](http://vis-www.cs.umass.edu/lfw/) benchmark.

## Features
* Out of Box Working Face Recognition 
* Choose Any Pre-Trained Model from Facenet
* For training just provide the proper folder structure
* Faster than other available solutions

### Prerequisites

* You need Python(2.6 to 3.5) installed
* X-based System supported _(does work on Windows but not tested)_

### Installing

```python
pip install facenet_recognition
```


#### Setup 

__Create setup as follows:__

![input_dir](https://user-images.githubusercontent.com/15515106/38088234-b267317e-3378-11e8-9e82-e4615d7568d3.png)


1. Create input directory eg: input_images
![screen shot 2018-03-29 at 5 42 47 pm](https://user-images.githubusercontent.com/15515106/38088332-11e51f4e-3379-11e8-9db4-90e57b0f6b7f.png)

__We require at least an image per person__

2. Create aligned images directory eg: aligned_images
_Create this directory we will store aligned images here_
3. Create pre-trained model directory eg: pretrained_facenet_model
_Download Pre-Trained model from [Facenet](https://github.com/davidsandberg/facenet)_ and keep it in the pre_model directory
4. Create my trained classifier directory eg: my_classifier
_In this directory we will save our trained model_


## Let's Begin

#### For Facial Recognition we need to align images as follows:
```python
import facenet_recognition
facenet_recognition.align_input('input_images','aligned_images')
```
_Above command will create our input images into aligned format and save it in given aligned images folder_

#### Train & Test Classifier on Images

After we have aligned images now we can train our classifier.

```python
pre_model='./pretrained_facenet_model/20170511-185253.pb' #locaiton of pret-trained model from Facenet
my_class ='./my_classifier/my_classifier.pkl' #location where we want to save
test_classifier_type = 'svm' #type of model either svm or nn
weight= './my_classifier/model_small.yaml' #local stored weights

facenet_recognition.test_train_classifier(aligned_images,pre_model,my_class,weight,test_classifier_type,nrof_train_images_per_class=30, seed=102)

```
_Mininum Required Image per person_: _1_
_Number of Images for Training per Person_: _30 (configurable)_

#### Train Classifer on Images(only Training)

This API is used to Train our Classifier on Aligned Images

```python
pre_model='./pretrained_facenet_model/20170511-185253.pb' #locaiton of pret-trained model from Facenet
my_class ='./my_classifier/my_classifier.pkl' #location where we want to save
test_classifier_type = 'nn' #type of model either svm or nn
weight= './my_classifier/model_small.yaml' #local stored weights

facenet_recognition.create_classifier(aligned_images,pre_model,my_class,weight,test_classifier_type)

```
_Mininum Required Image per person_: _1_
_Number of Images for Training per Person_: _30 (fixed)_

#### Test Classifer on Images
This API is used to test our Trained Classifer
```python
pre_model='./pretrained_facenet_model/20170511-185253.pb' #locaiton of pret-trained model from Facenet
my_class ='./my_classifier/my_classifier.pkl' #location where we want to save
test_classifier_type = 'nn' #type of model either svm or nn
weight= './my_classifier/model_small.yaml' #local stored weights

facenet_recognition.test_classifier(aligned_images,pre_model,my_class,weight,test_classifier_type)

```
_Mininum Required Image per person_: _1_

## Authors

* **Ishwar Sawale** -- [Visit Portfolio ](http://ishwarsawale.com)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Big Thanks to David Sandberg for Facent
* Inspired by Dlib based library face_recognition