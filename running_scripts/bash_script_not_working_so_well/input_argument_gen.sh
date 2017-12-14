
for pattern in `echo 1 2 3 4`; do
	for pattern_size in `echo 4 8 16`; do
		for packet in `echo 1 2 4 8 16`; do
			for gap in `echo 0 1 2 4 8`; do
				echo ./ClusterFPGASim.exe -i $pattern -s $pattern_size -p $packet -g $gap >> input_argument.txt;
			done
		done
	done
done
