
This is to help generate the summary of youtube videos.
### Features: 
1. Generates summary on a simple click within few seconds.
2. Timestamps are present with summary which directs to that part on clicking the timestamp.

The basic strategy it uses is using ML summarizing techniques on the transcript of the video.

The project is divided in two separate entities: 
1. client which is a chrome extension
2. server which process the request and sends it back to the client as a HTTP response.

The above structure is taken owing to implementation of Restful services.

### Installation:
1. Clone the repo.
2. Go in the server folder and create, activate a virtual environment and install the requirements
   with pip or pip3 install -r requirements.txt .If you can manage installing torch, else
3. Make a account on [ngrok.com](https://ngrok.com/) and use auth token from [dashboard](https://dashboard.ngrok.com/get-started/setup) for setup.

4. Everything is done, run the app now. 
5. Also change the server link in [popup.js](/client/popup.js) file in get request to API.
6. Next load the chrome extension folder [client](/client) unpacked from [chrome://extensions/](chrome://extensions/).
   Go to [youtube](https://youtube.com/) and open a video and click on summarize and see the summary.
7. connect to ngrok each time app is run a new time.

### Server:
It is a simple flask app, which has a API /api/summarize?youtube_video='url' which can be used to get the summary of a
desired youtube video by simply making a GET XML HTTP request.

### Client:
It is a chrome extension which will render the summary of the youtube video below the youtube video player by making
use of the above API. Just click on summarize button and it will show the summary of the youtube video.

## Implementation Details:
### Server
The server side is implemented using flask as a restful service.
The summarization is done by first generating the transcript of the video
for which if the video has already transcript then it is used with the help of a python
library *youtube-transcript-api* ,otherwise first the audio is taken and speech to text transformation is done.
Again useful python libraries for used for this.

After this, the summary can be generated using the transformers. As described here [Useful Blog](https://www.thepythoncode.com/article/text-summarization-using-huggingface-transformers-python), there are two ways to do this
1. Extractive summarization
2. Abstractive summarization


Here, currently sumy with LSA summarizer is used.

The summary is then given back as a HTTP response after one gives a GET HTTP request on */api/summarize?youtube_video="a valid url"*.

To server the request over HTTPS (as the youtube is a https website and generating a HTTP request to a http website will give a mixed content error), the app needs be to run on https rather than http, for this option is to deploy it on a host which will give the required https url and certificates.



### Chrome-Extension
On clicking the summarize button on the popup, if the url is of form *https://www.youtube.com/watch?v=** the popup js makes a GET request to our *Server API* .A div element is added below the youtube player with a preload text.
Then, after the text is received, it is passed to the content js which then changes the content inside the above div element. Most of the properties are inherited from parent element, so that it fits perfectly there. Extra styling are added in [content.css](/client/content.css) <br>
It can be used by loading unpacked from [chrome://extensions/](chrome://extensions/).


