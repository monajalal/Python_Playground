#download ffmpeg.osx from the following link
#https://github.com/imageio/imageio-binaries/raw/master/ffmpeg/ffmpeg.osx
#install Python3
# python3 -m pip install moviepy
from moviepy.editor import *
txt_clip = TextClip("My Holidays 2013",fontsize=70,color='white')
txt_clip = txt_clip.set_pos('center').set_duration(10)
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.io.VideoFileClip import VideoFileClip

generator = lambda txt: TextClip(txt, font='Georgia-Regular',
                                    fontsize=24, color='white')





