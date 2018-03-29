from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'tensorflow==1.2',
    'scipy',
    'scikit-learn',
    'opencv-python',
    'h5py',
    'keras',
    'numpy',
    'scipy',
    'opencv-python',
    'sklearn',
    'matplotlib',
    'Pillow',
    'requests',
    'psutil'
]
setup(name='facenet_recognition',
      version='0.1.4',
      description='Face recognition based on Facenet',
      long_description=readme + '\n\n' + history,
      url='http://github.com/ishwarsawale/facenet_recognition',
      packages=[
        'facenet_recognition',
      ],
      package_dir={'facenet_recognition': 'facenet_recognition'},
      package_data={
        'facenet_recognition': ['facenet_recognition/*.npy']
      },
      author='Ishwar Sawale',
      author_email='ishwar.code@gmail.com',
      install_requires=requirements,
      license='MIT',
      include_package_data=True,
      zip_safe=False,
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
      )



