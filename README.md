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
        <li><a href="#project-directory-structure">Project Directory Structure</a></li>
        <ul>
            <li><a href="#folders-overview">Folders Overview</a></li>
        </ul>
        <li><a href="#project-setup">Project Setup</a></li>
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
- Have a look at the [project directory structure](#project-directory-structure) and the [folder overview](#folder-overview) to understand where to store/upload your contribution.
- If you're creating a task, go to the tasks folder and create a new folder with the below naming convention and add a README.md with tasks details and goals to help other contributors understand.
    - Task Folder Naming Convention : _task-n-taskname (where n is the task number)_ ex: task-1-information-gathering, task-2-exploratory-data-analysis, etc.
    - Create a README.md with a table containing information table about all contributions for the task.
- If you're contributing for a task, please make sure to store in relavant location and update the README.md information table with your contribution details.
- Make sure your file names (jupyter notebooks, python files, data sheet file names etc) has proper naming to help others in easily identifing them.
- Please restrict yourself from creating unnessesary folders other than in 'tasks' folder (as above mentioned naming convention) to avoid confusion.
- Always document your classes, functions and notebooks to help others understand their objective.


### Folder Overview

- Data - Folder to contain all the data collected, manipulated, and used in this project.
- Tasks - Folder to contain all individual tasks.
- Models - Folder to contain all trained and serialized nodels.
- Reports - Folder to contain all final reports of the project.
- References - Folder to contain all referenced code and research papers used in the project.

## Project Setup

```bash
  $ git clone https://github.com/OmdenaAI/Transformative
  $ cd Transformative

  $ pip install -r requirements.txt
```

