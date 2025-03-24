import pandas as pd
import re
import logging
from pathlib import Path
from typing import Dict
import tkinter as tk
from tkinter import scrolledtext

# Configure logging for debugging and error messages
logging.basicConfig(level=logging.INFO)


def read_excel_table(excel_file: str) -> Dict[str, str]:
  """
  Read Excel table and extract filename mapping
  """

  try:
    df = pd.read_excel(excel_file, dtype={'Old Filename': str, 'New Filename': str})
    filename_mapping = df.set_index('Old Filename')['New Filename'].to_dict()
    return filename_mapping
  except FileNotFoundError as fnf_error:
    logging.error("Excel file not found: %s", fnf_error)
    return {}
  except ValueError as ve:
    logging.error("Error processing Excel file: %s", ve)
    return {}
  except Exception as e:
    logging.error("Unexpected error reading Excel file: %s", e)
    return {}
 

def rename_files(directory: str, filename_mapping: Dict[str, str], output_text: scrolledtext.ScrolledText) -> None:
    """
    Rename files in the specified directory based on the filename mapping.
    """
    directory_path = Path(directory)
    if not directory_path.exists():
        output_text.insert(tk.END, "Error: The specified directory does not exist.\n", 'error')
        return

    renaming_output = []
    files = list(directory_path.iterdir())

    # Normalize mapping keys to lowercase.
    filename_mapping = {k.lower(): v for k, v in filename_mapping.items()}

    if not filename_mapping:
        output_text.insert(tk.END, "Error: No filename mapping provided.\n", 'error')
        return

    for file in files:
        if file.is_file():
            base_filename = file.stem
            file_extension = file.suffix

            match = re.match(r'(.+?)(?:_\d+|\s*\(\d+\))', base_filename)
            if not match:
                output_text.insert(tk.END, f"No match found for file {file.name}. Skipping...\n", 'error')
                continue

            prefix = match.group(1).lower()
            if prefix in filename_mapping:
                new_filename = filename_mapping[prefix] + base_filename[len(prefix):] + file_extension
                new_path = file.parent / new_filename

                if new_path.exists():
                    output_text.insert(tk.END, f"File {new_filename} already exists. Skipping rename for {file.name}.\n", 'error')
                    continue

                try:
                    file.rename(new_path)
                    renaming_output.append(f"Renamed: {file.name} -> {new_filename}")
                except Exception as e:
                    output_text.insert(tk.END, f"Error renaming file {file.name}: {str(e)}\n", 'error')
            else:
                output_text.insert(tk.END, f"No match found for file {file.name} in the filename mapping. Skipping...\n", 'error')

    output_text.insert(tk.END, "\n".join(renaming_output))


def export_template(output_text: scrolledtext.ScrolledText) -> None:
    """
    Export an Excel template with headers for filename mapping.
    """
    try:
        template_df = pd.DataFrame(columns=['Old Filename', 'New Filename'])
        from tkinter import filedialog  # Import locally since it's a GUI interaction.
        save_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
        if not save_path:
            output_text.insert(tk.END, "Template export canceled.\n")
            return
        template_df.to_excel(save_path, index=False)
        output_text.insert(tk.END, f"Exported template to {save_path}\n")
    except Exception as e:
        output_text.insert(tk.END, f"Error exporting template: {e}\n")