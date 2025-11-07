import os
import glob
import argparse


def system(cmd):
    print(cmd+'\n')
    return os.system(cmd)


def user_confirm(msg):
    confirm = input(msg+'\n> ')
    while confirm not in ['y', 'n']:
        confirm = input('\nplease enter y/n to confirm or cancel\n> ')
    return confirm == 'y'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Git Repository Utility - Split large files for bypassing GitHub file size limit"
    )
    parser.add_argument(
        "large_file_log",
        nargs="?",
        default="large_files.log",
        help="Path to large file log (default: large_files.log)"
    )
    parser.add_argument(
        "--merge",
        action="store_true",
        help="To merge large file parts instead of splitting"
    )
    parser.add_argument(
        "--clear",
        action="store_true",
        help="To clear splitted original files or merged file parts. BE CAUTIOUS!"
    )
    args = parser.parse_args()
    
    mode = 'merge' if args.merge else 'split'
    to_clear = args.clear
    with open(args.large_file_log) as f:
        files = [line.strip() for line in f.read().split('\n') if line.strip() and not line.strip().startswith('#')]
    print(f"found {len(files)} files, mode: {mode}\n")
    
    for file in files:
        if mode == 'merge':
            if os.path.exists(file):
                print(f"warning: file {file} already exists when merging\n", flush=True)
                continue
            errno = system(f"cat \"{file}\".* > \"{file}\"")
            if errno != 0:
                print(f'error when merging {file}, errno: {errno}\n', flush=True)
            else:
                if to_clear and user_confirm(f"to remove {glob.glob(f'{file}.*')}? [y/n]"):
                    system(f"rm \"{file}\".*")
        else:
            if not os.path.exists(file):
                print(f"warning: file {file} does not exist when splitting\n", flush=True)
                continue
            if glob.glob(f'{file}.*'):
                print(f"warning: file parts of {file} may exist and be covered, please check\n", flush=True)
                continue
            errno = system(f"split -d -b 100M \"{file}\" \"{file}\".")
            if errno != 0:
                print(f'error when splitting {file}, errno: {errno}\n', flush=True)
            else:
                if to_clear and user_confirm(f"to remove {glob.glob(file)}? [y/n]"):
                    system(f"rm \"{file}\"")

    print('done')
    pass
