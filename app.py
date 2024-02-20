
from flask import Flask, render_template, request, redirect, url_for
from googleapiclient.discovery import build

app = Flask(__name__, template_folder='templates', static_folder='static')

# Your API key obtained from the Google Developers Console
API_KEY = 'AIzaSyAl9LhzD8aQMDyV2qJTHyjtNgWGBzYMASI'  # Replace 'YOUR_API_KEY_HERE' with your actual API key

def search_youtube(query):
    # Initialize the YouTube service
    youtube = build('youtube', 'v3', developerKey=API_KEY)
# youtube_search.py
from googleapiclient.discovery import build

# Your API key obtained from the Google Developers Console
API_KEY = 'AIzaSyAl9LhzD8aQMDyV2qJTHyjtNgWGBzYMASI'  # Replace 'YOUR_API_KEY_HERE' with your actual API key

def search_youtube(query):
    # Initialize the YouTube service
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    # Search for videos and order by relevance
    request = youtube.search().list(
        q=query,
        part='snippet',
        type='video',
        maxResults=20,  # Limit to 20 videos
        order='relevance'  # Order by relevance
    )

    # Execute the search request
    response = request.execute()

    # Return a list of video items
    return response['items']

    # Search for videos and order by relevance
    request = youtube.search().list(
        q=query,
        part='snippet',
        type='video',
        maxResults=20,  # Limit to 5 videos
        order='relevance'  # Order by relevance
    )

    # Execute the search request
    response = request.execute()

    # Return a list of video items
    return response['items']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        return redirect(url_for('search_results', query=query))
    return render_template('index.html')

@app.route('/search_results/<query>')
def search_results(query):
    videos = search_youtube(query)
    return render_template('search_results.html', videos=videos)

if __name__ == '__main__':
    app.run(debug=True)
