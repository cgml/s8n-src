import golden_data


class SequenceInstructionsBuilder:
    def create_instructions(self, storyboard):
        return self.create_instructions_mini(storyboard)

    def create_instructions_mini(self, storyboard):
        scenes = [
            {
                "scene": "scene_0000",
                "total_scene_range": (20, 94),
                "fps": 30,
                "level_path": "/Game/__STAGE-0__/photostudio-portrait-20230122/level-photostudio-portrait-20230122-0612.level-photostudio-portrait-20230122-0612",
                "sequences": [
                    {
                        # "sequence_path": "/Game/__STAGE-0__/photostudio-portrait-20230122/sequences/look-1105/sequence-photostudio-portrait-20230122-1259_XLS",
                        #"sequence_path": "/Game/__STAGE-0__/photostudio-portrait-20230122/sequences/look-1105/sequence-photostudio-portrait-20230122-1259_XLS.sequence-photostudio-portrait-20230122-1259_XLS",
                        "sequence_path": "/Game/__STAGE-0__/photostudio-portrait-20230122/sequences/look-1105/sequence-photostudio-portrait-20230122-1259_XLS.sequence-photostudio-portrait-20230122-1259_XLS",
                        "render_cuts": [
                            {"render_cut_id": "rc-01", "start_frame": 0, "end_frame": 31}
                            ,{"render_cut_id": "rc-02", "start_frame": 61, "end_frame": 71}
                        ]
                    }
                ],
            }
        ]

        sequence_instructions = {
            "preset": "/Game/__STAGE-0__/photostudio-portrait-20230122/presets/preset-photostudio-portrait-20230122-2145-HDAA1x1",
            "scenes": scenes,
            "tracks": {
                "video": [
                    {"scene": "scene_0000", "render_cut_id": "rc-01", "start_frame": 1, "end_frame": 20, "expected_frames": 40, "direction": "forward"},
                    {"scene": "scene_0000", "render_cut_id": "rc-01", "start_frame": 1, "end_frame": 20, "expected_frames": 30, "direction": "backward"},
                    {"scene": "scene_0000", "render_cut_id": "rc-02", "start_frame": 61, "end_frame": 70, "expected_frames": 40, "direction": "forward"}
                ],
                "audio": {
                    "music": {
                        "file_path": "C:/s8n/system-linux/data/output/audio/mp3/fr60cut_alexberoza_artnow.mp3",
                        "start_frame": 0,
                        "end_frame": 240
                    }
                }
            }
        }
        return sequence_instructions


    def create_instructions_large(self, storyboard):
        scenes = [
            {
                "scene": "scene_0000",
                "total_scene_range": (20, 94),
                "fps": 30,
                "level_path":"/Game/__STAGE-0__/photostudio-portrait-20230122/level-photostudio-portrait-20230122-0612.level-photostudio-portrait-20230122-0612",
                "sequences": [
                    {
                        "sequence_path": "/Game/__STAGE-0__/photostudio-portrait-20230122/sequences/look-1105/sequence-photostudio-portrait-20230122-1259_XLS",
                        "render_cuts": [
                            {"render_cut_id": "rc-01", "start_frame": 20, "end_frame": 41},
                            {"render_cut_id": "rc-02", "start_frame": 50, "end_frame": 71},
                        ]
                    },
                    {
                        "sequence_path": "/Game/__STAGE-0__/photostudio-portrait-20230122/sequences/look-1105/sequence-photostudio-portrait-20230122-1259_FS",
                        "render_cuts": [
                            {"render_cut_id": "rc-03", "start_frame": 20, "end_frame": 41},
                            {"render_cut_id": "rc-04", "start_frame": 50, "end_frame": 71},
                        ]
                    },
                    {
                        "sequence_path": "/Game/__STAGE-0__/photostudio-portrait-20230122/sequences/look-1105/sequence-photostudio-portrait-20230122-1259_MS",
                        "render_cuts": [
                            {"render_cut_id": "rc-05", "start_frame": 20, "end_frame": 41},
                            {"render_cut_id": "rc-06", "start_frame": 50, "end_frame": 71},
                        ]
                    },
                    {
                        "sequence_path": "/Game/__STAGE-0__/photostudio-portrait-20230122/sequences/look-1105/sequence-photostudio-portrait-20230122-1259_CU",
                        "render_cuts": [
                            {"render_cut_id": "rc-07", "start_frame": 20, "end_frame": 41},
                            {"render_cut_id": "rc-08", "start_frame": 50, "end_frame": 71},
                        ]
                    },
                    {
                        "sequence_path": "/Game/__STAGE-0__/photostudio-portrait-20230122/sequences/look-1116/sequence-photostudio-portrait-20230122-1259_XLS",
                        "render_cuts": [
                            {"render_cut_id": "rc-09", "start_frame": 20, "end_frame": 41},
                            {"render_cut_id": "rc-10", "start_frame": 50, "end_frame": 71},
                        ]
                    },
                    {
                        "sequence_path": "/Game/__STAGE-0__/photostudio-portrait-20230122/sequences/look-1116/sequence-photostudio-portrait-20230122-1259_FS",
                        "render_cuts": [
                            {"render_cut_id": "rc-11", "start_frame": 20, "end_frame": 41},
                            {"render_cut_id": "rc-12", "start_frame": 50, "end_frame": 71},
                        ]
                    },
                    {
                        "sequence_path": "/Game/__STAGE-0__/photostudio-portrait-20230122/sequences/look-1116/sequence-photostudio-portrait-20230122-1259_MS",
                        "render_cuts": [
                            {"render_cut_id": "rc-13", "start_frame": 20, "end_frame": 41},
                            {"render_cut_id": "rc-14", "start_frame": 50, "end_frame": 71},
                        ]
                    },
                    {
                        "sequence_path": "/Game/__STAGE-0__/photostudio-portrait-20230122/sequences/look-1116/sequence-photostudio-portrait-20230122-1259_CU",
                        "render_cuts": [
                            {"render_cut_id": "rc-15", "start_frame": 20, "end_frame": 41},
                            {"render_cut_id": "rc-16", "start_frame": 50, "end_frame": 71},
                        ]
                    }

                ],
            }
        ]

        sequence_instructions = {
            "preset": "/Game/__STAGE-0__/photostudio-portrait-20230122/presets/preset-photostudio-portrait-20230122-2145-HDAA1x1",
            "scenes": scenes,
            "tracks": {
                "video": [
                    {"scene": "scene_0000", "render_cut_id": "rc-01", "start_frame": 21, "end_frame": 40,
                     "direction": "forward"},
                    {"scene": "scene_0000", "render_cut_id": "rc-02", "start_frame": 51, "end_frame": 60,
                     "direction": "forward"},
                    {"scene": "scene_0000", "render_cut_id": "rc-02", "start_frame": 61, "end_frame": 60,
                     "direction": "backward"},
                    {"scene": "scene_0000", "render_cut_id": "rc-03", "start_frame": 21, "end_frame": 40,
                     "direction": "forward"},
                    {"scene": "scene_0000", "render_cut_id": "rc-04", "start_frame": 21, "end_frame": 40,
                     "direction": "forward"},
                    {"scene": "scene_0000", "render_cut_id": "rc-05", "start_frame": 21, "end_frame": 40,
                     "direction": "forward"},
                    {"scene": "scene_0000", "render_cut_id": "rc-06", "start_frame": 21, "end_frame": 40,
                     "direction": "forward"},
                    {"scene": "scene_0000", "render_cut_id": "rc-07", "start_frame": 21, "end_frame": 40,
                     "direction": "forward"},
                    {"scene": "scene_0000", "render_cut_id": "rc-08", "start_frame": 21, "end_frame": 40,
                     "direction": "forward"},
                    {"scene": "scene_0000", "render_cut_id": "rc-09", "start_frame": 21, "end_frame": 40,
                     "direction": "forward"},
                    {"scene": "scene_0000", "render_cut_id": "rc-10", "start_frame": 21, "end_frame": 40,
                     "direction": "forward"},
                    {"scene": "scene_0000", "render_cut_id": "rc-11", "start_frame": 21, "end_frame": 40,
                     "direction": "forward"},
                    {"scene": "scene_0000", "render_cut_id": "rc-12", "start_frame": 21, "end_frame": 40,
                     "direction": "forward"},
                    {"scene": "scene_0000", "render_cut_id": "rc-13", "start_frame": 21, "end_frame": 40,
                     "direction": "forward"},
                    {"scene": "scene_0000", "render_cut_id": "rc-14", "start_frame": 21, "end_frame": 40,
                     "direction": "forward"},
                    {"scene": "scene_0000", "render_cut_id": "rc-15", "start_frame": 21, "end_frame": 40,
                     "direction": "forward"},
                    {"scene": "scene_0000", "render_cut_id": "rc-16", "start_frame": 21, "end_frame": 40,
                     "direction": "forward"},
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
        return sequence_instructions

        sequence_instructions = {
            "preset": "/Game/__STAGE-0__/photostudio-portrait-20230122/presets/preset-photostudio-portrait-20230122-2145-HDAA1x1",
            "scenes": scenes,
            "tracks": {
                "video": [
                    {"scene": "scene_0000", "render_cut_id": "rc-01", "start_frame": 20, "end_frame": 40,
                     "direction": "forward"},
                    {"scene": "scene_0000", "render_cut_id": "rc-02", "start_frame": 50, "end_frame": 60,
                     "direction": "forward"},
                    {"scene": "scene_0000", "render_cut_id": "rc-02", "start_frame": 60, "end_frame": 60,
                     "direction": "backward"},
                    {"scene": "scene_0000", "render_cut_id": "rc-03", "start_frame": 20, "end_frame": 40,
                     "direction": "forward"},
                    {"scene": "scene_0000", "render_cut_id": "rc-04", "start_frame": 50, "end_frame": 60,
                     "direction": "forward"},
                    {"scene": "scene_0000", "render_cut_id": "rc-05", "start_frame": 20, "end_frame": 40,
                     "direction": "forward"},
                    {"scene": "scene_0000", "render_cut_id": "rc-06", "start_frame": 50, "end_frame": 60,
                     "direction": "forward"},
                    {"scene": "scene_0000", "render_cut_id": "rc-07", "start_frame": 20, "end_frame": 40,
                     "direction": "forward"},
                    {"scene": "scene_0000", "render_cut_id": "rc-08", "start_frame": 50, "end_frame": 60,
                     "direction": "forward"},
                    {"scene": "scene_0000", "render_cut_id": "rc-09", "start_frame": 20, "end_frame": 40,
                     "direction": "forward"},
                    {"scene": "scene_0000", "render_cut_id": "rc-10", "start_frame": 50, "end_frame": 60,
                     "direction": "forward"},
                    {"scene": "scene_0000", "render_cut_id": "rc-11", "start_frame": 20, "end_frame": 40,
                     "direction": "forward"},
                    {"scene": "scene_0000", "render_cut_id": "rc-12", "start_frame": 50, "end_frame": 60,
                     "direction": "forward"},
                    {"scene": "scene_0000", "render_cut_id": "rc-13", "start_frame": 20, "end_frame": 40,
                     "direction": "forward"},
                    {"scene": "scene_0000", "render_cut_id": "rc-14", "start_frame": 50, "end_frame": 60,
                     "direction": "forward"},
                    {"scene": "scene_0000", "render_cut_id": "rc-15", "start_frame": 20, "end_frame": 40,
                     "direction": "forward"},
                    {"scene": "scene_0000", "render_cut_id": "rc-16", "start_frame": 50, "end_frame": 60,
                     "direction": "forward"},
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
