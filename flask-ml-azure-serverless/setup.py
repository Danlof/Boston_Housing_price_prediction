from setuptools import setup, find_packages

# meta data of the package 
NAME = 'Boston Housing prediction'
DESCRIPTION = 'House price prediction model'
URL ='https://github.com/Danlof/Boston-housing-prediction'
EMAIL ='mdanlof@gmail.com'
AUTHOR = 'Danlof Musyoki'
REQUIRES_PYTHON = '>=3.10.12'

setup(
    name='Boston Housing prediction',
    version='0.1',
    packages=find_packages(),
     install_requires=[
        # List of dependencies
        'pandas',
        'numpy',
        'scikit-learn',
        'seaborn',
        'scipy',
        'xgboost',
        'matplotlib',
        'joblib',
        'gunicorn',
        'fastapi',
        'pytest',
        'uvicorn',
        'prometheus-fastapi-instrumentator',
        'Flask',
        'pylint',
        'Jinja2',
        'itsdangerous',
        'matplotlib',
    ],
)