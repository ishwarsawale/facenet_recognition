from setuptools import setup

setup(name='facenet_recognition',
      version='0.0.1b',
      description='Face recognition based on Facenet',
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
      license='MIT',
      include_package_data=True,
      zip_safe=False)



