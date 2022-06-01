#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 08:41:07 2022

@author: zjc
"""

import os
import numpy as np
import cv2
from glob import glob

# _IMAGE_SIZE = 256

def cal_for_frames(video_path,flow_path):
    frames = glob(os.path.join(video_path, '*.jpg'))
    frames.sort()
    optical= glob(os.path.join(flow_path, '*.jpg'))
    optical.sort()
    merge = []
    fra=[]
    flow=[]
    prev1 = cv2.imread(frames[0])
    prev2 = cv2.imread(optical[0])
    for i, frame_curr in enumerate(frames):
        curr = cv2.imread(frame_curr)
        fra.append(curr)
    for i, opt in enumerate(optical):
        curr = cv2.imread(opt)
     
        flow.append(curr)  
        
    merge=np.hstack((fra,flow))
    return merge


    
def save_flow(video_flows, merge_path):
    for i, merge in enumerate(video_flows):
        cv2.imwrite(os.path.join(merge_path.format('u'), "{:06d}.jpg".format(i)),
                    merge[:, :, 0])
        cv2.imwrite(os.path.join(merge_path.format('v'), "{:06d}.jpg".format(i)),
                    merge[:, :, 1])

def extract_flow(video_path,flow_path,merge_paths):
    merge = cal_for_frames(video_path,flow_paths)
    save_flow(merge, merge_paths)
    print('complete:' + flow_path)
    return


if __name__ =='__main__':

    video_paths="/home/zjc/下载/VideoGPT-master/output"
    flow_paths="/home/zjc/下载/VideoGPT-master/flow"
    merge_paths="/home/zjc/下载/VideoGPT-master/merge_result"
    video_lengths = 272
    merge = cal_for_frames(video_paths,flow_paths)
    save_flow(merge, merge_paths)
    print('complete:' + merge_paths)
    #extract_flow(video_paths, flow_paths,merge_paths)