import os
import shutil
import argparse
import logging

IMAGE_EXTENSIONS = ["jpg", "jpeg", "png", "gif", "webp", "heic", "bmp"]

def setup_logging(debug):
    logging.basicConfig(level=logging.DEBUG if debug else logging.INFO, format='%(message)s')

def scan_directory(directory, depth):
    files_to_move = {}
    for root, _, files in os.walk(directory):
        current_depth = root[len(directory):].count(os.sep)
        if depth is not None and current_depth > depth:
            continue

        for file in files:
            ext = file.lower().rsplit('.', 1)[-1]
            if ext in IMAGE_EXTENSIONS:
                src_path = os.path.join(root, file)
                if ext not in files_to_move:
                    files_to_move[ext] = []
                files_to_move[ext].append(src_path)
        if depth is None:  # If depth is not specified, only process the top-level directory
            break
    return files_to_move

def display_move_plan(files_to_move):
    for ext, files in files_to_move.items():
        logging.info(f"\nFiles to move to '{ext}' directory:")
        for file in files:
            logging.info(f"  {file}")
    logging.info("\nDo you want to proceed with the file move? (yes/no): ")
    return input().strip().lower() == 'yes'

def move_files(files_to_move, directory):
    for ext, files in files_to_move.items():
        ext_dir = os.path.join(directory, ext)
        if not os.path.exists(ext_dir):
            os.makedirs(ext_dir)
            logging.debug(f"Created directory: {ext_dir}")

        for file in files:
            dest_path = os.path.join(ext_dir, os.path.basename(file))
            shutil.move(file, dest_path)
            logging.info(f"Moved {file} to {dest_path}")

def main():
    parser = argparse.ArgumentParser(description="Sort and move image files by extension.")
    parser.add_argument('directory', type=str, help='Directory path to organize.')
    parser.add_argument('-a', action='store_true', help='Sort and move all image files by extension.')
    parser.add_argument('-t', type=str, help='Sort and move image files with the specified extension.')
    parser.add_argument('-l', type=int, help='Depth of subdirectories to include.')
    parser.add_argument('--debug', action='store_true', help='Enable debug logging.')

    args = parser.parse_args()

    setup_logging(args.debug)

    if not os.path.isdir(args.directory):
        logging.error(f"Directory does not exist: {args.directory}")
        return

    if args.a:
        files_to_move = scan_directory(args.directory, args.l)
    elif args.t:
        if args.t not in IMAGE_EXTENSIONS:
            logging.error(f"Unsupported image extension: {args.t}")
            return
        files_to_move = scan_directory(args.directory, args.l)
        files_to_move = {args.t: files_to_move.get(args.t, [])}
    else:
        logging.error("You must specify either the -a option or the -t option.")
        return

    if not files_to_move:
        logging.info("No files to move.")
        return

    if display_move_plan(files_to_move):
        move_files(files_to_move, args.directory)
        logging.info("File move completed.")
    else:
        logging.info("File move aborted.")

if __name__ == "__main__":
    main()

