## GMMImgSegmentation
A tiny project using GMM to segment imgs.
This is done by:
1. First convert the image from RGB color space into RG color space
2. Then assume the pixels to be points from K different multiple dimentional Gaussians
3. Apply EM methods to obtain the fitted data points
### Example picture
![example](TestImage.jpg "Example picture") 
### K=3 Case
#### Picture converted into rg space
![k=3](K=3/poi.jpg)
#### Greyscale pictures reflect how likely(the possibility)that a pixel will lay in one Gaussian component.
+ White: More likely 
+ Black: Less likely

![K=3](K=3/Greyscale0.png) ![K=3](K=3/Greyscale1.png) ![K=3](K=3/Greyscale2.png)
#### Color distribution and Gaussians fitted
![K=3](K=3/class.png)

### K=4 Case
#### Greyscale pictures reflect how likely(the possibility)that a pixel will lay in one Gaussian component.
![K=4](K=4/Greyscale0.png) ![K=4](K=4/Greyscale1.png) ![K=4](K=4/Greyscale2.png) ![K=4](K=4/Greyscale3.png)
#### Color distribution and Gaussians fitted
![K=4](K=4/class.png)

### K=5 Case(notice the over-fit)
#### Greyscale pictures reflect how likely(the possibility)that a pixel will lay in one Gaussian component.
![K=5](K=5/Greyscale0.png) ![K=5](K=5/Greyscale1.png) ![K=5](K=5/Greyscale2.png) ![K=5](K=5/Greyscale3.png) ![K=5](K=5/Greyscale4.png)
#### Color distribution and Gaussians fitted
+Notice the tiny green located in blue area
![K=5](K=5/class.png)
