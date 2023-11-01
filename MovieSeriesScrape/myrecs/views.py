from django.shortcuts import render
import pandas as pd
import os

# get cwd and base_dir for robust csv filepaths
current_directory = os.path.dirname(__file__)
base_dir = os.path.dirname(current_directory)

def movies_view(request):
    movies_df = pd.read_csv(os.path.join(base_dir,'data','csv','movies.csv'))
    movies_data = movies_df.to_dict(orient='records')
    return render(request, 'movies.html', {'movies_data': movies_data})

def series_view(request):
    series_df = pd.read_csv(os.path.join(base_dir,'data','csv','series.csv'))
    series_data = series_df.to_dict(orient='records')
    return render(request, 'index.html', {'series_data': series_data})

def making_view(request):
    return render(request, 'making.html')
