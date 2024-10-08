## Predicting house price in boston and deploying a flask app on Azure cloud

- `notebook` contains an XGBoost regressor model that was used to train the data , and the model was saved for future use at `models`.

### Makefile
- It is used to:
    - create a virtual environment,
    - install the dependencies 
    - Perform tests and linting 
    - Build docker images and run them 

### Flask app
- We create a flask instance 
- We have logger that is set to capture messages of level `INFO` and above.
- The input data converted from a json structure to a dataframe.
- It  is then  scaled using a standard scaler.
- We load the xgboost regressor and make predictions 
- Then we convert the results to a jsonfile.
- All this is running in port 5000.
- use `python app.py` to run this script

### Azure yml file
- This YAML file is a configuration for the azure pipeline that automates the process of building and deploying a python project to azure app services on a linux environment.
- sets sets up the python environment
- Install the dependencies  
- Running linting tests to ensure it follows a specific formating and style standards.
- Archives the code in a .zip file 
- Deploys the .zip package to an azure web app running on linux.
