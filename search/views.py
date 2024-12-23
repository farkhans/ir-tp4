from django.shortcuts import render
from django.http import JsonResponse
from .utils import load_bm25_model


bm25_model = load_bm25_model()

def search_query(request):
    query = request.GET.get('q')
    if not query:
        return JsonResponse({'error': 'No query provided'}, status=400)
    
    
    results = bm25_model.transform(query)
    top_results = results[results['rank'] < 10].sort_values(by=['rank'])
    response_data = top_results[['docno', 'rank']].to_dict(orient='records')
    
    return JsonResponse({'query': query, 'results': response_data})
