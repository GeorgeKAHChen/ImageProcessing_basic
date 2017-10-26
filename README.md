# ImageProcessing_in_USTB
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
