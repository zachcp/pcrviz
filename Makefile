# note pymol must be available on the command line
# also uses the following python packages: click
# also uses the following programs: ffmpeg

build/pcr.pml:
	mkdir -p build
	cp *.pdb build
	python pcr_commands.py > build/pcr.pml
	

build/frame_matrix000.png: build/pcr.pml
	cd build; pymol -qc pcr.pml

build/PCR.mp4: build/frame_matrix000.png
	 ffmpeg -r 25 -i build/frame_matrix%03d.png PCR.mp4 
	 
clean:
	rm -rf build/

all: build/pcr.pml \
		 build/frame_matrix000.png \
		 build/PCR.mp4