# Maisee Brown
# 10/29/2012
# LiftShoulder.py (Arm Movements Collection 2/6)
# This script is one of six that are intended to show the basic degrees of freedom 
# that a robotic arm I am simulating in blender will be able to perform once built.

from armInclude import *

def liftShoulder(counter):
    # Set mode to pose mode
    bpy.ops.object.mode_set(mode='POSE')
    #start frame counter at 0
  #  counter = 1
    bpy.ops.anim.change_frame(frame = counter)
    # move the hand to each angle while updating the frame numbers
    for j in range(ShoulderLiftMax, ShoulderLiftMin-ShoulderLiftStep, -ShoulderLiftStep):
        # set new rotation angles
        PoseUpperArm.rotation_euler = (math.radians(0), math.radians(0), math.radians(j))
        #insert key frame so we can mark this position in our animation
        PoseUpperArm.keyframe_insert(data_path="rotation_euler")
        # increment counter so the animation progresses in time
        counter = counter + counterIncrement
        # set frame to new counter value
        bpy.ops.anim.change_frame(frame = counter)
        # Lower arm after each lift
    for k in range(ShoulderLiftMin, ShoulderLiftMax+ShoulderLiftStep, ShoulderLiftStep):
        # set new rotation angles
        PoseUpperArm.rotation_euler = (math.radians(0), math.radians(0), math.radians(k))
        # insert key frame so we can mark this position in our animation
        PoseUpperArm.keyframe_insert(data_path="rotation_euler")
        # increment counter so the animation progresses in time
        counter = counter + counterIncrement
        bpy.ops.anim.change_frame(frame = counter)
    bpy.context.scene.frame_end = counter + 1
    # when finished set the frame to frame zero so that when we animate it starts from the beginning
    bpy.context.scene.frame_end = counter + counterIncrement
	bpy.ops.anim.change_frame(frame = 0)

def main():
    print("Starting...")
	# This is a counter used to string the 6 motions in some order later after the initial scripts are running
    startcounter = 1
    #Clear out the actions from any previous run
    bpy.context.object.animation_data.action = None
    bpy.context.scene.frame_start = 0
	# Set the arm into the rest position incase it was left by a previous script in some other position
    setRestPosition()
    #Create new action
    bpy.ops.action.new() 
	#run the swing shoulder function
    swingShoulder(startcounter)
    # play the animation we just built
    bpy.ops.screen.animation_play()

main()