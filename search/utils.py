import ir_datasets as ir
import pandas as pd
import re
import pyterrier as pt
from pyterrier.measures import *
import pickle
if not pt.java.started():
    pt.java.init()

# Function to load the BM25 model
def load_bm25_model():
    with open('search/model/bm25_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model
