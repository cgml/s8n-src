import json


class GoldenData:
    #######################################################################
    # Story
    gamestory = {
            "players": {
                "PlayerA": {
                    "title": "The Wellness Warrior",
                    "description": """She's all about self-care and living a healthy, balanced lifestyle. 
                    Her days start with a green smoothie and yoga session, followed by a nutritious breakfast and plenty of water throughout the day. 
                    She enjoys regular workouts, either at the gym or outside in nature, and always makes time for relaxation and stress-relief. 
                    Her diet is clean and wholesome, but she also enjoys indulging in the occasional luxurious treat."""
                },
            },
            "chapters": [
                {
                    "chapter": "intro",
                    "voice-over": "In a world that is increasingly fast-paced and demanding, what does it take to be a truly successful woman?",
                    "text":"In a world that is increasingly fast-paced and demanding, what does it take to be a truly successful woman?",
                    "scenes":[
                        {
                            "scene": "gym",
                            "action": "A woman is jogging on a treadmill in a gym, her face set in determination as she sweats."
                        }
                    ]
                },
                {
                    "chapter": "persona - general characteristics - 1",
                    "voice-over": "A confident, successful woman is comfortable in her own skin and knows her worth. She doesn't compare herself to others and is content with who she is.",
                    "text": "comfortable in her own skin and knows her worth. doesn't compare herself to others and is content with who she is.",
                    "scenes":[
                        {
                            "scene": "elevator",
                            "action": [
                                    {
                                        "actor": "PlayerA",
                                        "action": "A woman presses an elevator button with one perfectly manicured hand, checking her reflection in the shiny metal doors as she waits.",
                                        "voice": None
                                    }
                            ]
                        }
                    ]
                },
                {
                    "chapter": "persona - general characteristics - 2",
                    "voice-over": "A successful woman knows what she wants and goes after it with confidence.",
                    "scenes": [
                        {
                            "actor": "PlayerA",
                            "action": "A woman walking purposefully down a city street, head held high and eyes focused ahead",
                            "voice": None
                        },
                        {
                            "actor": "PlayerA",
                            "action": "A woman confidently making her way through a crowded room, politely but firmly moving people out of her way",
                            "voice": None
                        },
                        {
                            "actor": "PlayerA",
                            "action": "A woman speaking passionately to a group of people, gesturing emphatically as she makes her point.",
                            "voice": None
                        },
                        {
                            "actor": "PlayerA",
                            "action": "A woman standing up to a bully or opponent, staring them down and refusing to back down.",
                            "voice": None
                        },
                        {
                            "actor": "PlayerA",
                            "action": "A woman crossing an finish line first, pumping her fist in the air in triumph.",
                            "voice": None
                        },
                    ]
                },
                {
                    "chapter": "general characteristics - 3",
                    "voice-over": "She takes care of herself physically and mentally, making sure to nurture her mind, body and soul.",
                    "scenes": [{
                        """                        
                        1. She wakes up in the morning and stretches her body, taking care to not overexert herself.
                        2. She eats a nutritious breakfast and then goes for a run or walk outside, enjoying the fresh air and nature.
                        3. She showers and takes care of her hygiene, making sure to also take care of her skin and hair.
                        4. She takes some time to relax and do something calming, like reading or meditating, before getting on with her day.
                        5. She goes to bed at a reasonable hour, making sure to get enough sleep so she can wake up refreshed and ready to start again tomorrow.
                        """

                    }]
                },
                {
                    "chapter": "product & character",
                    "voice-over": "She knows that a well-chosen outfit can help a woman project an image of success and competence.",
                    "scenes":[{
                        """
                        1. A woman getting dressed in a stylish outfit, looking in the mirror and feeling confident.
                        2. A woman walking down the street in her well-chosen outfit, head held high and receiving admiring glances from passers-by.
                        3. A woman at work, giving a presentation or leading a meeting, impressing her colleagues with her knowledge and command of the situation while looking fabulous in her power suit.
                        4. A woman on a date, exuding confidence and sexiness in her little black dress and high heels. 
                        5. A group of women getting ready for a night out together, laughing and complimenting each other's clothes as they put the finishing touches on their hair and makeup.
                        """

                    }]
                },
                {
                    "chapter": "brand reveal",
                    "voice-over": "Leo Riccati is a fashion brand that understands the needs of successful women. Our clothing is an expression of luxury, success and confidence – things every woman deserves to feel in her everyday life.",
                    "scenes": [{}]
                },
                {
                    "chapter": "product features - 1",
                    "text/voice-over": [
                        ("High Rise Waist with Tummy Control", "Lightweight leggings are designed to contour your curves and streamline your shape with a high-wide waist and tummy control."),
                        ("High quality materials", "Four-way stretch fabric that stretches and recovers on the cross and lengthwise grains"),
                        ("UPF 50+ protection", "Sun-Protective Clothing"),
                        ("Unique Style", "A wide range of colors and patterns to choose from")
                    ],
                    "scenes": [
                        {
                            "scene": "product",
                            "type": "product close up",
                            "vfx": {"type": "3d-text", "text": "High Rise Waist with Tummy Control"}
                        },
                        {
                            "scene": "product",
                            "type": "product close up",
                            "vfx": {"type": "3d-text", "text": "High quality materials"}
                        }
                    ]
                },
                {
                    "chapter": "call to action",
                    "voice-over": "Get the wardrobe you deserve! You work hard - now it's time to treat yourself. Act now and learn more at our website",
                    "text": "Get the wardrobe you deserve! Act now and learn more at our website: www.leoriccati.com",
                    "scenes": [
                        {
                            "scene": "product selection",
                            "type": "produce line",
                            "vfx": {}
                        }
                    ]
                },
                {
                    "chapter": "avoid failure",
                    "voice": "No one wants to feel rejected or unaccepted after neglecting their style.",
                    "scene": [
                        {
                            "scene": "old lognely woman sitting on a bench in a park ", # show bigest fear
                        }
                    ]
                },
                {
                    "chapter": "get success",
                    "voice": "The biggest secret is that confident, successful women surround themselves with positive people who support their dreams",

                },
                {
                    "chapter": "brand",
                    "voice": "Leonardo Riccati. Live in Luxury with Confidence",
                    "text": "Leonardo Riccati. Live in Luxury with Confidence",
                    "scenes": [
                        {
                            "scene": "vfx - brand reveal"
                        }
                    ]
                },
                {
                    "chapter": "joke",
                    "scenes": [
                        {
                            "scene": "old woman chaising truck with leggings"
                        }
                    ]
                }

            ],
        }





    #######################################################################
    # Gameplay

    face_animation_path = '/Game/s8n/animations/livelink/photostudio-hq/2022-09-04/Face_Archetype_Skeleton_Sequence.Face_Archetype_Skeleton_Sequence'
    body_anim1_sequence_path = '/Game/s8n/animations/mixamo-y-retargeted/Rumba_Dancing_Retargeted.Rumba_Dancing_Retargeted'
    body_anim2_sequence_path = '/Game/s8n/animations/mixamo-y-retargeted/Catwalk_Sequence_05_-_YBot_-_F40_Retargeted.Catwalk_Sequence_05_-_YBot_-_F40_Retargeted'

    MICROSECOND_IN_SEC = 1000000
    gameplay = [
        {
            "level_path": "gym/....",
            "level_type": "gym",
            "level": '/Game/s8n/scenes/experimental-01/experimental-01.experimental-01',
            "start_time": 1667692603963361,
            "gameplay_chapter": "intro",
            "players":{
                'player_a': {
                    'scene_object_name': 'PlayerA',  # If player not found in a level - it will be created with bp
                    'bp_path': '/Game/MetaHumans/elisa-001-f1-005/BP_elisa-001-f1-005.BP_elisa-001-f1-005',
                    'face_animations': [{
                        'start_frame': 0,
                        'end_frame': 300,
                        'animation_ue_path': '/Game/s8n/animations/livelink/photostudio-hq/2022-09-04/Face_Archetype_Skeleton_Sequence.Face_Archetype_Skeleton_Sequence',
                    }],
                    'body_animations': [
                        {
                            'start_position': {
                                'location': (0, 0, 0),
                                'rotation': (0, 0, 0)
                            },
                            'start_frame': 0,
                            'end_frame': 300,
                            'animation_ue_path': '/Game/s8n/animations/mixamo-y-retargeted/Treadmill_Running_-_O0_Retargeted.Treadmill_Running_-_O0_Retargeted'
                        }
                    ]
                }
            }
        },
        {
            "level_path": "elevator/....", # A woman presses an elevator button with one perfectly manicured hand, checking her reflection in the shiny metal doors as she waits.
            "level_type": "elevator",
            "level": '/Game/s8n/scenes/experimental-01/experimental-01.experimental-01',
            "start_time": 1667692613963361,
            "meta":{
                "gameplay_chapter": "persona - general characteristics - 1",
                "voice-over": "A confident, successful woman is comfortable in her own skin and knows her worth. She doesn't compare herself to others and is content with who she is.",
                "text": "comfortable in her own skin and knows her worth. doesn't compare herself to others and is content with who she is.",
            },
            "players": {
                'player_a': {
                    'scene_object_name': 'PlayerA',  # If player not found in a level - it will be created with bp
                    'bp_path': '/Game/MetaHumans/elisa-001-f1-005/BP_elisa-001-f1-005.BP_elisa-001-f1-005',
                    'face_animations': [{
                        'start_frame': 0,
                        'end_frame': 300,
                        'animation_ue_path': '/Game/s8n/animations/livelink/photostudio-hq/2022-09-04/Face_Archetype_Skeleton_Sequence.Face_Archetype_Skeleton_Sequence'
                    }],
                    'body_animations': [
                        {
                            'start_position': {
                                'location': (0, 0, 0),
                                'rotation': (0, 0, 0)
                            },
                            'start_frame': 0,
                            'end_frame': 300,
                            'animation_ue_path': '/Game/s8n/animations/mixamo-y-retargeted/Idle_Retargeted1.Idle_Retargeted1'
                        }
                    ]
                }
            }
        },
        {
            "level_path": "city/....", #  "A woman walking purposefully down a city street, head held high and eyes focused ahead
            "level_type": "city",
            "level": '/Game/s8n/scenes/experimental-01/experimental-01.experimental-01',
            "start_time": 1667692613963361,
            "meta":{
                "gameplay_chapter": "persona - general characteristics - 2",
                "voice-over": "A successful woman knows what she wants and goes after it with confidence.",
                "text": "A successful woman knows what she wants and goes after it with confidence.",
            },
            "players": {
                'player_a': {
                    # "A woman walking purposefully down a city street, head held high and eyes focused ahead
                    'scene_object_name': 'PlayerA',  # If player not found in a level - it will be created with bp
                    'bp_path': '/Game/MetaHumans/elisa-001-f1-005/BP_elisa-001-f1-005.BP_elisa-001-f1-005',
                    'face_animations': [{
                        'start_frame': 0,
                        'end_frame': 300,
                        'animation_ue_path': '/Game/s8n/animations/livelink/photostudio-hq/2022-09-04/Face_Archetype_Skeleton_Sequence.Face_Archetype_Skeleton_Sequence'
                    }],
                    'body_animations': [
                        {
                            'start_position': {
                                'location': (0, 0, 0),
                                'rotation': (0, 0, 0)
                            },
                            'start_frame': 0,
                            'end_frame': 600,
                            'animation_path':'/Game/s8n/animations/mixamo-y-retargeted/Catwalk_Sequence_05_-_YBot_-_F40_Retargeted.Catwalk_Sequence_05_-_YBot_-_F40_Retargeted'
                        }
                    ]
                }
            }
        },
        {
            "level_path": "bedroom-meditation/....", # "She takes some time to relax and do something calming, like reading or meditating, before getting on with her day.
            "level_type": "bedroom-meditation",
            "level": '/Game/s8n/scenes/experimental-01/experimental-01.experimental-01',
            "start_time": 1667692613963361,
            "meta":{
                "gameplay_chapter": "persona - general characteristics - 3",
                "voice-over": "She takes care of herself physically and mentally, making sure to nurture her mind, body and soul.",
                "text": "She takes care of herself physically and mentally, making sure to nurture her mind, body and soul.",
            },
            "players": {
                'player_a': {
                    # bedroom
                    'scene_object_name': 'PlayerA',  # If player not found in a level - it will be created with bp
                    'bp_path': '/Game/MetaHumans/elisa-001-f1-005/BP_elisa-001-f1-005.BP_elisa-001-f1-005',
                    'face_animations': [{
                        'start_frame': 0,
                        'end_frame': 300,
                        'animation_ue_path': '/Game/s8n/animations/livelink/photostudio-hq/2022-09-04/Face_Archetype_Skeleton_Sequence.Face_Archetype_Skeleton_Sequence'
                    }],
                    'body_animations': [
                        {
                            'start_position': {
                                'location': (0, 0, 0),
                                'rotation': (0, 0, 0)
                            },
                            'start_frame': 0,
                            'end_frame': 600,
                            'animation_path':'/Game/s8n/animations/mixamo-y-retargeted/Catwalk_Sequence_05_-_YBot_-_F40_Retargeted.Catwalk_Sequence_05_-_YBot_-_F40_Retargeted'
                        }
                    ]
                }
            }
        },
        {
            "level_path": "dressing-room/....",
            "level_type": "dressing-room",
            "level": '/Game/s8n/scenes/experimental-01/experimental-01.experimental-01',
            "start_time": 1667692613963361,
            "meta": {
                "gameplay_chapter": "product & character",
                "scene": "A woman getting dressed in a stylish outfit, looking in the mirror and feeling confident.",
                "voice-over": "She knows that a well-chosen outfit can help a woman project an image of success and competence.",
                "text": "She knows that a well-chosen outfit can help a woman project an image of success and competence.",
            },
            "players": {
                'player_a': {
                    'scene_object_name': 'PlayerA',  # If player not found in a level - it will be created with bp
                    'bp_path': '/Game/MetaHumans/elisa-001-f1-005/BP_elisa-001-f1-005.BP_elisa-001-f1-005',
                    'face_animations': [{
                        'start_frame': 0,
                        'end_frame': 300,
                        'animation_ue_path': '/Game/s8n/animations/livelink/photostudio-hq/2022-09-04/Face_Archetype_Skeleton_Sequence.Face_Archetype_Skeleton_Sequence'
                    }],
                    'body_animations': [
                        {
                            'start_position': {
                                'location': (0, 0, 0),
                                'rotation': (0, 0, 0)
                            },
                            'start_frame': 0,
                            'end_frame': 600,
                            'animation_path':'/Game/s8n/animations/mixamo-y-retargeted/Catwalk_Sequence_05_-_YBot_-_F40_Retargeted.Catwalk_Sequence_05_-_YBot_-_F40_Retargeted'
                        }
                    ]
                }
            }
        },
        {
            "level_path": "brand-reveal/....",
            "level_type": "brand-reveal",
            "level": '/Game/s8n/scenes/experimental-01/experimental-01.experimental-01',
            "start_time": 1667692613963361,
            "meta": {
                "gameplay_chapter": "brand reveal",
                "scene": "brand reveal",
                "voice-over": "Leo Riccati is a fashion brand that understands the needs of successful women. Our clothing is an expression of luxury, success and confidence – things every woman deserves to feel in her everyday life.",
                "text": "Leo Riccati is a fashion brand that understands the needs of successful women. Our clothing is an expression of luxury, success and confidence – things every woman deserves to feel in her everyday life.",
            },
            "players": {
                'player_a': {
                    'scene_object_name': 'PlayerA',  # If player not found in a level - it will be created with bp
                    'bp_path': '/Game/MetaHumans/elisa-001-f1-005/BP_elisa-001-f1-005.BP_elisa-001-f1-005',
                    'face_animations': [{
                        'start_frame': 0,
                        'end_frame': 300,
                        'animation_ue_path': '/Game/s8n/animations/livelink/photostudio-hq/2022-09-04/Face_Archetype_Skeleton_Sequence.Face_Archetype_Skeleton_Sequence'
                    }],
                    'body_animations': [
                        {
                            'start_position': {
                                'location': (0, 0, 0),
                                'rotation': (0, 0, 0)
                            },
                            'start_frame': 0,
                            'end_frame': 600,
                            'animation_path':'/Game/s8n/animations/mixamo-y-retargeted/POWER-GESTURE' # LIKE SUPERWOOMAN
                        }
                    ]
                }
            },
            "meshes": [
            ]
        },
        {
            "level_path": "product-close-up/....",
            "level_type": "product-close-up",
            "level": '/Game/s8n/scenes/experimental-01/experimental-01.experimental-01', # TBD
            "start_time": 1667692613963361,
            "meta": {
                "gameplay_chapter": "product features",
                "scene": "A woman getting dressed in a stylish outfit, looking in the mirror and feeling confident.",
                "text/voice-over": [
                    ("High Rise Waist with Tummy Control",
                     "Lightweight leggings are designed to contour your curves and streamline your shape with a high-wide waist and tummy control."),
                    ("High quality materials",
                     "Four-way stretch fabric that stretches and recovers on the cross and lengthwise grains"),
                    ("UPF 50+ protection", "Sun-Protective Clothing"),
                    ("Unique Style", "A wide range of colors and patterns to choose from")
                ],
            },
            "players": {
                'player_a': {
                    'scene_object_name': 'PlayerA',  # If player not found in a level - it will be created with bp
                    'bp_path': '/Game/MetaHumans/elisa-001-f1-005/BP_elisa-001-f1-005.BP_elisa-001-f1-005',
                    'face_animations': [{
                        'start_frame': 0,
                        'end_frame': 300,
                        'animation_ue_path': '/Game/s8n/animations/livelink/photostudio-hq/2022-09-04/Face_Archetype_Skeleton_Sequence.Face_Archetype_Skeleton_Sequence'
                    }],
                    'body_animations': [
                        {
                            'start_position': {
                                'location': (0, 0, 0),
                                'rotation': (0, 0, 0)
                            },
                            'start_frame': 0,
                            'end_frame': 600,
                            'animation_path': '/Game/s8n/animations/mixamo-y-retargeted/IDLE WITH HANDS UP'
                        }
                    ],
                    'body_hidden': True,
                    'face_hidden': True,
                    "product_animations":[
                        ("spine-04", "close-up-scan", 0.25),
                        ("right-hip", "", 0.25),
                        ("left-knee", "", 0.25),
                        ("left-knee", "", 0.25),
                    ]
                }
            }
        },
        {
            "level_path": "product-line/....",
            "level_type": "product-line",
            "level": '/Game/s8n/scenes/experimental-01/experimental-01.experimental-01',  # TBD
            "start_time": 1667692693963361,
            "meta": {
                "gameplay_chapter": "call to action",
                "scene": "Product selection that looks glamour, luxury, and variey of styles",
                "text/voice-over": [
                    ("Get the wardrobe you deserve! You work hard - now it's time to treat yourself. Act now and learn more at our website",
                        "Get the wardrobe you deserve! Act now and learn more at our website: www.leoriccati.com")

                ],
            },
            "players": {
                'player_a': {
                    'scene_object_name': 'PlayerA',  # If player not found in a level - it will be created with bp
                    'bp_path': '/Game/MetaHumans/elisa-001-f1-005/BP_elisa-001-f1-005.BP_elisa-001-f1-005',
                    'face_animations': [{
                        'start_frame': 0,
                        'end_frame': 300,
                        'animation_ue_path': '/Game/s8n/animations/livelink/photostudio-hq/2022-09-04/Face_Archetype_Skeleton_Sequence.Face_Archetype_Skeleton_Sequence'
                    }],
                    'body_animations': [
                        {
                            'start_position': {
                                'location': (0, 0, 0),
                                'rotation': (0, 0, 0)
                            },
                            'start_frame': 0,
                            'end_frame': 600,
                            'body_animation':''
                        }
                    ],
                    'body_hidden': True,
                    'face_hidden': True,
                    "product_animations": [
                        ("spine-04", "long-shot", 0.25),
                    ]
                }
            }
        },
        {
            "level_path": "empty-park/....",
            "level_type": "empty-park",
            "level": '/Game/s8n/scenes/experimental-01/experimental-01.experimental-01',  # TBD
            "start_time": 1667692693963361,
            "meta": {
                "gameplay_chapter": "avoid failure",
                "scene": "old woman sitting on a bench in empty park, alone",
                "text/voice-over": [
                    ("No one wants to feel rejected or unaccepted after neglecting their style.",
                    "No one wants to feel rejected or unaccepted after neglecting their style.")

                ],
            },
            "players": {
                'player_a': {
                    'scene_object_name': 'PlayerA',  # If player not found in a level - it will be created with bp
                    'bp_path': '/Game/MetaHumans/elisa-001-f1-005/BP_elisa-001-f1-005.BP_elisa-001-f1-005',
                    'face_animations': [{
                        'start_frame': 0,
                        'end_frame': 300,
                        'animation_ue_path': '/Game/s8n/animations/livelink/photostudio-hq/2022-09-04/Face_Archetype_Skeleton_Sequence.Face_Archetype_Skeleton_Sequence'
                    }],
                    'body_animations': [
                        {
                            'start_position': {
                                'location': (0, 0, 0),
                                'rotation': (0, 0, 0)
                            },
                            'start_frame': 0,
                            'end_frame': 600,
                            'body_animation': ''
                        }
                    ],
                }
            }
        },
        {
            "level_path": "party/....",
            "level_type": "party",
            "level": '/Game/s8n/scenes/experimental-01/experimental-01.experimental-01',  # TBD
            "start_time": 1667692693963361,
            "meta": {
                "gameplay_chapter": "get success",
                "scene": "old woman sitting on a bench in empty park, alone",
                "text/voice-over": [
                    ("The biggest secret is that confident, successful women surround themselves with positive people who support their dreams.",
                     "The biggest secret is that confident, successful women surround themselves with positive people who support their dreams.")

                ],
            },
            "players": {
                'player_a': {
                    'scene_object_name': 'PlayerA',  # If player not found in a level - it will be created with bp
                    'bp_path': '/Game/MetaHumans/elisa-001-f1-005/BP_elisa-001-f1-005.BP_elisa-001-f1-005',
                    'face_animations': [{
                        'start_frame': 0,
                        'end_frame': 300,
                        'animation_ue_path': '/Game/s8n/animations/livelink/photostudio-hq/2022-09-04/Face_Archetype_Skeleton_Sequence.Face_Archetype_Skeleton_Sequence' # SMILE
                    }],
                    'body_animations': [
                        {
                            'start_position': {
                                'location': (0, 0, 0),
                                'rotation': (0, 0, 0)
                            },
                            'start_frame': 0,
                            'end_frame': 600,
                            'body_animation': 'DANCE'
                        }
                    ],
                }
            }
        },
        {
            "chapter": "brand",
            "voice": "Leonardo Riccati. Live in Luxury with Confidence",
            "text": "Leonardo Riccati. Live in Luxury with Confidence",
            "scenes": [
                {
                    "scene": "vfx - brand reveal"
                }
            ]
        },
        {
            "chapter": "joke",
            "scenes": [
                {
                    "scene": "old woman chaising truck with leggings"
                }
            ]
        }

    ]

    #######################################################################
    # Storybooard
    storyboard = [
        {
            "scene": "scene_0000",
            "total_scene_range": (0, 300),
            "fps": 30,
            "level_path": "/Game/s8n/scenes/experimental-01/experimental-01.experimental-01",
            "level_configuration": {
                "property1": "value1"
            },
            "players": [
                {
                    "name": "PlayerA",
                    "ue_path": "/Game/MetaHumans/elisa-001-f1-005/BP_elisa-001-f1-005-HQ.BP_elisa-001-f1-005-HQ",
                    "face_animations": [{
                        "ue_path": face_animation_path,
                        "start_frame": 0,
                        "end_frame": 300,
                        "offset": 0
                    }],
                    "body_animations": [{
                        "ue_path": body_anim1_sequence_path,
                        "start_frame": 0,
                        "end_frame": 100,
                        "offset": 0
                    },
                        {
                            "ue_path": body_anim1_sequence_path,
                            "start_frame": 100,
                            "end_frame": 300,
                            "offset": 0
                        }]
                }
            ],
            "meshes": []
        }
    ]


    #######################################################################
    # Sequence Instructions


    scenes = [
        {
            "scene": "scene_0000",
            "total_scene_range": (0, 300),
            "fps": 30,
            "level_path": "/Game/s8n/scenes/experimental-01/experimental-01.experimental-01",
            "level_configuration": {
                "property1": "value1"
            },
            "players": [
                {
                    "name": "PlayerA",
                    "ue_path": "/Game/MetaHumans/elisa-001-f1-005/BP_elisa-001-f1-005-HQ.BP_elisa-001-f1-005-HQ",
                    "face_animations": [{
                        "ue_path": face_animation_path,
                        "start_frame": 0,
                        "end_frame": 300,
                        "offset": 0
                    }],
                    "body_animations": [{
                        "ue_path": body_anim1_sequence_path,
                        "start_frame": 0,
                        "end_frame": 100,
                        "offset": 0
                    },
                        {
                            "ue_path": body_anim1_sequence_path,
                            "start_frame": 100,
                            "end_frame": 300,
                            "offset": 0
                        }]
                }
            ],
            "meshes": [],
            "camera_shots": [
                {
                    "start_frame": 0,
                    "end_frame": 150,
                    "transformations":{
                        "0": (-100, 0, 50, 0, 0, 0),
                        "150": (-300, 0, 50, 0, 0, 0)
                    },
                    "properties": {
                        "CurrentFocalLength": {
                            "0": 5,
                            "150": 20
                        }
                    }
                },
                {
                    "start_frame": 150,
                    "end_frame": 300,
                    "transformations":{
                        "150": (-300, 0, 50, 0, 0, 0),
                        "300": (-100, 0, 50, 0, 0, 0)
                    },
                    "properties": {
                        "CurrentFocalLength": {
                            "151": 20,
                            "300": 5
                        }
                    }
                }
            ],
            "render_cuts":[
                {"render_cut_id": "rc-01", "start_frame": 0, "end_frame": 60},
                {"render_cut_id": "rc-02", "start_frame": 80, "end_frame": 140},
                {"render_cut_id": "rc-03", "start_frame": 160, "end_frame": 220},
                {"render_cut_id": "rc-04", "start_frame": 240, "end_frame": 300},
            ]
        }
    ]

    sequence_instructions = {
        "scenes": scenes,
        "tracks": {
            "video": [
                {"scene": "scene_0000", "render_cut_id": "rc-01", "start_frame": 0, "end_frame": 60, "direction": "forward"},
                {"scene": "scene_0000", "render_cut_id": "rc-02", "start_frame": 80, "end_frame": 140, "direction": "forward"},
                {"scene": "scene_0000", "render_cut_id": "rc-02",  "start_frame": 100, "end_frame": 140, "direction": "backward"},
                {"scene": "scene_0000", "render_cut_id": "rc-03",  "start_frame": 160, "end_frame": 220, "direction": "forward"},
                {"scene": "scene_0000", "render_cut_id": "rc-04",  "start_frame": 240, "end_frame": 300, "direction": "forward"},
            ],
            "audio": {
                "music": {
                    "file_path": "C:/s8n/linux-cp/data/output/audio/mp3/fr60cut_alexberoza_artnow.mp3",
                    "start_frame": 0,
                    "end_frame": 260
                }
            }
        }
    }



