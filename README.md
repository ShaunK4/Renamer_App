![Renamer Banner](/readme_images/Renamer.png)

The Renamer Application is a Python GUI tool that allows users to rename files in a specified directory based on a mapping defined in an Excel file. It uses [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) for a modern interface and [pandas](https://pandas.pydata.org/) for handling Excel files.

## Features

- **Excel Mapping:** Read an Excel file with columns `Old Filename` and `New Filename` to determine the renaming scheme.
- **Flexible Renaming:** Supports files with numeric suffixes (e.g., `filename_1.txt` or `filename (1).txt`).
- **Conflict Handling:** Checks for conflicts to avoid overwriting files.
- **Export Template:** Easily export an Excel template to help users create their mapping files.

![GUI display image](/readme_images/gui_img.png)


## Examples

<details>

<summary>Bulk renaming .txt files with a numeric suffix (e.g., _1 or (1))</summary>

![File example image](/readme_images/file.png)

| Old Filename |  New Filename  |
|     :---:    |     :---:      |
| File 1       |  new_File 1    |
| File 2       |  new_File 2    |
| File 3       |  new_File 3    |
| File 4       |  new_File 4    |
| File 5       |  new_File 5    |

![Renamed file example](/readme_images/file_example.png)

</details>

<details>

<summary>Bulk renaming .png files with a numeric suffix (e.g., _1 or (1))<summary>

![File example image](/readme_images/img.png)

| Old Filename |  New Filename  |
|     :---:    |     :---:      |
|   img1       |     new_img1   |
|   img2       |     new_img2   |
|   img3       |     new_img3   |

![Renamed image example](/readme_images/img_example.png)

</details>

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
