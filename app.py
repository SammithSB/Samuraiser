from datetime import datetime
from flask import Flask, render_template, request, redirect, json
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
# define a variable to hold you app
app = Flask(__name__)

# define your resource endpoints


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


app.route('/time', methods=['GET'])


def get_time():
    return str(datetime.datetime.now())


@app.route('/youtube', methods=['GET', 'POST'])
def get_transcript():
    try:
        youtube_video = request.form['y_link']
        if("=" in youtube_video):
            video_id = youtube_video.split("=")[1]
        elif("youtu.be" in youtube_video):
            video_id = youtube_video.split("/")[3]

        text = YouTubeTranscriptApi.get_transcript(video_id)
        s = ""
        for i in range(len(text)):
            s += " "+text[i]['text']
        return s
    except:
        return 'hogappa'

        # server the app when this file is run
if __name__ == '__main__':
    app.run()
