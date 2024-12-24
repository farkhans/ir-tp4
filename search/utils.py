from pathlib import Path
import pyterrier as pt
import re

if not pt.java.started():
    pt.java.init()

base_path = Path(__file__).resolve().parent  
index_path = base_path / "model" / "index" / "data.properties"


def load_bm25_model():
    #The best bm25.b get from hyper tuning
    bm25 = pt.BatchRetrieve(str(index_path), wmodel='BM25', controls={"bm25.b": 1})

    return bm25

def preprocess(text):
    text = text.lower()
    pattern = re.compile('[\W_]+')
    text = pattern.sub(' ', text)
    text.strip()
    return text



