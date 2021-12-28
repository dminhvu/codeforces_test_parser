#!"python"
# in case this file does not run, please replace "python" with your "path/to/python.exe"
# if you do not know where it is, type "where.exe python" in your terminal

import os
import sys
import shutil
import requests
from bs4 import BeautifulSoup

base_folder = 'samples'

def generate(contest_id,problem_ids):
    print(f'Downloading...')
    os.makedirs(f'{base_folder}\{contest_id}', exist_ok=True)
    for folder in os.listdir(base_folder):
        if folder == str(contest_id):
            continue
        shutil.rmtree(f'{base_folder}/{folder}',ignore_errors=True)

    for problem_id in problem_ids:
        os.makedirs(f'{base_folder}/{contest_id}/{problem_id}',exist_ok=True)
        url = f"https://codeforces.com/contest/{contest_id}/problem/{problem_id}"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        inputs = soup.find_all('div', class_='input')
        for i, inp in enumerate(inputs):
            for br in inp.find_all('br'):
                br.replace_with("\n")
            content = inp.find_next('pre')
            with open(f'{base_folder}/{contest_id}/{problem_id}/input{i}.txt','w') as f:
                f.writelines(str(content.text).strip())

        outputs = soup.find_all('div', class_='output')
        for i, out in enumerate(outputs):
            for br in out.find_all('br'):
                br.replace_with("\n")
            content = out.find_next('pre')
            with open(f'{base_folder}/{contest_id}/{problem_id}/output{i}.txt','w') as f:
                f.writelines(str(content.text).strip())
    print('Succesfully downloaded all samples!')

if __name__=='__main__':
    args = sys.argv[1:]
    generate(args[0],args[1:])