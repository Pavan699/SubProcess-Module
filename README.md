# SubProcess-Module

Hadoop Version :- Hadoop 3.2.2

Use of subprocess module to run the CLI commands.

By using Subprocess library to execute Hadoop commands in Python Subprocess library is used to run any terminal commands using python

# subprocess.run(["hadoop","command"])
to run any hadoop command It prints output of terminal directly in console to store in separate variable we use

stdout=subprocess.PIPE
stderr=subprocess.PIPE
Text=True output = subprocess.run(["hadoop","command"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) To Print output we se Print(output.stdout) To Print error traceback we se Print(output.stderr) To get number of errors occurd in command is Print(output.returncode)
