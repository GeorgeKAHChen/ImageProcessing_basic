# ImageProcessing_in_USTB (Finished)
I finished all this program finally.<br/>
A long time journey, I used about 14 week to finished all this program.<br/>
However, this program still have some little bug which I am not confident. As I will use this program to finish some research, I think I will find them and recovery.<br/>
## Surround
`Warning: As I did nothing of compatibility， DO Not using this program on Windows system. You can use this program on UNIX 
You should install some package before using it, and I will give you the installation function with pip3`<br/>
STEP 1: Install Python3<br/>
For Linux Ubuntu and Debain system<br/>
```
    sudo apt upgrade
    sudo apt update
    sudo apt install python3 python3-pip ipython3
```
<br/>
For Fedora and Red-hat system<br/>
```
    sudo yum upgrade
    sudo yum update
    sudo yum install python3 python3-pip ipython3
```
<br/>
For Mac OS<br/>
You should insttall brew first<br/>
```
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
And install python3<br/>
```
    brew update
    brew upgrade
    brew install python3 python3-pip ipython3
```

STEP 2: Install python package<br/>
```
    pip3 install Pillow
    pip3 install matplotlib
    pip3 install PyWavelets
```
You should also install opev-cv, however, as the installation of open-cv is so different, I cannot give you some confident method to install it. Here I will give you a reference of open-cv installation.<br/>
For Linux<br/>
```
    https://docs.opencv.org/trunk/d7/d9f/tutorial_linux_install.html
```
For Mac OS<br/>
```
    https://www.pyimagesearch.com/2016/12/19/install-opencv-3-on-macos-with-homebrew-the-easy-way/
```

STEP 3:

This program will read all jpg, png and bmp figures in the program folders without /Output.



<h2>History version </h2>
This program is the code I had written or I will write during my Image Processing course in USTB.<br/>
As usual I will still use Python, which is the most beautiful program language (just a joke).<br/>
And if you are my friend or student in my school, you can also use these code during this class.<br/>
By the way, my class is teaching with both Chinese and English. So don't care about why I often using English during the program<br/>
<br/>
<br/>
Kazuki Amakawa<br/>
<br/>
<br/>
By the way, you may need to install these packages<br/>
pip3 install Pillow<br/>
pip3 install matplotlib<br/>
You may also need install opencv if you want to run these code normally. As the installing of opencv in different system are different, I cannot tell you all the method you need. However, if you are macos, you can install it with the method below<br/>
https://www.pyimagesearch.com/2016/12/19/install-opencv-3-on-macos-with-homebrew-the-easy-way/<br/>
<br/>
And, it is confident that these can work without bug in the MacOS or Linux(or all Unix). Although it is can be compiled in Windows, I still not confident if they have any bug in Windows System, espacelly Windows10 (or Bug10)
<br/>
<br/>
WARNING:
Althrough homeworks can work in the Windows System, The main program with paper <b>CANNOT</b> working even compiling on Windows System!!<br/>
<br/><br/>
<br/><h2>Ver 1.00</h2><br/>
<b>New Functions:</b><br/>
1  Gray level linear transformation.<br/>
2  Gamma(power) transformation.<br/>
3  Contrast-Stretching Transformations.<br/>
4  Histogram Equalization<br/>
5  Maximum entropy for thresholding<br/>
<br/><h2>Ver 1.01</h2><br/>
<b>New Functions:</b><br/>
1  Get Gradient of figure<br/>
2  Thresholding with Gradient<br/>
3  Statistic the figure<br/>
<br/><h2>Ver 1.02</h2><br/>
<b>New Functions:</b><br/>
1  Convolution Function with fft and ifft algorithm<br/>
2  Two Monte Carlo Algorithm for the paritical of figure (Actually not very ideal)<br/>
<br/><h2>Ver 1.03</h2><br/>
<b>New Functions:</b><br/>
1  Add some kernel of convolution<br/>
2  Add another kind of Gradient transformation Algorithm<br/>
3  Add the 2 Side Gradient Treasholding with DFS<br/>
4  Repair some of bugs<br/>
<br/><h2>Ver 1.04</h2><br/>
<b>New Functions:</b><br/>
1  Median Filtering<br/>
2  Sobel 3 * 3 cross edge detection operator<br/>
3  Roberts cross edge detection operator<br/>
4  Gradient Treasholding with Convolution<br/>
5  The smallest variance smoothing filter<br/>
6  Add the norma Convolution method<br/>
<b>Waring:</b> We found a new bug about FFT-IFFT Convolution. Up to now, we still cannot understand why the result of FFT-IFFT Convolution is different from Normal Convolution.<br/>
<br/><h2>Ver 1.05</h2><br/>
<b>New Functions:</b><br/>
1  Some new kernel and algoritm<br/>
2  Compeleted some algorithm and repaired some bug<br/>
3  Added a algorithm called Toboggan Algorithm(Not compeleted, just finished the part of part. Yes, the part of part)<br/>
<br/><h2>Ver 2.00</h2><br/>
Finished all item in my class, especially last test
