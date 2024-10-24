import os
import subprocess

# Define your RTMPS URL and key
rtmp_url = 'rtmps://dc4-1.rtmp.t.me/s/'
stream_key = '2072225992:-ZpnvW1JIyUnHuEXVXvWqg'

# The M3U link you want to stream
m3u_link = 'https://ndtvindiaelemarchana.akamaized.net/hls/live/2003679/ndtvindia/master.m3u8'

# Use FFmpeg to pull the M3U stream and send it to Telegram via RTMPS
ffmpeg_command = [
    'ffmpeg',
    '-i', m3u_link,   # Input stream (M3U link)
    '-c:v', 'copy',   # Copy video codec without re-encoding
    '-c:a', 'aac',    # Audio codec
    '-strict', 'experimental', 
    '-f', 'flv',      # Output format for RTMP
    f'{rtmp_url}{stream_key}'   # RTMP URL + Stream Key
]

# Start the FFmpeg process
subprocess.run(ffmpeg_command)
