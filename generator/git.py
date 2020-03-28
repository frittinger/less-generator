"""git handling"""

import subprocess


def create_git_repo(repo_name):
    result = subprocess.run(["git", "init", repo_name], check=True)
