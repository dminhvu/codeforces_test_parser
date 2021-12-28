import os
import sys
import subprocess

workspace_folder = "E:\Code\CompetitiveProgramming\Coding Problems\Codeforces" # replace path/to/your/source_file.cpp here

contest_id = os.listdir('samples/')[0]

def run_sample(problem_id):
    print(f'Running problem {problem_id}...')
    if not os.path.exists(f"{workspace_folder}\{contest_id}{problem_id}.cpp"):
        print(f'There is no source file for problem {problem_id}!')
        return
    os.system(f'g++ "{workspace_folder}\{contest_id}{problem_id}.cpp" -o "{workspace_folder}\{contest_id}{problem_id}.exe"')
    print('Successfully compiled!')
    print()
    n_cases = len(os.listdir(f'samples/{contest_id}/{problem_id}'))//2
    n_correct = 0
    for i in range(n_cases):
        print(f'Sample case #{i+1}:',end=' ')
        with open(f'samples/{contest_id}/{problem_id}/input{i}.txt') as f:
            inp = f.read()

            process = subprocess.Popen(f'"{workspace_folder}\{contest_id}{problem_id}.exe"', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            process.stdin.write(str(inp).encode())

            your_output = process.communicate()[0]
            your_output = your_output.decode()
            original_your_output = your_output.rstrip('\n')
            your_output = "".join(your_output.splitlines())
            your_output = " ".join(your_output.split()).rstrip('\n')

            with open(f'samples/{contest_id}/{problem_id}/output{i}.txt') as f2:

                output = f2.read().strip()
                original_output = output
                output = "".join(output.splitlines())
                output = " ".join(output.split())
                if your_output == output:
                    print('Correct!')
                    n_correct += 1
                else:
                    print('Failed!')

                print('Input:')
                print(inp.rstrip('\n'))
                print()

                print('Output:')
                print(original_output)
                print()
                # print(output)

                print('Your output:')
                print(original_your_output)
                print()
                # print(your_output)

    print(f'Result: {n_correct}/{n_cases} case(s) passed!')
    os.remove(f"{workspace_folder}\{contest_id}{problem_id}.exe")

if __name__=='__main__':
    args =  sys.argv[1:]
    try:
        run_sample(args[0])
    except:
        print('Please provide one problem!')