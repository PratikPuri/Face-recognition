<h1>Real Time Face Recognition System</h1>

<h3>Introduction</h3> 
Real time face recognition using dataset from AT&T database image training has been implemented in this assignment. Real time face recognition has several applications, some of them include use in phone cameras, in surveillance systems, for law enforcement purposes and many more. To implement real time face recognition, the algorithm based on the paper by Matthew A. Turk and Alex P. Pentland has been implemented in this assignment. The steps used in implementing the algorithm are as follows:<br><br>
<ol>
<li><b>Calculating Eigenfaces for Recognition –</b> To calculate the Eigenfaces, the following steps were used:<br>
    <ol>
    <li>The face vectors were stored in a matrix such that each column of the matrix represents a face vector. The dimensions of the matrix for 30 of the AT&T database images         is 10304 x 300.<br><br>
    <p align="center"><img src="https://github.com/PratikPuri/Face-Recognition/blob/feature-readme/images/image1.jpg"></p></li>
    <li>The mean of the face vectors was subtracted from individual face vectors.
    <p align="center"><img src="https://github.com/PratikPuri/Face-Recognition/blob/feature-readme/images/image2.jpg"><br>Mean</p>
    <p align="center"><img src="https://github.com/PratikPuri/Face-Recognition/blob/feature-readme/images/image3.jpg"><br>Mean subtracted from face</p></li>
    <li>The covariance matrix is given by:<br>
    <p align="center"><img src="https://github.com/PratikPuri/Face-Recognition/blob/feature-readme/images/image4.jpg"><br>
    <img src="https://github.com/PratikPuri/Face-Recognition/blob/feature-readme/images/image5.jpg"></p>
    Instead of computing AAT, ATA was computed to reduce the processing time. Since, AAT is a [N2xN2], while ATA is a [M x M] matrix. Their eigen values remain same and their eigenvectors are related by
    Thus, the computation time for calculating the eigenvectors and eigenvalue was reduced.</li>
    <li>K eigenvectors corresponding to the K best eigenvalues were selected. K = M/2 eigenvectors were selected for this case corresponding to the K best eigenvalues, where M = total number of images used in training. The k eigenvector matrix was then normalized.
    <p align="center"><img src="https://github.com/PratikPuri/Face-Recognition/blob/feature-readme/images/image6.jpg"></p></li>
    <li>Once the eigenvectors were selected their weights were calculated by projecting the (Face vectors - mean) vectors onto the eigenvector plane.
    <p align="center"><img src="https://github.com/PratikPuri/Face-Recognition/blob/feature-readme/images/image7.jpg"><br>
    Where w vector corresponds to the weight vector</p></li>
    </ol>
</li>
<li><b>Face identification –</b> The following steps were used for face identification:<br>
    <ol>
    <li>Similar steps were followed for a new image. This new image is the image of a person whose faces have been used in the training of the images.</li>
    <li>The weight vector for a single new image was calculated and compared with the existing weights of the trained images. The weight vector of the person closest to the weight vector of the new image was declared as the identified person from the image.</li>
    <li>To find the closest weight vector, the weight vectors from pre-trained data and new image were subtracted and then normalized. The difference was then normalized. The person whose weight vector had the minimum value corresponding to the normalized output was declared as the person in the image.
    <p align="center"><img src="https://github.com/PratikPuri/Face-Recognition/blob/feature-readme/images/image8.jpg"></p></li>
    <li>If er was found to be more than the threshold value, that means that the image given for identification does not belong to any of the images used for training.</li>
    </ol>
</li>
<li><b>Face recognition –</b> The following steps were used for face recognition -
    <ol>
    <li>Similar steps as above were followed and new weight vector was calculated for the unknown image.</li>
    <li>The weight vector was then multiplied with the reduced eigenvector of the unknown image and the new (Face vectors - mean) vector was found, which was then compared with the original (Face vectors - mean) vector without the data loss. (Lets say (Face vectors - mean) vector = phi)
    <p align="center"><img src="https://github.com/PratikPuri/Face-Recognition/blob/feature-readme/images/image9.jpg"></p></li>
    <li>They were compared by finding the normalized output of the difference between the original and the new phi.
    <p align="center"><img src="https://github.com/PratikPuri/Face-Recognition/blob/feature-readme/images/image10.jpg"></p></li>
    <li>If ed was found to be less than a threshold value, (4000 in this case), a face was present in the unknown image and face recognition was successful or else no face was present in the unknown image and face recognition was unsuccessful.
    <p align="center"><img src="https://github.com/PratikPuri/Face-Recognition/blob/feature-readme/images/image11.jpg"></p></li>
    </ol>
</li>
</ol>
<h3>References:</h3>
<ol>
<li>M. A. Turk and A. P. Pentland, "Face recognition using eigenfaces," Proceedings. 1991 IEEE Computer Society Conference on Computer Vision and Pattern Recognition, Maui, HI, USA, 1991, pp. 586-591. doi: 10.1109/CVPR.1991.139758 keywords: {computerised pattern recognition;eigenvalues and eigenfunctions;unsupervised learning;eigenfaces;human faces;face recognition system;two-dimensional recognition;feature space;face space;face images;eigenvectors;Face recognition;Face detection;Humans;Character recognition;Computer vision;Head;Eyes;Nose;Computational modeling;Image recognition}, URL: http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=139758&isnumber=3774</li>
<li>Data download link: https://www.cl.cam.ac.uk/research/dtg/attarchive/facedatabase.html</li>
<li>https://www.learnopencv.com/eigenface-using-opencv-c-python/</li>
<li>http://www.vision.jhu.edu/teaching/vision08/Handouts/case_study_pca1.pdf</li>
<li>http://www.cbsally.com/black-and-white-photography.html</li>
</ol>
