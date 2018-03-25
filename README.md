# Face Recognition
Face Recognition Based on Facenet

Built using [Facenet](https://github.com/davidsandberg/facenet)'s state-of-the-art face recognition
built with deep learning. The model has an accuracy of 99.2% on the
[Labeled Faces in the Wild](http://vis-www.cs.umass.edu/lfw/) benchmark.

## Features

#### Train Classifier on your images

Create setup as follows:

1 mkdir input_images
2 mkdir aligned_images
3 mkdir pre_model(Download Pretrained Model from Facenet)
4 mkdir my_classifier


```python
import facenet_recognition
facenet_recognition.align_input('input_images','aligned_images')
```

#### Train only Classifer on input images

```python
pre_model='./pre_model/20170511-185253.pb'
my_class ='./my_class/my_classifier.pkl' 
test_classifier_type = 'svm'
weight= './my_class/model_small.yaml'

facenet_recognition.test_train_classifier(input_dir,pre_model,my_class,weight,test_classifier_type)

```

Supported Models are: SVM, NN
