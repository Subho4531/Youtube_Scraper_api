from flask import Flask, request, jsonify
from youtube_search import search_youtube




app = Flask(__name__)

@app.route("/youtube_trend_links", methods=["GET"])
def youtube_summary_get():
    topic = request.args.get("topic")
    limit = int(request.args.get("limit", 5))

    if not topic:
        return jsonify({"error": "Please provide a topic"}), 400

    videos = search_youtube(topic, limit)
    if not videos:
        return jsonify({"error": "No videos found"}), 404

    

    video_links = []

    for video in videos:
        video_links.append(video['link'])

    return jsonify({"topic": topic,"videos": video_links})



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)