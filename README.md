![Renamer Banner](\readme_images\Renamer.png)

The Renamer Application is a Python GUI tool that allows users to rename files in a specified directory based on a mapping defined in an Excel file. It uses [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) for a modern interface and [pandas](https://pandas.pydata.org/) for handling Excel files.

## Features

- **Excel Mapping:** Read an Excel file with columns `Old Filename` and `New Filename` to determine the renaming scheme.
- **Flexible Renaming:** Supports files with numeric suffixes (e.g., `filename_1.txt` or `filename (1).txt`).
- **Conflict Handling:** Checks for conflicts to avoid overwriting files.
- **Export Template:** Easily export an Excel template to help users create their mapping files.

## Installation

1. **Clone the Repository:**

  ```bash
   git clone https://github.com/ShaunK4/Renamer_App.git
   cd Renamer_App
  ```
2. **Create and Activate a Virtual Environment (Optional but Recommended):**

  ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
  ```

3. **Install the Dependencies:**

  ```bash
    pip install -r requirements.txt
  ```

## Usage

To start the application, run:

  ```bash
    python renamer.py
  ```
This will launch the GUI where you can select an Excel file, choose a directory, and perform the file renaming operation.

## Running Tests

To run the unit tests:

  ```bash
    python -m unittest discover tests
  ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have improvements or bug fixes.
