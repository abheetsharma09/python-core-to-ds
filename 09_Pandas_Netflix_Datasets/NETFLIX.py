from flask import Flask, render_template, jsonify, request
import pandas as pd

app = Flask(__name__)

CSV_PATH = "data/NETFLIXDb.csv"

def get_filtered_df(genre_filter=None):
    """
    Helper function to load the dataset and filter it by genre.
    Using a helper function keeps the code clean and reusable.
    Added engine='python' and on_bad_lines='skip' to prevent buffer overflows from malformed data.
    """
    try:
        df = pd.read_csv(
            CSV_PATH, 
            engine='python', 
            on_bad_lines='skip', 
            encoding='utf-8'
        )
    except Exception as e:
        # Fallback tracking if quotes inside descriptions are severely broken
        df = pd.read_csv(
            CSV_PATH, 
            engine='python', 
            on_bad_lines='skip', 
            quoting=3
        )
    
    # Fill empty genres with a placeholder string to avoid errors
    df['Genre'] = df['Genre'].fillna('Unknown')
    
    # If a specific genre is requested (and it's not 'All'), filter the dataframe
    if genre_filter and genre_filter.lower() != 'all':
        # .str.contains allows matching even if a show has multiple genres (e.g., "Action, Sci-Fi")
        df = df[df['Genre'].str.contains(genre_filter, case=False, na=False)]
        
    return df

@app.route('/')
def index():
    # 1. Get a unique, sorted list of all individual genres to populate the dropdown
    # Configured safely with python engine to eliminate parsing crashes
    raw_genres = pd.read_csv(
        CSV_PATH, 
        engine='python', 
        on_bad_lines='skip', 
        usecols=['Genre']
    ).dropna()
    
    unique_genres = set()
    for item in raw_genres['Genre']:
        # Split by comma in case rows have multiple values like "Drama, Thriller"
        for g in str(item).split(','):
            unique_genres.add(g.strip())
            
    sorted_genres = sorted(list(unique_genres))
    
    # 2. Load the initial first 50 rows for the first page load (defaults to 'All' genres)
    df = get_filtered_df(genre_filter='All')
    shows = df.head(50).to_dict(orient='records')
    
    # Pass both the initial shows and the list of genres to the HTML template
    return render_template('index.html', shows=shows, genres=sorted_genres)

@app.route('/get_more_shows')
def get_more_shows():
    # Grab the page number and the selected genre filter from the JavaScript request
    page = request.args.get('page', default=1, type=int)
    genre_filter = request.args.get('genre', default='All', type=str)
    per_page = 50
    
    # Get the dataset filtered down to only the requested genre
    df = get_filtered_df(genre_filter)
    
    # Calculate row ranges to slice the filtered dataset
    # e.g., Page 2 -> start index 50, end index 100
    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page
    
    # Slice the dataframe safely using .iloc
    sliced_df = df.iloc[start_idx:end_idx]
    shows = sliced_df.to_dict(orient='records')
    
    # Send the next batch back to JavaScript as JSON
    return jsonify(shows)

if __name__ == '__main__':
    app.run(debug=True)