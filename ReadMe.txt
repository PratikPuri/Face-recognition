1) The code for face identification and detection is "Face recognition code.py"
2) The images used for training are taken from AT&T database stored in the folder "att_faces"
3) The images used for identification from the pretrained images, to check face detection for a person and an arbitrary image are stored in the "Unknown" folder.
4) The code consists of two different parts: Identification and Detection:
	a) Identification - Images have been trained from the AT&T database for 30 people with 9 images for each person.
			    The 10th image for four people from the database has been kept in the "Unknown/Identification" folder (To identify a new image, 			    	    whose images have been pretrained)
			    Enter either of s1,s2,s3,s4 for name of the directory
	b) Detection - 
		i) Person - Images of new people who have not been trained are kept in the "Unknown/Detection" folder, to check for face recognition.
			    Enter s31....s40 for folder
			    Enter 1....10 for image
		ii) Unknown image - In this option an unknown image of 92x112 pixels can be given as input. To check that the code does not identify a face 			            when it is not present, the image "flower" can be given as input. 
			    Enter flower for image

The data download link for AT&T database is: https://www.cl.cam.ac.uk/research/dtg/attarchive/facedatabase.html