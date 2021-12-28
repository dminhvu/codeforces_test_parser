#!"python"
# in case this file does not run, please replace "python" with your "path/to/python.exe"
# if you do not know where it is, type "where.exe python" in your terminal

import os
import sys
import subprocess

# workspace folder
workspace_folder = "E:\Code\CompetitiveProgramming\Coding Problems\Codeforces" # replace path/to/your/source_file.cpp here
# contest id, e.g. 1620 for Educational Codeforces Round 119
base_folder = 'samples'
contest_id = os.listdir(base_folder)[0]

def run_sample(problem_id):

    if not os.path.exists(f'{base_folder}\{contest_id}\{problem_id}'):
        print(f'You have not downloaded sample tests for problem {problem_id}!')
        print(f'Downloading...')
        os.system(f'.\prepare {contest_id} {problem_id}')
        print(f'Sample test(s) for problem {problem_id} have been downloaded!')

    print(f'Running problem {problem_id}...')

    if not os.path.exists(f'{workspace_folder}\{contest_id}{problem_id}.cpp'):
        print(f'There is no source file for problem {problem_id}!')
        return

    # these are paths to cpp file and exe file
    # please change this to suit your folder structure
    # in this case, filename is "E:\...\Codeforces\1620A.cpp"
    # if your file is at "...\Codeforces\Educational Codeforces Round 119\A.cpp" for example
    # then change path_to_cpp_file = f'{workspace_folder}\{contest_name}\{problem_id}.cpp
    # with contest_name = "Education Codeforces Round 119" and problem_id = "A"
    # do not forget to change path_to_exe_file as well

    path_to_cpp_file = f'{workspace_folder}\{contest_id}{problem_id}.cpp'
    path_to_exe_file = f'{workspace_folder}\{contest_id}{problem_id}.exe'
    os.system(f'g++ "{path_to_cpp_file}" -o "{path_to_exe_file}')
    print('Successfully compiled!')
    print()

    n_cases = len(os.listdir(f'{base_folder}/{contest_id}/{problem_id}'))//2 # number of sample test cases
    n_correct = 0 # count correct test cases

    for i in range(n_cases):
        print(f'Sample case #{i+1}:',end=' ')
        with open(f'{base_folder}/{contest_id}/{problem_id}/input{i}.txt') as f:
            inp = f.read()

            process = subprocess.Popen(f'"{path_to_exe_file}"', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            process.stdin.write(str(inp).encode())

            # pre-processing your output, do not change this
            your_output = process.communicate()[0]
            your_output = your_output.decode().strip()
            original_your_output = your_output.rstrip('\n')
            your_output = " ".join(your_output.splitlines())
            your_output = " ".join(your_output.split()).rstrip('\n')

            with open(f'{base_folder}/{contest_id}/{problem_id}/output{i}.txt') as f2:
                # pre-processing actual output, do not change this
                output = f2.read().strip()
                original_output = output
                output = " ".join(output.splitlines())
                output = " ".join(output.split())

                # compare your output vs actual output
                if your_output == output:
                    print('Correct!')
                    n_correct += 1
                else:
                    print('Failed!')
                print('-' * 10)
                # input
                print('Input:')
                print(inp.rstrip('\n'))
                print('-'*10)
                # your output
                print('Output:')
                print(original_your_output)
                # print(your_output) # debug
                print('-'*10)
                # expected output
                print('Expected:')
                print(original_output)
                # print(output) # debug
                print('-'*10)

    print(f'Result: {n_correct} / {n_cases} case(s) passed!')
    os.remove(f'{workspace_folder}\{contest_id}{problem_id}.exe')

if __name__=='__main__':
    args =  sys.argv[1:]
    try:
        run_sample(args[0])
    except:
        print('Please provide one problem!')