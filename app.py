from flask import Flask, request, send_file, render_template, redirect, url_for
from pytube import YouTube
from moviepy.editor import AudioFileClip
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_video():
    url = request.form['url']

    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    output_file = stream.download()

    # Convert to MP3
    base, ext = os.path.splitext(output_file)
    mp3_file = base + '.mp3'
    AudioFileClip(output_file).write_audiofile(mp3_file)
    os.remove(output_file)

    return send_file(mp3_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
