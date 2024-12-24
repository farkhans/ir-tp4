from django.http import JsonResponse
from .utils import load_bm25_model, preprocess

# Load the BM25 model
bm25_model = load_bm25_model()

def search_query(request):
    query = request.GET.get('q', '')
    if not query:
        return JsonResponse({'error': 'Query parameter is missing'}, status=400)
    
    processed_query = preprocess(query)
    results = bm25_model.transform(processed_query)
    top_results = results[results['rank'] < 30].sort_values(by=['rank'])
    return JsonResponse(top_results.to_dict(orient='records'), safe=False)
