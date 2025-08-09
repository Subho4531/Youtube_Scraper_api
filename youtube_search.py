from youtubesearchpython import VideosSearch

def search_youtube(topic: str, limit: int = 10):
    """Search YouTube for videos related to a given topic."""
    videos_search = VideosSearch(topic, limit=limit)
    search_results = videos_search.result().get("result", [])

    video_list = []
    for item in search_results:
        video_info = {
            "title": item.get("title", ""),
            "link": item.get("link", ""),
            "published": item.get("publishedTime", ""),
            "views": item.get("viewCount", {}).get("short", ""),
            "channel": item.get("channel", {}).get("name", ""),
            "description": ""
        }
        description_snippet = item.get("descriptionSnippet")
        if description_snippet and isinstance(description_snippet, list):
            video_info["description"] = description_snippet[0].get("text", "")
        video_list.append(video_info)
    return video_list