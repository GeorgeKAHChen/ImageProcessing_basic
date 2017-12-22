# ImageProcessing_in_USTB (Finished, version 2.0)
I finished all this program finally.<br/>
A long time journey, I used about 14 week to finished all this program.<br/>
However, this program still have some little bug which I am not confident. As I will use this program to finish some research, I think I will find them and recovery.<br/>
## Surrounding
`Warning: As I did nothing of compatibility， DO Not using this program on Windows system. You can use this program on UNIX 
You should install some package before using it, and I will give you the installation function with pip3`
<br/>
STEP 1: Install Python3<br/>
For Linux Ubuntu and Debain system<br/>
```
    sudo apt upgrade
    sudo apt update
    sudo apt install python3 python3-pip ipython3
```
For Fedora and Red-hat system<br/>
```
    sudo yum upgrade
    sudo yum update
    sudo yum install python3 python3-pip ipython3
```
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
https://docs.opencv.org/trunk/d7/d9f/tutorial_linux_install.html<br/>
For Mac OS<br/>
https://www.pyimagesearch.com/2016/12/19/install-opencv-3-on-macos-with-homebrew-the-easy-way/<br/>

STEP 3: Download the program<br/>
You can download this program with git, and I will show you how to use it.<br/>
```
    git clone https://github.com/KazukiAmakawa/ImageProcessing_in_USTB/
```

## Usage
This program will read all jpg, png and bmp figures in the program folders without /Output. If you want to using a figure, you need just put it in the root folders, or build a folder which have name you like and not /Output. <br/>
You can begin all the program with the command <br/>
```
    python3 Main.py
```
First in first, you need to choose the figure you want to use. Print the code of figure and press ENTER.<br/>
![image](http://stlaplace.com/img/Git/1.png)
Here, you can choose you need using this figure for a long time or just one case. If you input n or N, after algorithm, you need choose a new figure, else, you can use this figure for a long time.<br/>
![image](http://stlaplace.com/img/Git/2.png)
After that, you can choose the algorithm you need, or input 0 to exit and -1 to choose another figure.<br/>
![image](http://stlaplace.com/img/Git/3.png)
If you used any algorithm, the system will ask you if you need save this figure or not, all the figure will be saved in folder /Output (Thats why all figure in /Output will not be read).<br/>
![image](http://stlaplace.com/img/Git/4.png)
The system will also ask you if you need using this figure or not. If you input y or Y, you can use other tools working on the figure after algorithm.<br/>

## Functions
1)  Gray level linear transformation.<br/>
Some Basic Functions, include:<br/>
 (1)  Negative operation<br/>
(2)  Thresholding<br/>
(3)  Gray level linear transformation.<br/>
(4)  Logarithmic Transformation<br/>
(5)  Exponential transformation<br/>
(6)  Linear Treatment<br/>
2)  Gamma(power) transformation.<br/>
3)  Contrast-Stretching Transformations.<br/>
4)  Histogram Equalization<br/>
5)  Maximum entropy for thresholding<br/>
6)  Get Gradient of figure<br/>
7)  Thresholding with Gradient<br/>
8)  Statistic the figure<br/>
This function have some bug, which I am not confident.<br/>
9)  Auto algorithm!<br/>
Do not using this program, this is the function I try to build a Auto Monte Carlo algorithm, It's failed.<br/>
10) Monte Carlo Average Constrast<br/>
Do not using this program, this is the function I try to build a Auto Monte Carlo algorithm, It's failed.<br/>
11) Convolution<br/>
You can choose the kernel of convolution, you can also add some kernel in /Convolution.py<br/>
12) Histogram Equalization with Monte Carlo<br/>
Do not using this program, this is the function I try to build a Auto Monte Carlo algorithm, It's failed.<br/>
13) Gradient transformation Algorithm (GTA!)<br/>
Do not using this program, this is the function I try to build a Auto Monte Carlo algorithm, It's failed.<br/>
14) 2 Side Gradient Treasholding with DFS<br/>
Do not using this program, this is the function I try to build a Auto Monte Carlo algorithm, It's failed.<br/>
15) Median Filtering<br/>
16) Sobel 3 * 3 cross edge detection operator<br/>
17) Roberts cross edge detection operator<br/>
18) Gradient Treasholding with Convolution<br/>
19) The smallest variance smoothing filter<br/>
20) Canny edge detector<br/>
21) Random Walk Algorithm<br/>
Do not using this program. It's failed.<br/>
Here I will give you the Random Walk Image Edge Algorithm(RWIEA) which is a part of CRIEA program.<br/>
https://github.com/KazukiAmakawa/CRIEA<br/>
22) Unsharp masking<br/>
23) Block Algorithm<br/>
Do not using this program. It's failed. You can get the block algorithm with the Toboggan Algorithm below.<br/>
24) Toboggan Algorithm<br/>
25) Linear PDE method<br/>
26) Non-linear PDE method<br/>
27) Bilateral Filter Smoothing<br/>
28) Least square estimation<br/>
29) Iterative solution<br/>
30) Fourier Transform<br/>
31) Histogram Fourier Transform<br/>
32) Entropy Analysis<br/>
33) Wavelet Algorithm<br/>
For last test.<br/>
34) Gauss Random<br/>
For last test.<br/>
35) ADMM Algorithm<br/>
For last test.<br/>

## Others
The main program which I am working on is based on the function 21) Random Walk Algorithm. It is called as criea(CNN and Random walk Image Edge Algorithm). Here is the main page of this program (Chinese):<br/>
http://www.criea.info/index.php/%E9%A6%96%E9%A1%B5<br/>
And the code of this program is over here:<br/>
https://github.com/KazukiAmakawa/CRIEA<br/>

## Special Thanks
My teacher Zhengwei Sheng. And my friends include Tao Ren, Yurou Chen, Kun Liu, Ruijie Lv.<br/>
If you have some problem, please send the E-mail to KazukiAmakawa@gmail.com, Thanks!
<br/>
<br/>
<br/>
<br/>
Kazuki Amakawa<br/>
22 Dec. 2017<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
## History version
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
