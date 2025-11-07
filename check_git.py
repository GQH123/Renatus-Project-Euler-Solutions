#!/usr/bin/env python3
"""
Git Repository Utility Script

This script provides various Git-related functions including:
- Checking for files larger than Git's file size limit
- Finding untracked files
- Checking repository status
- Finding files that should be ignored
"""

import os
import sys
import argparse
import subprocess
from pathlib import Path
from typing import List, Tuple, Optional
import fnmatch

# Git's default file size limit (100MB in bytes)
DEFAULT_GIT_FILE_LIMIT = 100 * 1024 * 1024  # 100MB


def format_file_size(size_bytes: int) -> str:
    """Convert bytes to human readable format."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} TB"


def is_git_repository(path: str = ".") -> bool:
    """Check if the current directory is a Git repository."""
    try:
        subprocess.run(
            ["git", "rev-parse", "--git-dir"],
            cwd=path,
            capture_output=True,
            check=True
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def get_gitignore_patterns(repo_path: str = ".") -> List[str]:
    """Read .gitignore patterns from the repository."""
    gitignore_path = Path(repo_path) / ".gitignore"
    patterns = []
    
    if gitignore_path.exists():
        with open(gitignore_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    patterns.append(line)
    
    return patterns


def is_ignored_by_gitignore(file_path: str, patterns: List[str], repo_path: str = ".") -> bool:
    """Check if a file would be ignored by .gitignore patterns."""
    relative_path = os.path.relpath(file_path, repo_path)
    
    for pattern in patterns:
        if fnmatch.fnmatch(relative_path, pattern) or fnmatch.fnmatch(os.path.basename(relative_path), pattern):
            return True
    
    return False


def find_large_files(directory: str = ".", 
                    size_limit: int = DEFAULT_GIT_FILE_LIMIT,
                    check_git_tracking: bool = True) -> List[Tuple[str, int]]:
    """
    Find files larger than the specified size limit.
    
    Args:
        directory: Directory to search (default: current directory)
        size_limit: File size limit in bytes (default: 100MB)
        check_git_tracking: Whether to check if files are already tracked by Git
    
    Returns:
        List of tuples containing (file_path, file_size)
    """
    large_files = []
    repo_path = directory
    
    # Get gitignore patterns
    gitignore_patterns = get_gitignore_patterns(repo_path) if check_git_tracking else []
    
    # Get list of files already tracked by Git
    tracked_files = set()
    if check_git_tracking and is_git_repository(directory):
        try:
            result = subprocess.run(
                ["git", "ls-files"],
                cwd=directory,
                capture_output=True,
                text=True,
                check=True
            )
            tracked_files = set(result.stdout.strip().split('\n')) if result.stdout.strip() else set()
        except subprocess.CalledProcessError:
            pass
    
    # Walk through directory recursively
    for root, dirs, files in os.walk(directory):
        # Skip .git directory
        if '.git' in dirs:
            dirs.remove('.git')
        
        for file in files:
            file_path = os.path.join(root, file)
            
            try:
                file_size = os.path.getsize(file_path)
                
                if file_size > size_limit:
                    relative_path = os.path.relpath(file_path, repo_path)
                    
                    # Check if file is already tracked by Git
                    is_tracked = relative_path in tracked_files
                    
                    # Check if file would be ignored by .gitignore
                    is_ignored = is_ignored_by_gitignore(file_path, gitignore_patterns, repo_path)
                    
                    large_files.append((file_path, file_size, is_tracked, is_ignored))
                    
            except (OSError, IOError):
                # Skip files that can't be accessed
                continue
    
    return large_files


def get_untracked_files(directory: str = ".") -> List[str]:
    """Get list of untracked files in the Git repository."""
    if not is_git_repository(directory):
        return []
    
    try:
        result = subprocess.run(
            ["git", "ls-files", "--others", "--exclude-standard"],
            cwd=directory,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip().split('\n') if result.stdout.strip() else []
    except subprocess.CalledProcessError:
        return []


def get_git_status(directory: str = ".") -> Optional[str]:
    """Get Git repository status."""
    if not is_git_repository(directory):
        return None
    
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=directory,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None


def check_git_lfs_installed() -> bool:
    """Check if Git LFS is installed."""
    try:
        subprocess.run(
            ["git", "lfs", "version"],
            capture_output=True,
            check=True
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Git Repository Utility - Check for large files and repository status"
    )
    parser.add_argument(
        "directory",
        nargs="?",
        default=".",
        help="Directory to check (default: current directory)"
    )
    parser.add_argument(
        "--size-limit",
        type=int,
        default=DEFAULT_GIT_FILE_LIMIT,
        help=f"File size limit in bytes (default: {DEFAULT_GIT_FILE_LIMIT} = 100MB)"
    )
    parser.add_argument(
        "--size-mb",
        type=float,
        help="File size limit in MB (alternative to --size-limit)"
    )
    parser.add_argument(
        "--show-all",
        action="store_true",
        help="Show all large files, including tracked and ignored ones"
    )
    parser.add_argument(
        "--no-status",
        action="store_true",
        help="Do not show Git repository status"
    )
    parser.add_argument(
        "--no-untracked",
        action="store_true",
        help="Do not show untracked files"
    )
    
    args = parser.parse_args()
    
    # Convert MB to bytes if specified
    if args.size_mb:
        size_limit = int(args.size_mb * 1024 * 1024)
    else:
        size_limit = args.size_limit
    
    directory = os.path.abspath(args.directory)
    
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        sys.exit(1)
    
    print(f"Checking directory: {directory}")
    print(f"File size limit: {format_file_size(size_limit)}")
    print("-" * 60)
    
    # Check if it's a Git repository
    if is_git_repository(directory):
        print("✓ Git repository detected")
        
        # Check Git LFS
        if check_git_lfs_installed():
            print("✓ Git LFS is available")
        else:
            print("⚠ Git LFS is not installed (recommended for large files)")
    else:
        print("⚠ Not a Git repository")
    
    print()
    
    # Find large files
    print("Searching for large files...")
    large_files = find_large_files(directory, size_limit, True)
    
    if large_files:
        print(f"\nFound {len(large_files)} files larger than {format_file_size(size_limit)}:")
        print("-" * 60)
        
        problematic_files = []
        
        if large_files:
            large_files_log = open('large_files.log', 'w')
            
        for file_path, file_size, is_tracked, is_ignored in large_files:
            relative_path = os.path.relpath(file_path, directory)
            size_str = format_file_size(file_size)
            
            status_indicators = []
            if is_tracked:
                status_indicators.append("TRACKED")
            if is_ignored:
                status_indicators.append("IGNORED")
            
            status_str = f" [{', '.join(status_indicators)}]" if status_indicators else ""
            
            print(f"  {size_str:>10} - {relative_path}{status_str}")
            large_files_log.write(f"#{size_str:>10} {status_str}\n{os.path.abspath(file_path)}\n\n")
            
            # Mark as problematic if not tracked and not ignored
            if not is_tracked and not is_ignored:
                problematic_files.append((relative_path, file_size))
        
        if large_files:
            large_files_log.close()
        
        if problematic_files and not args.show_all:
            print(f"\n⚠ WARNING: {len(problematic_files)} large files are not tracked or ignored:")
            for file_path, file_size in problematic_files:
                print(f"  - {file_path} ({format_file_size(file_size)})")
            
            print("\nRecommendations:")
            print("1. Add large files to .gitignore if they shouldn't be tracked")
            print("2. Use Git LFS for large files that should be version controlled")
            print("3. Consider reducing file sizes or splitting large files")
    else:
        print(f"✓ No files larger than {format_file_size(size_limit)} found")
    
    # Show Git status if requested
    if not args.no_status:
        print("\nGit Status:")
        print("-" * 60)
        status = get_git_status(directory)
        if status:
            print(status)
        else:
            print("Repository is clean or not a Git repository")
    
    # Show untracked files if requested
    if not args.no_untracked:
        print("\nUntracked Files:")
        print("-" * 60)
        untracked = get_untracked_files(directory)
        if untracked:
            for file in untracked:
                print(f"  {file}")
        else:
            print("No untracked files")


if __name__ == "__main__":
    main()
