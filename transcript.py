import urlparse
from youtube_transcript_api import YouTubeTranscriptApi
import re
from transformers import pipeline
'''
match = re.search(r"youtube\.com/.*v=([^&]*)")
if match:
    result = match.group(1)
else:
    result = ""
text = YouTubeTranscriptApi.get_transcript(result)
textFile = open('transcript.txt', 'w')
for i in range(len(text)):
    s = text[i]['text']vavfv v vvc
    textFile.writelines(s)
textFile.close()
'''

'''
def get_transcript(id):
    text = YouTubeTranscriptApi.get_transcript(id)
    s = ""
    for i in range(len(text)):
        s += " "+text[i]['text']
    return type(s)


'''

url_data = urlparse.urlparse("http://www.youtube.com/watch?v=z_AbfPXTKms&NR=1")
query = urlparse.parse_qs(url_data.query)
video = query["v"][0]
print(v)


def get_transcript(id):
    text = """
For the first time in eight years, a TV legend returned to doing what he does best.
Contestants told to "come on down!" on the April 1 edition of "The Price Is Right" encountered not host Drew Carey but another familiar face in charge of the proceedings.
Instead, there was Bob Barker, who hosted the TV game show for 35 years before stepping down in 2007.
Looking spry at 91, Barker handled the first price-guessing game of the show, the classic "Lucky Seven," before turning hosting duties over to Carey, who finished up.
Despite being away from the show for most of the past eight years, Barker didn't seem to miss a beat.
"""
    summarization = pipeline("summarization")
    summary_text = summarization(text)[0]['summary_text']
    return summary_text


'''
    s = ""
    for i in range(len(text)):
        s += " "+text[i]['text']
        '''


text = get_transcript("PN_4yMSylqk")
print(text)
