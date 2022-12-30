import bpy

for bone in bpy.context.selected_objects[0].find_armature().data.bones:
    print("Bone ", bone.name)
    # bone.select = True

daz3d_remapping = {
    "":""
}

import json

"""
LY Tarian=Root
abdomenLower=spine_01
abdomenUpper=spine_02
chestLower=spine_03
lCollar=clavicle_L
lShldrBend=UpperArm_L
lForearmBend=Lowerarm_L
lHand=Hand_L
rCollar=Clavicle_R
rShldrBend=Upperarm_R
rForearmBend=Lowerarm_R
rHand=Hand_R
neckLower=neck_01
lThighBend=Thigh_L
lShin=Calf_L
lFoot=Foot_L
rThighBend=Thigh_R
rShin=Calf_R
rFoot=Foot_R
lIndex1=Index_01_L
lIndex2=Index_02_L
lIndex3=Index_03_L
lMid1=middle_01_L
lMid2=middle_02_L
lMid3=middle_03_L
lPinky1=pinky_01_L
lPinky2=pinky_02_L
lPinky3=pinky_03_L
lRing1=ring_01_L
lRing2=ring_02_L
lRing3=ring_03_L
lThumb1=thumb_01_L
lThumb2=thumb_02_L
lThumb3=thumb_03_L
lForearmTwist=lowerarm_Twist_01_L
lShldrTwist=upperarm_Twist_01_L
rIndex1=Index_01_R
rIndex2=Index_02_R
rIndex3=Index_03_R
rMid1=middle_01_R
rMid2=middle_02_R
rMid3=middle_03_R
rPinky1=pinky_01_R
rPinky2=pinky_02_R
rPinky3=pinky_03_R
rRing1=ring_01_R
rRing2=ring_02_R
rRing3=ring_03_R
rThumb1=thumb_01_R
rThumb2=thumb_02_R
rThumb3=thumb_03_R
rForearmTwist=lowerarm_Twist_01_R
rShldrTwist=upperarm_Twist_01_R
lBigToe=Ball_l
lThighTwist=thigh_twist_01_L
rBigToe=Ball_r
rThighTwist=thigh_twist_01_R
"""