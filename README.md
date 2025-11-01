# YouTube Scraper API

A minimal Flask API that returns YouTube video links for a given topic. The API calls a helper function `search_youtube` (imported from `youtube_search`) to find trending/relevant videos and returns their URLs.

This repository contains:
- app.py — a small Flask app exposing a single POST endpoint: /youtube_trend_links

Note: app.py imports `search_youtube` from `youtube_search`. Ensure the `youtube_search` helper/module or dependency is present in the project or installed from the appropriate package.

## Features

- Minimal, easy-to-run Flask API
- Query for a topic and receive a list of YouTube video links
- Optional limit parameter to control how many links are returned (default: 5)

## Requirements

- Python 3.8+
- Flask
- The module that provides `search_youtube` (this repository expects a module called `youtube_search` that exposes `search_youtube(topic, limit)`). Install from the project's requirements if present.

Recommended:
- Use a virtual environment (venv / virtualenv / conda)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Subho4531/Youtube_Scraper_api.git
   cd Youtube_Scraper_api
   ```

2. Create and activate a virtual environment:
   - Linux / macOS:
     ```
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   - Windows (PowerShell):
     ```
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```

3. Install dependencies:
   - If a `requirements.txt` exists:
     ```
     pip install -r requirements.txt
     ```
   - If not, at minimum install Flask and the youtube search dependency you use:
     ```
     pip install flask
     # and install the package that provides youtube_search (if using a PyPI package)
     # e.g. pip install youtube-search-python
     ```
   - If `youtube_search` is a local module (a file `youtube_search.py`), no separate install is needed.

## Running the API (development)

Start the Flask app:
```
python app.py
```
By default it listens on 0.0.0.0:5000 (debug mode enabled in app.py).

## API

POST /youtube_trend_links

Query parameters:
- topic (required) — the search topic or query string to find relevant YouTube videos
- limit (optional) — integer number of videos to return (default: 5)

Notes:
- app.py reads parameters from the query string (request.args), not the JSON body.
- Example endpoint: http://localhost:5000/youtube_trend_links?topic=cats&limit=3

Responses:
- 200 OK
  ```
  {
    "topic": "cats",
    "videos": [
      "https://www.youtube.com/watch?v=abc123",
      "https://www.youtube.com/watch?v=def456",
      "https://www.youtube.com/watch?v=ghi789"
    ]
  }
  ```

- 400 Bad Request
  ```
  {
    "error": "Please provide a topic"
  }
  ```

- 404 Not Found (when no videos returned)
  ```
  {
    "error": "No videos found"
  }
  ```

Example using curl:
```
curl -X POST "http://localhost:5000/youtube_trend_links?topic=python+tutorials&limit=4"
```

Example using Python requests:
```python
import requests

resp = requests.post("http://localhost:5000/youtube_trend_links", params={"topic": "python tutorials", "limit": 3})
print(resp.status_code)
print(resp.json())
```

## Implementation Notes

- app.py expects a function named `search_youtube(topic, limit)` that returns an iterable (list) of video objects/dicts where each dictionary contains at least a 'link' key. Example:
  ```
  [
    {"title": "Video 1", "link": "https://www.youtube.com/watch?v=..."},
    {"title": "Video 2", "link": "https://www.youtube.com/watch?v=..."},
    ...
  ]
  ```
- If you are using a third-party package for searching YouTube, verify its function signature and adapt or provide a thin wrapper module named `youtube_search` that exposes `search_youtube`.

## Testing & Troubleshooting

- If you get `ImportError: No module named youtube_search`, either:
  - Install the correct third-party package that provides `youtube_search`, or
  - Add a local module `youtube_search.py` that implements `search_youtube`.
- If YouTube search calls require API keys (e.g., using the official YouTube Data API), make sure to provide credentials and update `youtube_search` accordingly.

## Suggested Improvements

- Add request validation and better error handling.
- Support reading `topic` from JSON body for POST requests.
- Add unit tests for the Flask endpoint and the search helper.
- Add rate limiting and caching for repeated queries.
- Provide Dockerfile and/or a requirements.txt for easier deployment.

## Contributing

Contributions are welcome. Please open an issue or a pull request describing your changes.

## License

Specify a license (e.g., MIT) in a LICENSE file if you want this project to be open source.
