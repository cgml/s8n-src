import unittest
import sequencer_instructions_builder as sib
from golden_data import GoldenData


class SequencerInstructionsBuilderTests(unittest.TestCase):
    def test_create_storyboard(self):
        pass

    def test_instructions_build_sequencer(self):
        builder = sib.SequenceInstructionsBuilder()
        instructions = builder.create_instructions(storyboard=GoldenData.storyboard)
        print(instructions)
        self.assertTrue('camera_shots' in instructions['scenes'][0])
        self.assertTrue('video' in instructions['tracks'])
        self.assertTrue('audio' in instructions['tracks'])
        self.assertTrue('music' in instructions['tracks']['audio'])
