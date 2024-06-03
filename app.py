from fastapi import FastAPI
from BankNotes import BankNote
import uvicorn
import pandas as pd
import numpy as np
import pickle

app = FastAPI()
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

@app.get('/')
def index():
    return {'message': 'Hello World'}

@app.get('/{name}')
def get_name(name: str):
    return {'Hello': f'{name}'}

@app.post('/predict')
def predict_Note(data:BankNote):
    data = data.dict()
    variance=data['variance']
    skewness=data['skewness']
    curtosis=data['curtosis']
    entropy=data['entropy']
   # print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    if(prediction[0]>0.5):
        prediction="The note is FAKE"
    else:
        prediction="Bank note"
    return {
        'BankNote prediction': prediction
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload