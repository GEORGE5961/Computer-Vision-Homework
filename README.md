# Computer-Vision-Homework

## Asignement 1

Write your own implementations of the morphological **dilation and erosion operations**. Your programs should input a binary image (as a matrix) and a structuring element (also as a matrix), and produce a binary image (another matrix) as the result of the operation.

**You can generate the structuring element as a binary image with an arbitrary shape or use a predefined structure (such as a square or a disc) with a user-defined parameter for its size (such as the length of the side of the square or the diameter of the disc).** Given the structuring element, your code should implement the dilation and erosion operations using the definitions given in the course slides. Note that the structuring element is created outside and given as an input to the dilation/erosion codes so that these codes can work with any kind of structuring element. You are free to use any programming language. 

### My demo

It now only works on binary images which has only two values: 0 and 255.

The foreground color is white(255) and the background color is black(0). In general, Erosion decreases the white area and dilation expands the white area. The kernel I used is the simplest square.

The demo is shown in the following images. The effect is quite obvious. 

#### Origin image

<img src="https://github.com/GEORGE5961/Computer-Vision-Homework/blob/master/hw1/origin.png?raw=true" width="30%" />

#### Eroded image

<img src="https://github.com/GEORGE5961/Computer-Vision-Homework/blob/master/hw1/eroded.png?raw=true" width="30%" />

#### Dalited image

<img src="https://github.com/GEORGE5961/Computer-Vision-Homework/blob/master/hw1/dalited.png?raw=true" width="30%" />


