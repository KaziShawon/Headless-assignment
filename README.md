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
        <li><a href="#Steps to start solving">How to Make a Contribution</a></li>
        <li><a href="#project-directory-structure">Project Directory Structure</a></li>
        <ul>
            <li><a href="#folders-overview">Folders Overview</a></li>
        </ul>
        <li><a href="#project-setup">Project Setup</a></li>
    </ol>
</details>

## About the Project
For this project we are going to predict cardiac arrest, which is a life-threatening medical event that affects thousands of patients around the world every year. For this problem, machine learning seems to be the best approach to alert hospitals with anticipation that a patient will have a cardiac arrest. This will improve the survival rates of patients.

### Goals
- **Task 1**: Design a classification ML algorithm capable of separating the group of patients that will experience cardiac arrest from those that do not. 

- **Task 2**: Evaluate the best-performing model once per hour for all case and control events, find an optimal threshold for alerting staff, and count the number of instances the algorithm exceeds that threshold (an 'alert') and when. Consider a prediction in the second hour as a true alert and all other alerts as false.

### Recommended Project Plan

<center>
    <img src="https://i.ibb.co/LdZGCCy/Screenshot-from-2021-09-14-10-39-46.png"></img>
</center>

### Deliverables
- **Deliverable 1**: A report detailing the analysis methodology and results.
- **Deliverable 2**: Well-thought out, thoroughly annotated and visually pleasing figures explaining the analysis methodology and results.
- **Deliverable 3**: A clearly-annotated body of code capturing the analysis. (src folder) 

## How to Make a Contribution
- Have a look at the [project directory structure](#project-directory-structure) and the [folder overview](#folder-overview) to understand where to store/upload your contribution.
- If you're creating a task, go to the tasks folder and create a new folder with the below naming convention and add a README.md with tasks details and goals to help other contributors understand.
    - Task Folder Naming Convention : _task-n-taskname (where n is the task number)_ ex: task-1-information-gathering, task-2-exploratory-data-analysis, etc.
    - Create a README.md with a table containing information table about all contributions for the task.
- If you're contributing for a task, please make sure to store in relavant location and update the README.md information table with your contribution details.
- Make sure your file names (jupyter notebooks, python files, data sheet file names etc) has proper naming to help others in easily identifing them.
- Please restrict yourself from creating unnessesary folders other than in 'tasks' folder (as above mentioned naming convention) to avoid confusion.
- Always document your classes, functions and notebooks to help others understand their objective.


## Project Directory Structure

The directory structure for this project will look like this:

```
├── README.md
├── requirements.txt        <- Requirements file for reproducing the environment.
│
├── data
│   ├── raw                 <- The original, immutable data dump.
│   ├── interim             <- Intermediate data that has been transformed for later use.
│   └── processed           <- The final, canonical data sets for modeling.
│
├── tasks                   <- All contributions organized by folders.
│   ├── task-0-template-folder
│   ├── task-1-data-gathering-and-preprocessing
│   ├── task-2-visualizations-and-machine-learning-explainability
│   ├── task-3-feature-engineering-and-model-experiments
│   ├── task-4-deliverables-and-deployment
│   ...
│
├── models                  <- Trained and serialized models, model predictions, or model summaries.
├── reports                 <- All final reports of the project.
│   └── figures             <- Figures used to generate reports.
│
└── references              <- Research papers, referenced code.
```

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

