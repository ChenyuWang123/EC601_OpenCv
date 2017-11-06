# 1.
## Truncate

Turns the gray image and the value over 127 to threshold, decreases the contrast of the image.

## Binary

Turns the gray image and the value over 127 to 255（max）, the other values are cleared, the contrast of light and shade increases.

## Band

Frstly, do the same thing as Binary. 

Then compared with thershold2(123), the values over 125 are cleared and the others are changed to the max.

Use the command 'and' to deal with the two results. 

Finally, we get a band, the result is inverted from the orignial one but lose some information.

## Semi

Automaticaly, calculate the threshold depends on the image of light and shade. 

Values over the threshold are turned to max, the others are cleared. 

The comparation hs been increased without large anount of data lose.

## Adaptive

It divids the image into different parts to calculate the threshold. 

Values over the threshold are changed to max, the others are cleared.

The original information is saved well and the comparation has been increased. 

# 2.

Thershold is unitary and lose lots of information about vector.

# 3.

It works well with images with varying illumination
