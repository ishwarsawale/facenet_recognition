# -*- coding: utf-8 -*-
from facenet_recognition import align_images as align
from facenet_recognition import auto_train_test as classifier
import os, os.path

def pre_check(directory):
    if not os.path.exists(directory):
        raise(directory, 'does not exist')

def align_input(input_dir=None, out_dir=None):
    pre_check(input_dir)
    pre_check(out_dir)
    align.align_data(input_dir, out_dir)

def create_classifier(input_dir=None, model_dir=None,classifier_dir=None, classifier_weight=None, model_type=None):
    pre_check(input_dir)
    if model_type.upper() == 'SVM':
        classifier.train_test(
            mode='TRAIN',classifier_filename=classifier_dir, 
            model_type=model_type.upper(),min_nrof_images_per_class=1,
            nrof_train_images_per_class=30,
            batch_size=1000,image_size=160,
            use_split_dataset=False,
            model_dir = model_dir,
            seed=102, data_dir=input_dir)
    elif model_type.upper() == 'NN' and classifier_weight:
        classifier.train_test(
            mode='TRAIN',classifier_filename=classifier_dir, 
            model_type=model_type.upper(),min_nrof_images_per_class=1,
            nrof_train_images_per_class=30,
            batch_size=1000,image_size=160,
            use_split_dataset=False,
            model_dir = model_dir,
            seed=102, data_dir=input_dir,
            classifier_weight=classifier_weight)
    else:
        print('only svm and nn classifier are supported')

def test_train_classifier(input_dir=None, model_dir=None,classifier_dir=None, classifier_weight=None, model_type=None,
    nrof_train_images_per_class=30, seed=102):
    pre_check(input_dir)
    print(seed)
    if model_type.upper() == 'SVM':
        classifier.train_test(
            mode='TRAIN',classifier_filename=classifier_dir, 
            model_type=model_type.upper(),min_nrof_images_per_class=1,
            nrof_train_images_per_class=nrof_train_images_per_class,
            batch_size=1000,image_size=160,
            use_split_dataset=True,
            model_dir = model_dir,
            seed=seed, data_dir=input_dir)
        classifier.train_test(
            mode='TEST',classifier_filename=classifier_dir, 
            model_type=model_type.upper(),min_nrof_images_per_class=1,
            nrof_train_images_per_class=nrof_train_images_per_class,
            batch_size=1000,image_size=160,
            use_split_dataset=True,
            model_dir = model_dir,
            seed=seed, data_dir=input_dir)
    elif model_type.upper() == 'NN' and classifier_weight:
        classifier.train_test(
            mode='TRAIN',classifier_filename=classifier_dir, 
            model_type=model_type.upper(),min_nrof_images_per_class=1,
            nrof_train_images_per_class=nrof_train_images_per_class,
            batch_size=1000,image_size=160,
            use_split_dataset=True,
            model_dir = model_dir,
            seed=seed, data_dir=input_dir,
            classifier_weight=classifier_weight)
        classifier.train_test(
            mode='TEST',classifier_filename=classifier_dir, 
            model_type=model_type.upper(),min_nrof_images_per_class=1,
            nrof_train_images_per_class=nrof_train_images_per_class,
            batch_size=1000,image_size=160,
            use_split_dataset=True,
            model_dir = model_dir,
            seed=seed, data_dir=input_dir,
            classifier_weight=classifier_weight)
    else:
        print('only svm and nn classifier are supported')

def test_classifier(input_dir=None, model_dir=None,classifier_dir=None, classifier_weight=None, model_type=None):
    pre_check(input_dir)
    if model_type.upper() == 'SVM':
        classifier.train_test(
            mode='TEST',classifier_filename=classifier_dir, 
            model_type=model_type.upper(),min_nrof_images_per_class=1,
            nrof_train_images_per_class=30,
            batch_size=1000,image_size=160,
            use_split_dataset=False,
            model_dir = model_dir,
            seed=102, data_dir=input_dir)
    elif model_type.upper() == 'NN' and classifier_weight:
        classifier.train_test(
            mode='TEST',classifier_filename=classifier_dir, 
            model_type=model_type.upper(),min_nrof_images_per_class=1,
            nrof_train_images_per_class=30,
            batch_size=1000,image_size=160,
            use_split_dataset=False,
            model_dir = model_dir,
            seed=102, data_dir=input_dir,
            classifier_weight=classifier_weight)
    else:
        print('only svm and nn classifier are supported')