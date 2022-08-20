import unittest
import os
from src.export_data.helper_dir_file_edit import *
from src.export_data.plantuml_generate import *

# import testbook


class Test_main(unittest.TestCase):

    # Initialize test object
    def __init__(self, *args, **kwargs):
        super(Test_main, self).__init__(*args, **kwargs)
        self.script_dir = self.get_script_dir()
        self.project_name = "Whitepaper"

    # returns the directory of this script regardles of from which level the code is executed
    def get_script_dir(self):
        return os.path.dirname(__file__)

    def test_if_plantuml_file_is_outputted(self):
        diagram_text_filename = "trivial_gantt.uml"

        dynamic_diagram_dir_relative_to_root = (
            f"code/{self.project_name}/src/Diagrams/Dynamic_diagrams"
        )
        diagram_text_filepath_relative_to_root = (
            f"{dynamic_diagram_dir_relative_to_root}/{diagram_text_filename}"
        )

        create_dir_relative_to_root_if_not_exists(dynamic_diagram_dir_relative_to_root)
        self.assertTrue(
            dir_relative_to_root_exists(dynamic_diagram_dir_relative_to_root)
        )

        # Generate a PlantUML diagram.
        filename, lines = create_trivial_gantt(diagram_text_filename)
        output_diagram_text_file(filename, lines, dynamic_diagram_dir_relative_to_root)

        # Assert file exist.
        self.assertTrue(os.path.exists(diagram_text_filepath_relative_to_root))

        # TODO: Assert file content is correct.

        # Cleanup after
        delete_dir_relative_to_root_if_not_exists(dynamic_diagram_dir_relative_to_root)
        self.assertFalse(
            dir_relative_to_root_exists(dynamic_diagram_dir_relative_to_root)
        )
