import os
import re

# clean the file from previous run
os.system('rm execution_command.txt')

# declare the input variables
PATTERN = [0, 1, 2, 3, 4, 5, 6]
PATTERN_SIZE = [4, 8]
PACKET_SIZE = [1, 2 ,4, 8, 16]
INJECTION_GAP = [0, 1, 3, 5, 11]

# generate the command line and store in the file
with open('execution_command.txt', 'w') as COMMAND:

	for i, pattern in enumerate(PATTERN):
		for j, pattern_size in enumerate(PATTERN_SIZE):
			for k, packet_size in enumerate(PACKET_SIZE):
				for l, injection_gap in enumerate(INJECTION_GAP):
					#print("./ClusterFPGASim.exe -i %d -s %d -p %d -g %d" % (pattern, pattern_size, packet_size, injection_gap))
					COMMAND.write('./ClusterFPGASim.exe -i '+str(pattern)+' -s '+str(pattern_size)+' -p '+str(packet_size)+' -g '+str(injection_gap)+'\n')


with open('execution_command.txt', 'r') as COMMAND:
	for i, input_command in enumerate(COMMAND):
		# print out the commandline and remove the '\n'
		#print(input_command.rstrip())
		
		# extract the numbers of the executed command and appendix it to the job name
		input_param = re.findall(r'\d+', input_command.rstrip());	
		#print("%s %s %s %s" % (input_param[0], input_param[1], input_param[2], input_param[3]))

		# execute the qsub in command mode by adding '-b y' flag
		os.system('qsub -q bme.q -cwd -N CYANG_'+input_param[0]+'_'+input_param[1]+'_'+input_param[2]+'_'+input_param[3]+' -j y -b y '+input_command.rstrip())
