import os
import time
import json
import argparse

from auto_format import get_problem_title

probinfo_json = 'ProblemInfo.json'


def make_problem_dir(problem_id):
    current_problem_dirs = os.listdir(".")
    problem_id_str = f'{problem_id:03d}'
    for dir in current_problem_dirs:
        if dir.startswith(problem_id_str):
            print(f"Problem {problem_id} already exists")
            return
    title = get_problem_title(problem_id)
    
    problem_info = json.load(open(probinfo_json))
    if problem_id_str in problem_info:
        print(f'warning: problem {problem_id_str} already in {probinfo_json} but no subdir found')
        problem_info[problem_id_str] = {'title': title, **problem_info[problem_id_str]}
    else:
        problem_info[problem_id_str] = {'title': title}
    problem_info = dict(sorted(problem_info.items(), key=lambda x: x[0]))
    json.dump(problem_info, open(probinfo_json, 'w'), indent=4, ensure_ascii=False)
    
    os.makedirs(f"{problem_id_str} - {title}")
    with open(f"{problem_id_str} - {title}/{problem_id}.py", "w") as f:
        f.write(f"# Problem {problem_id_str}. {title}\n")
        f.write(f"# Link: https://projecteuler.net/problem={problem_id}\n")
        f.write(f"# Answer: ?\n")
        f.write(f"# Language: Python\n")
        f.write(f"# Author: Renatus\n")
        f.write(f"# Date: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"import math\nfrom functools import lru_cache\n\n\n")
        f.write(f"def main():\n")
        f.write(f"    ...\n\n\n")
        f.write(f"if __name__ == '__main__':\n")
        f.write(f"    main()\n")
        f.write(f"    pass\n")
    os.system(f"cursor \"{problem_id_str} - {title}/{problem_id}.py\"")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("problem_id", type=int)
    args = parser.parse_args()

    problem_id = args.problem_id
    make_problem_dir(problem_id)
    pass
