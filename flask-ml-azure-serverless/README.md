## Predicting house price in boston and deploying a flask app on Azure cloud

- `notebook` contains an XGBoost regressor model that was used to train the data , and the model was saved for future use at `models`.

### Makefile
- It is used to:
    - create a virtual environment,
    - install the dependencies 
    -  

### Flask app
- We create a flask instance 
- We have logger that is set to capture messages of level `INFO` and above.
- The input data converted from a json structure to a dataframe.
- It  is then  scaled using a standard scaler.
- We load the xgboost regressor and make predictions 
- Then we convert the results to a jsonfile.
- All this is running in port 5000.
- use `python app.py` to run this script
