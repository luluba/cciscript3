#!/usr/bin/python

'''
Rotate Matrix:
Given an image represented by an N*N matrix,
where each pixel in the image is 4 bytes,
write a method to rotate the image by 90 degree.
Can you do this in place ?
'''
def rotate(matrix, n):
	for layer in range(n/2):
		first = layer
		last  = n - 1- layer
		for i in range(first, last):
			offset = i - first
			# save top
			top = matrix[first][i]
			
			# left -> top
			matrix[first][i] = matrix[last-offset][first]
			# bottom -> left
			matrix[last-offset][first] = matrix[last][last - offset]
			# right -> bottom
			matrix[last][last-offset] = matrix[i][last]
			# top -> right
			matrix[i][last] = top

def main():

if __name__ == "__main__":
