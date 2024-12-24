from django.http import JsonResponse
from django.shortcuts import render
from .utils import load_bm25_model, preprocess, get_text_by_docno

# Load the BM25 model
bm25_model = load_bm25_model()

def search_page(request):
    """Render halaman pencarian."""
    return render(request, 'search/search.html')

def search_query(request):
    """Mencari dokumen berdasarkan query."""
    query = request.GET.get('q', '')
    if not query:
        return JsonResponse({'error': 'Query parameter is missing'}, status=400)
    processed_query = preprocess(query)
    bm25_model = load_bm25_model()
    results = bm25_model.transform(processed_query)
    top_results = results[results['rank'] < 30].sort_values(by=['rank'])
    docno_list = top_results['docno'].tolist()
    text_results = get_text_by_docno(docno_list)
    return JsonResponse(text_results, safe=False)

def detail_view(request, docno):
    """Render detail dokumen berdasarkan docno."""
    docno_list = [docno]
    text_result = get_text_by_docno(docno_list) 

    if not text_result:
        return JsonResponse({'error': 'Document not found'}, status=404)

    return render(request, 'search/detail.html', {'docno': docno, 'text_raw': text_result[0]['text_raw']})

