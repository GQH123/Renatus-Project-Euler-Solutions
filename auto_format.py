import os
# import re
# import sys
import json
import math
import requests
from bs4 import BeautifulSoup
# import pdb

prefix = 'https://projecteuler.net/'
proxies = { "http": "http://host:7890", } 
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/79.0.3945.79 Chrome/79.0.3945.79 Safari/537.36',
    'Referer': prefix,
}
probinfo_json = 'ProblemInfo.json'


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def system(line):
    print(bcolors.WARNING + bcolors.BOLD + line + bcolors.ENDC)
    return os.system(line)


def get_url_text(url):
    while True:
        try:
            r = requests.get(url=url, headers=headers, proxies=proxies)
            assert r.status_code == 200
            return r.text
        except Exception as e:
            print('get fail...retrying')
            print(e)
            pass


def parse_problem_title(text, problem_id):
    posts = [] 
    soup = BeautifulSoup(text, features="lxml")
    # pdb.set_trace()
    for tag in soup.find_all('a', href="problem=%d" % problem_id):
        return tag.text


# https://projecteuler.net/archives;page=1
def process_problem_id(path, dir, problem_id, probinfo):
    if problem_id in probinfo and 'title' in probinfo[problem_id]:
        # print(f'problem {problem_id} already formatted')
        return
    problem_per_page = 50
    text = get_url_text('https://projecteuler.net/archives;page=%d' % math.ceil(problem_id/problem_per_page))
    title = parse_problem_title(text, problem_id)
    src_path = os.path.join(path, dir)
    dst_path = os.path.join(path, '%03d - %s' % (problem_id, title))
    if src_path == dst_path:
        # print(f'problem {problem_id} already formatted')
        pass
    else:
        system('mv "%s" "%s"' % (src_path, dst_path))
    
    if problem_id in probinfo:
        probinfo[problem_id] = {'title': title, **probinfo[problem_id]}  # place title at the first position
    else:
        probinfo[problem_id] = {'title': title}


def scan_dirs(path='.'):
    if not os.path.exists(os.path.join(path, probinfo_json)):
        probinfo = {}
    else:
        probinfo = json.load(open(os.path.join(path, probinfo_json)))
        # convert string keys to integers
        probinfo = {int(k): v for k, v in probinfo.items()}
    for dir in os.listdir(path):
        problem_id = -1
        try:
            problem_id = int(dir.split('-')[0].strip())
        except ValueError:
            continue
        process_problem_id(path, dir, problem_id, probinfo)
    # sort probinfo by problem_id
    probinfo = dict(sorted(probinfo.items(), key=lambda x: x[0]))
    probinfo = {'%03d' % k: v for k, v in probinfo.items()}
    json.dump(probinfo, open(os.path.join(path, probinfo_json), 'w'), indent=4, ensure_ascii=False)


if __name__ == '__main__':
    scan_dirs()
    pass
