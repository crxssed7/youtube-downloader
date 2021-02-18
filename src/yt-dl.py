from __future__ import unicode_literals
import youtube_dl
import sys

def download_url(video_url, ydl_opts):
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
    except:
        print('There was an error while downloading the video: ' + video_url)

def parse_args(video_url, type, final_path):
    if type == 'audio':
        # We want the audio only.
        if final_path:
            # We specify the file path
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': final_path + '\\/%(title)s.%(ext)s'
            }
        else:
            # We don't specify the file path
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }

        download_url(video_url = video_url, ydl_opts = ydl_opts)

    elif type == 'video':
        if final_path:
            # Specify final path
            ydl_opts = {
                'outtmpl': final_path + '\\/%(title)s.%(ext)s'
            }
        else:
            # Don't specify final path
            ydl_opts = {}

        download_url(video_url = video_url, ydl_opts = ydl_opts)

    else:
        print('You did not specify a valid type. Type can only be: audio, video')

if __name__ == '__main__':

    # Example command - yt-dl.py [video_url] [type] [final_path]

    if len(sys.argv) == 4:
        # Determine the URL to download.
        video_url = sys.argv[1]

        # Determine type
        type = sys.argv[2]

        # Determine the final_path of the download
        final_path = sys.argv[3]

        parse_args(video_url = video_url, type = type , final_path = final_path)

    elif len(sys.argv) == 3:
        # No final_path specified

        # Determine URL
        video_url = sys.argv[1]

        # Type
        type = sys.argv[2]

        # Don't need to specify final_path

        parse_args(video_url = video_url, type = type, final_path = '')

    else:
        print('Incorrect args. ' + str(len(sys.argv)))