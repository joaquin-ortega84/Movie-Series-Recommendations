from django.shortcuts import render
import pandas as pd

# Create your views here.

def movies_view(request):
    # Load your DataFrame or use your existing DataFrame (movies_df)
    movies_df = pd.read_csv('/Users/joaquinortega/code/joaquin-ortega84/video-recs/project/data/csv/movies.csv')

    # Convert the DataFrame to a list of dictionaries
    movies_data = movies_df.to_dict(orient='records')
    return render(request, 'movies.html', {'movies_data': movies_data})

def series_view(request):
    # Your logic for the Series view
    # Load your DataFrame or use your existing DataFrame (movies_df)
    series_df = pd.read_csv('/Users/joaquinortega/code/joaquin-ortega84/video-recs/project/data/csv/series.csv')

    # Convert the DataFrame to a list of dictionaries
    series_data = series_df.to_dict(orient='records')
    return render(request, 'series.html', {'series_data': series_data})

def making_view(request):
    return render(request, 'making.html')
