'''
@Author: Pavan Nakate
@Date: 2021-12-06 03:30
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : CLICommands 
'''
# Importing subprocess
import subprocess

def run_cmd(args_list):
    """
    Description:
        this function execute CLI commands
    Parameter:
        list of command words and paths of local system and hadoop system
    Return:
        output and error/warnning
    """
    print('Running command: {0}'.format(' '.join(args_list)))
    proc = subprocess.Popen(args_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE,universal_newlines=True)
    p_output, p_err = proc.communicate()
    return  p_output, p_err


version= run_cmd(['hadoop', 'version'])
print(version)

new_directory= run_cmd(['hadoop', 'fs', '-mkdir', '/SubProcessDemo'])
print(new_directory)

list_all_directory= run_cmd(['hadoop', 'fs', '-ls', '/'])
print(list_all_directory)

put_command= run_cmd(['hadoop', 'fs', '-put', '/home/pavan-linux/WordFile/HadoopInfo', '/SubProcessDemo'])
print(put_command)

copy_from_local= run_cmd(['hadoop', 'fs', '-copyFromLocal', '/home/pavan-linux/SubProcess/DemoText.txt', '/SubProcessDemo'])
print(copy_from_local)

cat= run_cmd(['hadoop', 'fs', '-cat', '/SubProcessDemo/DemoText.txt'])
print(cat)

get= run_cmd(['hadoop', 'fs', '-get', '/SubProcessDemo/HadoopInfo', '/home/pavan-linux/CopyFromHadoop'])
print(get)

copy_to_local= run_cmd(['hadoop', 'fs', '-copyToLocal', '/SubProcessDemo/DemoText.txt', '/home/pavan-linux/CopyFromHadoop'])
print(copy_to_local)

copy= run_cmd(['hadoop', 'fs', '-cp', '/SubProcessDemo/DemoText.txt', '/NewDemo'])
print(copy)

remove_directory= run_cmd(['hadoop', 'fs', '-rm', '-R', '/SubProcessDemo'])
print(remove_directory)