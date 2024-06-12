from flask import Flask, request, send_file, render_template
from pytube import YouTube
from moviepy.editor import VideoFileClip
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_video():
    url = request.form['url']
    video_format = request.form['format']

    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=(video_format == 'mp3')).first()
    output_file = stream.download()

    if video_format == 'mp3':
        base, ext = os.path.splitext(output_file)
        mp3_file = base + '.mp3'
        VideoFileClip(output_file).audio.write_audiofile(mp3_file)
        os.remove(output_file)
        output_file = mp3_file

    return send_file(output_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
