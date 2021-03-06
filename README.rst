Face Recognition
================

Face Recognition Based on Facenet

Built using `Facenet <https://github.com/davidsandberg/facenet>`__'s
state-of-the-art face recognition built with deep learning. The model
has an accuracy of 99.2% on the `Labeled Faces in the
Wild <http://vis-www.cs.umass.edu/lfw/>`__ benchmark.

Features
--------

-  Out of Box Working Face Recognition
-  Choose Any Pre-Trained Model from Facenet
-  For training just provide the proper folder structure
-  Faster than other available solutions

Prerequisites
~~~~~~~~~~~~~

-  You need Python(2.6 to 3.5) installed
-  X-based System supported *(does work on Windows but not tested)*

Installing
~~~~~~~~~~

.. code:: python

    pip install facenet_recognition

Setup
^^^^^

**Create setup as follows:**

1. Create input directory eg: input\_images
2. Create aligned images directory eg: aligned\_images *Create this
   directory we will store aligned images here*
3. Create pre-trained model directory eg: pretrained\_facenet\_model
   *Download Pre-Trained model from
   `Facenet`* and keep it
   in the pre\_model directory
4. Create my trained classifier directory eg: my\_classifier *In this
   directory we will save our trained model*

Let's Begin
-----------

For Facial Recognition we need to align images as follows:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    import facenet_recognition
    facenet_recognition.align_input('input_images','aligned_images')

*Above command will create our input images into aligned format and save
it in given aligned images folder*

Train & Test Classifier on Images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After we have aligned images now we can train our classifier.

.. code:: python

    pre_model='./pretrained_facenet_model/20170511-185253.pb' #locaiton of pret-trained model from Facenet
    my_class ='./my_classifier/my_classifier.pkl' #location where we want to save
    test_classifier_type = 'svm' #type of model either svm or nn
    weight= './my_classifier/model_small.yaml' #local stored weights

    facenet_recognition.test_train_classifier(aligned_images,pre_model,my_class,weight,test_classifier_type,nrof_train_images_per_class=30, seed=102)

*Mininum Required Image per person*: *1* *Number of Images for Training
per Person*: *30 (configurable)*

Train Classifer on Images(only Training)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This API is used to Train our Classifier on Aligned Images

.. code:: python

    pre_model='./pretrained_facenet_model/20170511-185253.pb' #locaiton of pret-trained model from Facenet
    my_class ='./my_classifier/my_classifier.pkl' #location where we want to save
    test_classifier_type = 'nn' #type of model either svm or nn
    weight= './my_classifier/model_small.yaml' #local stored weights

    facenet_recognition.create_classifier(aligned_images,pre_model,my_class,weight,test_classifier_type)

*Mininum Required Image per person*: *1* *Number of Images for Training
per Person*: *30 (fixed)*

Test Classifer on Images
~~~~~~~~~~~~~~~~~~~~~~~~

This API is used to test our Trained Classifer

.. code:: python

    pre_model='./pretrained_facenet_model/20170511-185253.pb' #locaiton of pret-trained model from Facenet
    my_class ='./my_classifier/my_classifier.pkl' #location where we want to save
    test_classifier_type = 'nn' #type of model either svm or nn
    weight= './my_classifier/model_small.yaml' #local stored weights

    facenet_recognition.test_classifier(aligned_images,pre_model,my_class,weight,test_classifier_type)

*Mininum Required Image per person*: *1*

Authors
-------

-  **Ishwar Sawale** -- `Visit Portfolio <http://ishwarsawale.com>`__

License
-------

This project is licensed under the MIT License - see the
`LICENSE.md <LICENSE.md>`__ file for details

Acknowledgments
---------------

-  Big Thanks to David Sandberg for Facent
-  Inspired by Dlib based library face\_recognition
