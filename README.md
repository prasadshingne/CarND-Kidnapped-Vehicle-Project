# Kidnapped Vehicle Project

[Udacity Starter Code](https://github.com/udacity/CarND-Kidnapped-Vehicle-Project)

The robot has been kidnapped and transported to a new location! Luckily it has a map of this location, a (noisy) GPS estimate of its initial location, and lots of (noisy) sensor and control data.

In this project we implement a two dimensional particle filter in C++ to localize a kidnapped vehicle. The particle filter is given a map and some initial localization information (analogous to what a GPS does). At each time step the filter gets noisy observation and control data.

## Prerequisites


* cmake >= 3.5
* make >= 4.1 (Linux, Mac), 3.81 (Windows)
* gcc/g++ >= 5.4
* [Udacity Term 2 Simulator](https://github.com/udacity/self-driving-car-sim/releases)



## Running the Code
This project involves the Term 2 Simulator which can be downloaded [here](https://github.com/udacity/self-driving-car-sim/releases)

This repository includes two files that can be used to set up and install uWebSocketIO for either Linux or Mac systems. For windows you can use either Docker, VMware, or even Windows 10 Bash on Ubuntu to install uWebSocketIO.

Once the install for uWebSocketIO is complete, the main program can be built and ran by doing the following from the project top directory.

1. mkdir build
2. cd build
3. cmake ..
4. make
5. ./particle_filter

Alternatively some scripts have been included to streamline this process, these can be leveraged by executing the following in the top directory of the project:

1. ./clean.sh
2. ./build.sh
3. ./run.sh

Tips for setting up your environment can be found [here](https://classroom.udacity.com/nanodegrees/nd013/parts/40f38239-66b6-46ec-ae68-03afd8a601c8/modules/0949fca6-b379-42af-a919-ee50aa304e6a/lessons/f758c44c-5e40-4e01-93b5-1a82aa4e044f/concepts/23d376c7-0195-4276-bdf0-e02f1f3c665d)

## My Simulator and Environment Set-up (Ubuntu 20.04.1 LTS)

### Simulator Setup

The instructions are from [here](https://medium.com/@kaigo/how-to-install-udacitys-self-driving-car-simulator-on-ubuntu-20-04-14331806d6dd).

1. Download the (.deb) package of Unity (3D) version 5.5.1f1 that the Udacity Simulator uses. 
2. Install dependencies : `sudo apt install gconf-service lib32gcc1 lib32stdc++6 libc6-i386 libgconf-2-4 npm`
3. Run the install : `sudo dpkg -i ~/Downloads/unity-editor_amd64-5.5.1xf1Linux.deb`
4. If you get error about unmet dependencies you may need to run, and retry ` sudo apt --fix-broken install` 
5. With Unity working now, download and run the latest release of the Udacity Term 2 [Simulator](https://github.com/udacity/self-driving-car-sim/releases). 

### Environment Setup

I used VSCode IDE for this project. Follow the thorough instructions provided by [yosoufe](https://gist.github.com/yosoufe/dd37284b7319c484dd77e42947fc82b7) to setup the environment. The instructions cover debugging as well which may be useful.

# Overview of main.cpp

The particle filter is implemented in particle_filter.cpp and particle_filter.h. 

The program main.cpp has already been filled out, but feel free to modify it.

Below is how main.cpp uses for uWebSocketIO in communicating with the simulator.

INPUT: values provided by the simulator to the c++ program

// sense noisy position data from the simulator

["sense_x"]

["sense_y"]

["sense_theta"]

// get the previous velocity and yaw rate to predict the particle's transitioned state

["previous_velocity"]

["previous_yawrate"]

// receive noisy observation data from the simulator, in a respective list of x/y values

["sense_observations_x"]

["sense_observations_y"]


OUTPUT: values provided by the c++ program to the simulator

// best particle values used for calculating the error evaluation

["best_particle_x"]

["best_particle_y"]

["best_particle_theta"]

//Optional message data used for debugging particle's sensing and associations

// for respective (x,y) sensed positions ID label

["best_particle_associations"]

// for respective (x,y) sensed positions

["best_particle_sense_x"] <= list of sensed x positions

["best_particle_sense_y"] <= list of sensed y positions

I don't touch main.cpp

# Implementing the Particle Filter

The particle filter is implemented in [src/particle_filter.cpp](https://github.com/prasadshingne/CarND-Kidnapped-Vehicle-Project/blob/master/src/particle_filter.cpp) -

* **Initializtion** in [ParticleFilter::init](https://github.com/prasadshingne/CarND-Kidnapped-Vehicle-Project/blob/1c8effc04d2ab72c25f1b84bf3f41bacb677df5a/src/particle_filter.cpp#L28) from line 28 to 63.
* **Prediction** in [ParticleFilter::prediction](https://github.com/prasadshingne/CarND-Kidnapped-Vehicle-Project/blob/1c8effc04d2ab72c25f1b84bf3f41bacb677df5a/src/particle_filter.cpp#L65) from line 65 to 99.
* **Data Association** in [ParticleFilter::dataAssociation](https://github.com/prasadshingne/CarND-Kidnapped-Vehicle-Project/blob/1c8effc04d2ab72c25f1b84bf3f41bacb677df5a/src/particle_filter.cpp#L101) from line 101 to 144.
* **Update Weights** in [ParticleFilter::updateWeights](https://github.com/prasadshingne/CarND-Kidnapped-Vehicle-Project/blob/1c8effc04d2ab72c25f1b84bf3f41bacb677df5a/src/particle_filter.cpp#L146) from line 146 to 232.
* **Resample** in [ParticleFilter::resample](https://github.com/prasadshingne/CarND-Kidnapped-Vehicle-Project/blob/1c8effc04d2ab72c25f1b84bf3f41bacb677df5a/src/particle_filter.cpp#L234) from line 234 to 274.

The rest of the code is untouched.

# Results

I ran the particle filter with 100 particles and it passed. Below screenshot shows the last frame from the simulator output.

| Parameter    |      x       |       y      |     yaw      |
|:------------:|:------------:|:------------:|:------------:|
|    Error     |    0.109     |     0.092    |     0.004    |


<img src="https://github.com/prasadshingne/CarND-Kidnapped-Vehicle-Project/blob/master/output_files/pf100_lastframe.jpg" width="480" height="270"/>

The simulation output video is [here](https://github.com/prasadshingne/CarND-Kidnapped-Vehicle-Project/blob/master/output_files/pf100-2021-01-31_07.11.12.mp4)

## Note: Effect of number of particles on estimation

In addition to running the filter with 100 particles I also ran it with 1 particle [simultor output](https://github.com/prasadshingne/CarND-Kidnapped-Vehicle-Project/blob/master/output_files/pf1-2021-01-31_07.23.47.mp4) and 3 particles [simultor output](https://github.com/prasadshingne/CarND-Kidnapped-Vehicle-Project/blob/master/output_files/pf3-2021-01-31_07.08.59.mp4).   

Of course the result was poor with 1 particle:

| Parameter    |      x       |       y      |     yaw      |
|:------------:|:------------:|:------------:|:------------:|
|    Error     |    8.525     |     8.097    |     0.083    |

Surprisingly to me the result is already much better with 3 particles:

| Parameter    |      x       |       y      |     yaw      |
|:------------:|:------------:|:------------:|:------------:|
|    Error     |    0.262     |     0.262    |     0.010    |

Screenshot of the last frame for both the simulations is shown below.

| 1 particle   | 3 particles  |
|:------------:|:------------:|
|<img src="https://github.com/prasadshingne/CarND-Kidnapped-Vehicle-Project/blob/master/output_files/pf1_lastframe.jpg" width="480" height="270"/> | <img src="https://github.com/prasadshingne/CarND-Kidnapped-Vehicle-Project/blob/master/output_files/pf3_lastframe.jpg" width="480" height="270"/> |

The below figures compare the position estimate, R (distance from origin) and Yaw for the three cases.

|   Position Estimate    |   R (distance from origin)   |           Yaw          |
|:----------------------:|:----------------------------:|:----------------------:|
|    <img src="https://github.com/prasadshingne/CarND-Kidnapped-Vehicle-Project/blob/master/output_files/Compare_predictions_position.jpg" width="320" height="180"/>     |   <img src="https://github.com/prasadshingne/CarND-Kidnapped-Vehicle-Project/blob/master/output_files/Compare_r.jpg" width="320" height="180"/>    |     <img src="https://github.com/prasadshingne/CarND-Kidnapped-Vehicle-Project/blob/master/output_files/Compare_yaw.jpg" width="320" height="180"/>   |




