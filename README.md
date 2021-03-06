<br/>
<p align="center">
    <a href="https://www.linkedin.com/in/kazi-saiful-islam-shawon-66116b160/" class="social-icon si-rounded si-small si-linkedin">
        <i class="icon-linkedin"></i>
    </a>
    <h3 align="center">​Pose Estimation and Tracking with MMDet</h3>
    <p align="center">
        Using Multithreading with OpenCV and MMCV, MMPose, MMDet
        <br/>
    </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
    <summary>Table of Contents</summary>
    <ol>
        <li><a href="#about-the-project">About the project</a></li>
        <ul>
            <li><a href="#goals">Goals</a></li>
            <li><a href="#recommended-project-plan">Recommended Project Plan</a></li>
            <li><a href="#deliverables">Deliverables</a></li>
        </ul>
        <li><a href="#Code Explanation">Code Explanation</a></li>
    </ol>
</details>

## About the Project
For this project we have to modify the given sample code in such a way so that we can track and detect pose data from 4 different video streams at one go. So basically the idea is: we have to parallely extract frames from 4 videos and merge every 4 frames into a single frame and run that frame through mmdet + mmpose.

### Goals
- **Task 1**: Apply multithreading to read frames with opencv. The steps are:
   - From every frame of respective four videos we combine them and create a single image.
   - If a video is finished then we need to continue giving blank image until most lengthy video continues and combine the images and pass it to inference.

- **Task 2**: Apply mmdet + mmpose
    - Of every combined image we run inference and get the output image.
    - We pass the predicted image to opencv videowrite method to save it as a video.

### Recommended Project Plan

<center>
    <img src="https://i.ibb.co/gJgpmgp/project-plan.jpg" alt="project-plan" border="0">
</center>

### Deliverables
- **Deliverable 1**: A script that embrace multithreading with OpenCV and returns images.
- **Deliverable 2**: Modified script of the given example to incorporate the multithreading and mmdet + pose estmation + object tracking
- **Deliverable 3**: A alternative script that doesn't use multithreading but do the job.

## Code Explantaion

- **The Approaches are:**
    - We initialize a multithreading instance, what we will call it to extract frames of the given video path.
    - We create four threads for four videos that are given to use and pass the frames for further processing.
    - Check if the video stops giving frames, if yes and it is not the most lengthy video one then create a blank image and pass it.
    - We combine the four images to create a single image. So, there will four portions in the combined image, which is given from four threads or blank image if the video stops streaming.
    - We resize the image in 1920 X 1080 and pass it to mmdet and mmpose for detecting, pose estimating and tracking the humans.

### Multithreading (video_get.py)
- We embrace instance method to use multithreading.
    -  In VideoGet class we initialize `VideoCapture` method.
    -  With start function we initialize the thread method and pass the function we are interested to run in thread.
    -  The get function will continue extracting frames until the video provides false when extracting images.
    <center>
        <img src="https://i.ibb.co/4MFQDvj/video-get.jpg" alt="video-get" border="0">
    </center>
### Detection + Pose Estimation +  Tracking
We modify the given example to a extend to use the threading and apply mmdet + mmpose.
#### Modify 1: 
Import videos's path and save it to list. Assert if it has only four videos, raise error if it's less than 4 or more than 4.

<img src="https://i.ibb.co/VBfW7bP/glob.jpg" alt="glob">

#### 
Modify 2: Intialize the video capture and asserting if any of them fails to load.

<a href="https://ibb.co/CP8c6Y0"><img src="https://i.ibb.co/hY96c48/assert-cv2.jpg" alt="assert-cv2"></a>

#### Modify 3:
Getting minimum fps and maximum size from all the videos and intializing `VideoWriter` to write the detected images as `.mp4` format.

<a href="https://ibb.co/BnTvVBW"><img src="https://i.ibb.co/XYF6Zt0/video-write.jpg" alt="video-write" border="0"></a>

#### Modify 4: 
Initializing threadVideoGet function where it will take video path and call the `VideoGet`, initialize thread and extract frames.

<a href="https://ibb.co/X2zVJw2"><img src="https://i.ibb.co/tmb3Cdm/assert-vdocapture.jpg" alt="assert-vdocapture" border="0"></a>

#### Modify 5:
We initialize video sorting function, where it returns the most lengthy video at the first index of the list.

<a href="https://ibb.co/cxjM8fP"><img src="https://i.ibb.co/FnFNYZ9/video-sorting.jpg" alt="video-sorting" border="0"></a>

#### Modify 6:
- We use Infinite loop until the mosth lengthy video stops giving frame.
- Till then, for the shorter videos we pass blank images of the required size.
- In the loop we start the threading and extract the images and success condition.

<a href="https://ibb.co/VJqc7w4"><img src="https://i.ibb.co/CmH3kPG/while.jpg" alt="while"></a>



