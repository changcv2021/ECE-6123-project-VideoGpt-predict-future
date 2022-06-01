dataset ucf101 
dataset can be constructed from UCF-101 data by running the script
sh scripts/preprocess/bair/create_bair_dataset.sh datasets/bair
Use the ucfTrainTestlist file to decide how to split the dataset, use ucf_split_train_test.py to divide each category into train and test（code in preprocess）

 videoframe.py can convert the video into video frames and store in a folder and use opticalflow. py calculates optical flow based on video frames
 
 for exapmle :jaywalking.mp4
 we can use videoframe.py converting the video to 272 images(remove meaningless endings), and use opticalflow. py getting  272 optical flow images,use merge.py to Combine the 256x256x3 image and optical into a 512x256x3 image，the number is 272
