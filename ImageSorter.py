import os
import shutil
import argparse
from collections import defaultdict

def get_image_files(root_dir, depth, exclude_dirs, debug):
    image_extensions = ["jpg", "jpeg", "gif", "png", "webp", "heic", "bmp"]
    files = []
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Determine the depth of the current directory
        current_depth = dirpath[len(root_dir):].count(os.sep) + 1
        
        # Skip directories at depths greater than specified
        if current_depth > depth:
            continue
        
        # Skip specified exclude directories
        if os.path.basename(dirpath).lower() in exclude_dirs:
            dirnames[:] = []
            continue
        
        for filename in filenames:
            if any(filename.lower().endswith(ext) for ext in image_extensions):
                files.append((dirpath, filename))
                if debug:
                    print(f"Found image file: {os.path.join(dirpath, filename)}")
    return files

def organize_files(files, root_dir, dry_run, debug):
    move_plan = defaultdict(list)
    
    for dirpath, filename in files:
        ext = filename.split('.')[-1].lower()
        target_dir = os.path.join(root_dir, ext)
        
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
            if debug:
                print(f"Created directory: {target_dir}")
        
        original_path = os.path.join(dirpath, filename)
        target_path = os.path.join(target_dir, filename)
        
        counter = 1
        while os.path.exists(target_path):
            name, ext = os.path.splitext(filename)
            target_path = os.path.join(target_dir, f"{name}({counter}){ext}")
            counter += 1
        
        move_plan[original_path].append(target_path)
        
        if debug:
            print(f"Planned move: {original_path} -> {target_path}")
    
    if dry_run:
        print("\nPlanned operations:")
        for src, targets in move_plan.items():
            for target in targets:
                print(f"Would move: {src} -> {target}")
    else:
        for src, targets in move_plan.items():
            for target in targets:
                shutil.move(src, target)
                print(f"Moved: {src} -> {target}")

def main():
    parser = argparse.ArgumentParser(description="Organize images by extension")
    parser.add_argument("path", type=str, help="Directory path to organize")
    parser.add_argument("-a", action="store_true", help="Organize all image files by extension")
    parser.add_argument("-t", type=str, help="Organize only specified image extension (e.g., 'jpg')")
    parser.add_argument("-l", type=int, default=1, help="Set directory depth (e.g., 2, 3, 4, ...)")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.path):
        print("Error: Specified path is not a directory")
        return
    
    if args.debug:
        print(f"Organizing images in directory: {args.path}")
        print(f"Options -a: {args.a}, -t: {args.t}, -l: {args.l}, --debug: {args.debug}")
    
    exclude_dirs = ["jpg", "jpeg", "gif", "png", "webp", "heic", "bmp"]
    
    if args.a:
        files = get_image_files(args.path, args.l, exclude_dirs, args.debug)
    elif args.t:
        files = get_image_files(args.path, args.l, exclude_dirs, args.debug)
        files = [(dirpath, filename) for dirpath, filename in files if filename.lower().endswith(args.t.lower())]
    else:
        print("Error: You must specify either -a or -t option")
        return
    
    if args.debug:
        print(f"Found {len(files)} image files to organize.")
    
    organize_files(files, args.path, dry_run=True, debug=args.debug)
    
    confirmation = input("\nDo you want to proceed with these changes? (y/n): ")
    if confirmation.lower() == 'y':
        organize_files(files, args.path, dry_run=False, debug=args.debug)
    else:
        print("Operation cancelled.")

if __name__ == "__main__":
    main()

