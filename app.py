import os
import uuid
from flask import Flask, request, jsonify, send_from_directory
from yt_dlp import YoutubeDL

app = Flask(__name__)

# Direktori penyimpanan file audio
DOWNLOAD_FOLDER = 'downloads'
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET'])
def get_audio_data():
    """
    API endpoint to download and serve YouTube audio locally.
    Takes a 'play' parameter with a YouTube URL.
    Example: /?play=https://www.youtube.com/watch?v=dQw4w9WgXcQ
    """
    youtube_url = request.args.get('play')

    if not youtube_url:
        return jsonify({"error": "The 'play' parameter is missing."}), 400

    try:
        # Buat nama file unik agar tidak tabrakan
        unique_id = str(uuid.uuid4())
        output_template = os.path.join(DOWNLOAD_FOLDER, f'{unique_id}.%(ext)s')

        # Konfigurasi yt-dlp
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output_template,
            'quiet': True,
            'no_warnings': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(youtube_url, download=True)

        # Dapatkan path file audio hasil unduhan
        filename = f"{unique_id}.mp3"
        file_path = os.path.join(DOWNLOAD_FOLDER, filename)
        file_size = os.path.getsize(file_path)
        duration_sec = info.get("duration", 0)
        duration_formatted = f"{duration_sec // 60}:{duration_sec % 60:02d}"

        return jsonify({
            "title": info.get("title"),
            "duration": duration_formatted,
            "file_size_bytes": file_size,
            "download_url": f"https://youtube-api.webkulo.com/download/{filename}"
        })

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

# Endpoint untuk mengunduh file yang sudah disimpan
@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(DOWNLOAD_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

