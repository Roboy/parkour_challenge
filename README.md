# Roboy Parkour Challenge

To use the Roboy Parkour Challenge Track Gazebo world execute the following:
```
cd parkour_challenge
ln -s $PWD/RoboyParkourTrack ~/.gazebo/models
roscore&
rosrun gazebo_ros gazebo parkour_world.sdf
```

Learn more at [www.roboy.org/win](https://roboy.org/win/).

![Gazebo Parkour Track](https://github.com/Roboy/parkour_challenge/blob/master/images/gazebo_track.png "Gazebo Parkour Track")

## Dummy demo

Link the robot model using
```
ln -s $PWD/parkour_dummy_demo/pioneer3at ~/.gazebo/models
```

Spawn the robot on the start line using `reference_frame` and `x y z` tags (assuming that `Gazebo` is already running with `parkour_world.sdf`)
```
rosrun gazebo_ros spawn_model -file `rospack find parkour_dummy_demo`/pioneer3at/model.sdf -sdf -model pioneer3at -reference_frame RoboyParkourTrack::mesh_link -x 0.3 -y -2.3 -z 0.5
```

Actuate back wheels
```
rosrun parkour_dummy_demo drive.py
```

To reset the the robot to initial position press `Ctrl+R` in Gazebo.
