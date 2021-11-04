import numpy
from numpy import linalg as LA
import cv2
import sys


##########  TRAINING OF IMAGES ##########


x=[]

# Reading images in matrix x using opencv

for i in range (1,31):

    for j in range (1,10):
        
        a = "att_faces/s" + str(i)+"/" + str(j) + ".pgm";

        x.append(numpy.reshape(cv2.imread(a, 0), -1).astype(numpy.float64)) # To store the images in vector form such that each row of x represents an image of dimensions:(1 x HW)
                                                                            # (where H is the no of pixels in height(92) and W the no of pixels in width(112))


# Arranging the matrix x such that each column of matrix x represents an image of dimensions:(HW x 1). Thus total matrix size of x is (10304 x 300)

x = numpy.asarray(x)
x = x.transpose()

# Finding the average face vector or mean (psy) of the image vectors arranged in the columns

psy = []
for i in range(len(x)):
    d=0
    for j in range(len(x[0])):
        d = d + x[i][j]
    psy.append(d)
    psy[i] = psy[i]/271.0

# Subtracting the mean from each face vector and storing it in phi

phi = x
for i in range(len(x)):
    for j in range(len(x[0])):
        phi[i][j] = x[i][j] - psy[i]

# Finding the eigenvectors and eigenvalues of the covariance matrix

covar = numpy.matmul(phi.transpose(),phi)

eigenValues, eigenVectors = numpy.linalg.eigh(covar)

eigenVectorsNew = numpy.matmul(phi, eigenVectors)
eigenVectorsNew = eigenVectorsNew/numpy.linalg.norm(eigenVectorsNew, axis=0)

# Selecting k best eigenvectors corresponding to the k best eigenvalues (In this k = len(eigenValues)/2)

U = eigenVectorsNew[:,(len(eigenValues)/2):]

# Calculating weights corresponding to the k eigenvectors

weights = numpy.matmul(U.transpose(), phi)

# Asking for option on how to proceed

print "What would you like to implement?"
print "1) Face Identification"
print "2) Face Detection"
ans = input("Input the index of the option to be implemented: ")

if ans == 1:

    ##########  FACE IDENTIFICATION ##########


    # Asking for a different image of one of the people whose images have been trained above
    
    f = raw_input("Name of the folder from the identification directory: ") # Input one of the folders from s1, s2, s3, s4
    a = "Unknown/Identification/" + str(f)+"/10.pgm";

    k = numpy.reshape(cv2.imread(a, 0), -1).astype(numpy.float64);

    # Subtracting the earlier calculated mean from the new face vector and storing it in phi
    
    phiN = k
    for i in range(len(phiN)):
        phiN[i] = phiN[i] - psy[i]

    # Calculating the weights corresponding to the new face vector

    weightsNew = numpy.matmul(U.transpose(), phiN)

    # Calculating the minimum weight difference by normalizing
    
    n = weights

    for i in range(len(weights)):
        for j in range(len(weights[0])):
            n[i][j] = n[i][j] - weightsNew[i]

    norm = []

    for i in range(len(weights[0])):
        t=0;
        for j in range(len(weights)):
            t = t + (n[j][i])**2
        t = t**(0.5)    
        norm.append(t)
    
    r = norm.index(min(norm))
    TH = 4000
    # Giving the output of the identified person corresponding to the input image 
    if min(norm)<=TH:
        
        if (r>=0 and r<=8):
            print ("The given testing image belongs to person - " + str(1))
        elif (r>=9 and r<=17):
            print ("The given testing image belongs to person - " + str(2))
        elif (r>18 and r<=26):
            print ("The given testing image belongs to person - " + str(3))
        elif (r>=27 and r<=35):
            print ("The given testing image belongs to person - " + str(4))
    else:
        print ("The image for identification does not correspond to any person used for training data")
        
elif ans == 2:
        

    ##########  FACE RECOGNITION ##########


    print "Select the face recognition check for one of the following: "
    print "a) Some unknown image"
    print "b) Person"
    ans1 = raw_input("Input the index corresponding to the option to be computed: ")
    
    if ans1 == "b":
        
        f = raw_input("Name of the folder from the image directory: ") # Input one of the folders from s31, s32, ...... s40
        i = raw_input("Name of the image from the selected folder in the image directory:" ) # Input any one of the image from 1,2, ..... 10 
        a = "Unknown/Detection/" + str(f)+"/" + str(i) + ".pgm";

        # Storing the value of the new image of dimensions (HW x 1) in phiN1

        k = numpy.reshape(cv2.imread(a, 0), -1).astype(numpy.float64);
        phiN1 = k

        # Subtracting mean from the stored matrix for new image
        
        for i in range(len(phiN1)):
            phiN1[i] = phiN1[i] - psy[i]

        # Computing weigths for the new image
        
        weightsNew1 = numpy.matmul(U.transpose(), phiN1)
       
        # Computing a new matrix for the input test image by multiplyingit with its weights
        
        phiN2 = numpy.matmul(U,weightsNew1)

        # Cheking the presence of a face by normalizing and comparing it with a threshold
        
        n1 = phiN1

        for i in range(len(phiN1)):
            n1[i] = n1[i] - phiN2[i]

        t=0;

        for i in range(len(n1)):
            t = t + (n1[i])**2
        norm1 = t**(0.5)

        TH = 4000
        if norm1 <= TH:
            print ("The input image has a face of a person, since the norm: " + str(norm1) + " is less than the set threshold: " + str(TH)) 

    elif ans1 == "a":
        
        h = raw_input("Name of the image: " ) # For unknown image, use an image of size 92 x 112 pixels. Here you can select the flower picture which I have resized to the required pixel size.
                                              # For using the flower picture, enter flower when promted
                                              
        a = "Unknown/Detection/" + str(h) + ".jpg";

        k = numpy.reshape(cv2.imread(a, 0), -1).astype(numpy.float64);
        phiN1 = k
        
        # Subtracting mean from the stored matrix for new image
        
        for i in range(len(phiN1)):
            phiN1[i] = phiN1[i] - psy[i]

        # Computing weigths for the new image
        
        weightsNew1 = numpy.matmul(U.transpose(), phiN1)
       
        # Computing a new matrix for the input test image by multiplyingit with its weights
        
        phiN2 = numpy.matmul(U,weightsNew1)

        # Cheking the presence of a face by normalizing and comparing it with a given threshold
        
        n1 = phiN1

        for i in range(len(phiN1)):
            n1[i] = n1[i] - phiN2[i]

        t=0;

        for i in range(len(n1)):
            t = t + (n1[i])**2
        norm1 = t**(0.5)    
        
        TH = 4000
        if norm1 > 4000:
            print ("The input image does not have the face of a person, since the norm: " + str(norm1) + " is greater than the set threshold: " + str(TH))
