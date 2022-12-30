import unittest
from unittest.mock import MagicMock

from golden_data import GoldenData
from sequence_instructions_executor import SequenceInstructionsExecutor


class SequenceInstructionsExecutorTests(unittest.TestCase):

    def test_process_sequence_instructions(self):

        executor = SequenceInstructionsExecutor()
        executor._open_level = MagicMock()
        executor._delete_sequence = MagicMock()
        executor._create_sequence = MagicMock()
        executor._render_scene_sequence = MagicMock()
        executor.process_sequence_instructions(sequence_instructions=GoldenData.sequence_instructions)

        self.assertEqual(1, executor._delete_sequence.call_count)
        self.assertEqual("scene_0000", executor._delete_sequence.call_args[0])
        self.assertEqual(1, executor._create_sequence.call_count)
        self.assertEqual(executor.WORK_DIR, executor._create_sequence.call_args[0])
        self.assertEqual("scene_0000", executor._create_sequence.call_args[1])
