import subprocess

def convert_480p(source):
    target = source + '_480p.mp4'
    cmd = 'ffmpeg -i "{0}" -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 "{1}"'.format(source, target)
    subprocess.run(cmd)              
   