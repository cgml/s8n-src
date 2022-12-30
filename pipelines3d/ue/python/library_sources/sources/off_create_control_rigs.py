import unreal

# Get the Editor world
world = unreal.EditorLevelLibrary.get_editor_world()

# Get the control rig asset
rig = unreal.load_asset("/Game/Animation/ControlRig/Mannequin_ControlRig")

# Get the rig class
rig_class = rig.get_control_rig_class()

# Using the level sequence and actor binding, we can either find or create a control rig track from the class
rig_track = unreal.ControlRigSequencerLibrary.find_or_create_control_rig_track(world,level_sequence, rig_class, actor_binding)