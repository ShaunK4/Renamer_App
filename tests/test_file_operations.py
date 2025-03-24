import unittest
import tempfile
import os
import pandas as pd
from pathlib import Path
from renamer import file_operations

class DummyOutput:
    """
    Dummy output widget to capture output from functions expecting a
    tkinter text widget. It implements a simple 'insert' method.
    """
    def __init__(self):
        self.contents = []

    def insert(self, index, text, *args, **kwargs):
        self.contents.append(text)

    def get_text(self):
        return "".join(self.contents)

class TestFileOperations(unittest.TestCase):
    def test_read_excel_table_valid(self):
        # Create a temporary Excel file with mapping data.
        with tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False) as tmp:
            tmp_file = tmp.name

        df = pd.DataFrame({
            "Old Filename": ["test", "example"],
            "New Filename": ["renamed_test", "renamed_example"]
        })
        df.to_excel(tmp_file, index=False)

        mapping = file_operations.read_excel_table(tmp_file)
        self.assertEqual(mapping, {"test": "renamed_test", "example": "renamed_example"})

        os.remove(tmp_file)  # Clean up temporary file.

    def test_read_excel_table_invalid(self):
        # Attempt to read a non-existent file; expect an empty mapping.
        mapping = file_operations.read_excel_table("non_existent_file.xlsx")
        self.assertEqual(mapping, {})

    def test_rename_files(self):
        # Create a temporary directory with a test file.
        with tempfile.TemporaryDirectory() as tmpdirname:
            tmpdir = Path(tmpdirname)
            # Create a test file that matches our regex (e.g., "test_1.txt").
            original_file = tmpdir / "test_1.txt"
            original_file.write_text("dummy content")

            # Dummy mapping: maps 'test' to 'renamed'.
            mapping = {"test": "renamed"}
            dummy_output = DummyOutput()

            file_operations.rename_files(str(tmpdir), mapping, dummy_output)

            # Check that the file has been renamed to "renamed_1.txt".
            expected_file = tmpdir / "renamed_1.txt"
            self.assertTrue(expected_file.exists(), f"Expected file {expected_file} not found.")

if __name__ == '__main__':
    unittest.main()
