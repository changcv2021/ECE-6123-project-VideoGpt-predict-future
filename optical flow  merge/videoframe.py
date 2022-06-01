from __future__ import print_function
import sys
import numpy as np
import os
import imageio
import cv2

Height = 256
Width = 256

file_dir = "jaywalking.mp4"
with imageio.get_reader(file_dir,  'ffmpeg') as vid:
    nframes = vid.get_meta_data()['nframes']
    for i, frame in enumerate(vid):
        n_frames = i
        frame = cv2.resize(frame, (Width, Height), interpolation = cv2.INTER_CUBIC)
        imageio.imwrite("/home/zjc/下载/VideoGPT-master/output"+'/frame_%d.jpg' %i, frame)
    np.save('nframes.npy', n_frames)
