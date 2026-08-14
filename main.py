import argparse
import os
import shutil

from rich.console import Console
from rich.panel import Panel
from rich.progress import track

console = Console()

# Expanded categories including programs/installers
EXTENSIONS = {
    "Programs": [".exe", ".msi", ".dmg", ".pkg", ".deb", ".rpm", ".AppImage",".apk"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".webm"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".json", ".sh"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
}


def organize_folder(target_dir):
  if not os.path.exists(target_dir):
    console.print(
        f"[bold red]Error:[/bold red] Directory '{target_dir}' does not exist!"
    )
    return

  console.print(
      Panel.fit(
          "[bold cyan]🚀 CYBER-CLEAN: CLI File Organizer[/bold cyan]",
          border_style="magenta",
      )
  )

  files = [
      f
      for f in os.listdir(target_dir)
      if os.path.isfile(os.path.join(target_dir, f))
  ]

  if not files:
    console.print("[yellow]Directory is already clean![/yellow]")
    return

  # Create category folders
  for category in EXTENSIONS:
    os.makedirs(os.path.join(target_dir, category), exist_ok=True)
  os.makedirs(os.path.join(target_dir, "Others"), exist_ok=True)

  moved_count = 0

  # Process files with a gorgeous progress bar
  for file in track(files, description="[green]Sorting files..."):
    file_path = os.path.join(target_dir, file)
    _, ext = os.path.splitext(file)
    ext = ext.lower()

    target_category = "Others"
    for category, exts in EXTENSIONS.items():
      if ext in exts:
        target_category = category
        break

    dest_path = os.path.join(target_dir, target_category, file)
    shutil.move(file_path, dest_path)
    moved_count += 1

  console.print(
      f"\n[bold green]✨ Successfully sorted {moved_count} files into"
      " categories![/bold green]"
  )


if __name__ == "__main__":
  parser = argparse.ArgumentParser(
      description=(
          "A sleek cyberpunk CLI tool to automatically organize files into"
          " categories."
      )
  )

  # Making the path argument required
  parser.add_argument(
      "path", help="Path to the directory you want to organize"
  )

  args = parser.parse_args()
  organize_folder(args.path)
