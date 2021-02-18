from __future__ import unicode_literals
import youtube_dl
import sys

if __name__ == '__main__':

    # Example command - yt-dl.py [video_url] [type] [final_path]

    if len(sys.argv) == 4:

        ydl_opts = {}

        # Determin the URL to download.
        video_url = sys.argv[1]

        if sys.argv[2] == 'audio':
            # We want the audio only.
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
        elif sys.argv[2] == 'video':
            ydl_opts = {}

        print(ydl_opts)
        print(video_url)

        #with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        #    ydl.download(['http://www.youtube.com/watch?v=BaW_jenozKc'])
    else:
        print('Incorrect args. ' + str(len(sys.argv)))