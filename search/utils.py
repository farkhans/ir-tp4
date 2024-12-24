from pathlib import Path
import pyterrier as pt
import re
import pandas as pd

if not pt.java.started():
    pt.java.init()

base_path = Path(__file__).resolve().parent  
index_path = base_path / "model" / "index" / "data.properties"
text_path = base_path / "model" / "qrels-folder" / "doc_test.csv"

def_text = pd.read_csv(text_path)

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

def get_text_by_docno(docno_list):
    df = def_text
    # Filter berdasarkan docno
    results = df[df['docno'].isin(docno_list)]
    return results[['docno', 'text_raw']].to_dict(orient='records')




