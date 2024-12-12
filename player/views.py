from youtube_search import YoutubeSearch
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest

def player_views(request):
    # Get search terms and max_results from query parameters (or set default values)
    search_terms = request.GET.get('search', '')  # Default to empty string if not provided
    max_results = request.GET.get('count', 10)  # Default to 10 if not provided

    # Validate the max_results to ensure it's a valid number
    try:
        max_results = int(max_results)
        if max_results <= 0:
            return HttpResponseBadRequest("max_results should be a positive integer.")
    except ValueError:
        return HttpResponseBadRequest("max_results must be a valid integer.")

    # Validate the search_terms to ensure it's not empty
    if not search_terms:
        return HttpResponseBadRequest("search_terms cannot be empty.")

    # Perform the YouTube search with dynamic search terms and max_results
    results = YoutubeSearch(search_terms, max_results=max_results).to_dict()
    
    video_urls= []
    for i in results:
        print(i['url_suffix'], "i['url_suffix'].")
        embed_url = i['url_suffix'].split('=')
        print(len(embed_url) == 3, len(embed_url), 2)
        if len(embed_url) == 3:
            url = f"https://www.youtube.com/embed/{embed_url[1].split('&')[0]}"
            video_urls.append(url)
    
    print(video_urls)
    # Pass the list to the template
    return render(request, 'video_list.html', {'video_urls': video_urls})
    