# sample_converter_m8tracker
Sample converter for M8 tracker

This tool will take a file, folder or subset of folders of audio files and convert them to 16bit, 44,1kHz stereo for compatibility with M8tracker.
When generating files, the script will attempt to categorise the samples using their current structure and put them in the path of the script.
If used to convert a large number of samples in a complex structure of folders, omit the last "/" in the folder structure.

# Requirements
Python3
pydub: pip3 install pydub

# Usage:
Example folder structure - the folder up one level of the path of the script has the following structure:

	Sample Packs/
		Rhythm Lab Neu Jungle Preview/
			Breaks/
				160 Bom Break 4.wav
				166_Wildfire_Break_3.wav
				...
			Synth/
				CS15 Modsynth07 G.wav
				CS15 Reese09 A.wav
				..

Command examples:
Example 1

	python3 ./convert_for_m8.py ../Sample Packs/Rhythm\ Lab\ Neu\ Jungle\ Preview/ <== Note trailing "/" character
	
	Will take all files under the folders of the folder "Rhythm Lab Neu Jungle Preview",
	convert them and put in a folder called "Rhythm Lab Neu Jungle Preview".
	The last slash character indicates for the script to put all files in one folder.
Example 2

	python3 ./convert_for_m8.py ../Sample Packs/Rhythm\ Lab\ Neu\ Jungle\ Preview
	Will take all files under the folders of the folder "Rhythm Lab Neu Jungle Preview",
	convert them and put in a folder called "Rhythm Lab Neu Jungle Preview", preserving sub-folders.
	Omitting the last slash character indicates for the script to preserve sub-folder structure.
