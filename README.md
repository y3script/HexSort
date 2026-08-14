# 🚀 HexSort: CLI File Organizer

A sleek, cyberpunk-inspired command-line interface (CLI) tool designed to automatically sort and organize messy directories into structured categories.

## ✨ Features

- **Cyberpunk UI:** Powered by `rich` to deliver vibrant console panels, colors, and an interactive progress bar.

- **Smart Categorization:** Automatically groups files into predefined folders based on their extensions.

- **Fallback Handling:** Unrecognized file types are safely swept into an **"Others"** directory.

- **Lightweight & Fast:** Built entirely using Python's standard libraries and styled with modern terminal formatting.

## 📂 Supported Categories

| **Category**  | **File Extensions**                                                 |
| ------------- | ------------------------------------------------------------------- |
| **Programs**  | `.exe`, `.msi`, `.dmg`, `.pkg`, `.deb`, `.rpm`, `.AppImage`, `.apk` |
| **Images**    | `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`, `.svg`                    |
| **Videos**    | `.mp4`, `.mov`, `.avi`, `.mkv`, `.webm`                             |
| **Documents** | `.pdf`, `.docx`, `.doc`, `.txt`, `.xlsx`, `.pptx`, `.csv`           |
| **Code**      | `.py`, `.js`, `.html`, `.css`, `.cpp`, `.json`, `.sh`               |
| **Archives**  | `.zip`, `.rar`, `.tar`, `.gz`, `.7z`                                |
| **Others**    | Any extension not listed above                                      |

## 🛠️ Installation & Setup (`uv`)

1. Ensure you have **Python 3.x** and **[uv](https://github.com/astral-sh/uv)** installed.

2. Initialize or navigate to your project directory, then add the required dependency:
   
   Bash
   
   ```
   uv add rich
   ```

3. Save the sorting script locally as `main.py`.

## 🚀 Usage

Run the script seamlessly using `uv run`:

Bash

```
uv run main.py /path/to/your/messy/folder
```

### Example

Bash

```
uv run main.py ~/Downloads
```

## 

## ⚠️ Disclaimer

> **Use with caution:** This script moves files directly into categorized subdirectories within the specified target path. Make sure to test it on a sample directory before running it on critical data.



## 🌐 Connect With the Developer

If you like this project or want to check out more web, app, and terminal-based software engineering projects, follow me here:

- **GitHub:** [@y3script](https://github.com/y3script)

- **Instagram:** [@yescript](https://instagram.com/yescript)



Made with 🐍, 💻, and a deep love for coding.
