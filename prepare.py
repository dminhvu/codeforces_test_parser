import os
import sys
import shutil
import requests
from bs4 import BeautifulSoup

base_folder = 'samples'

def generate(contest_id,problem_ids):
    if os.path.exists(base_folder):
        shutil.rmtree(base_folder,ignore_errors=True)
    os.makedirs(base_folder,exist_ok=True)

    for problem_id in problem_ids:
        os.makedirs(f'{base_folder}/{contest_id}/{problem_id}',exist_ok=True)
        url = f"https://codeforces.com/contest/{contest_id}/problem/{problem_id}"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        inputs = soup.find_all('div', class_='input')
        for i, inp in enumerate(inputs):
            content = inp.find_next('pre')
            with open(f'{base_folder}/{contest_id}/{problem_id}/input{i}.txt','w') as f:
                f.writelines(content.text[1:])

        outputs = soup.find_all('div', class_='output')
        for i, out in enumerate(outputs):
            content = out.find_next('pre')
            with open(f'{base_folder}/{contest_id}/{problem_id}/output{i}.txt','w') as f:
                f.writelines(content.text[1:])
    print('Succesfully downloaded all samples!')

if __name__=='__main__':
    args = sys.argv[1:]
    generate(args[0],args[1:])