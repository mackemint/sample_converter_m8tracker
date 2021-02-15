from pydub import AudioSegment
import sys, os

name = ""
file_count = 0
for root, dirs, files in os.walk(sys.argv[1], topdown=False):
	for file in files:
		file_name = os.path.join(root, file)
		try:
			sound = AudioSegment.from_file(file_name).set_frame_rate(44100).set_sample_width(2)
		except :
			print(f"File is not convertable: {file_name}")
			continue
		print(f"Converting {file_name} in 16bit, 44,1 kHz")
		name = file_name.strip("-")[file_name.rfind("/")+1:-4].replace("-", "_").replace(" ", "_").replace("__", "_")+".wav"
		location = "."+root[root.find("/", root.find("/") + 1):root.rfind("/")]
		file_path = os.path.join(location, name)
		if not os.path.isdir(location):
			print(f"creating folder {location}")
			os.mkdir(location)
		if os.path.isfile(file_path):
			name = name[:-4]+"(1)"+name[-4:]
			file_path = os.path.join(location, name)
		sound.export(file_path, format="wav")
		print(f"Created {file_path}")
		file_count += 1

if file_count > 1:
	print(f"Slicing complete, happy tracking!")
elif file_count < 1:
	print(f"No files converted")
else:
	print(f"Slicing complete, enjoy your sample {name}")