
# Rotate Matrix: Given an image represented 
# by an NxN matrix, where each pixel in the 
# image is 4 bytes, write a method to rotate 
# the image by 90 degrees. Can you do this in place?


def rotate(matrix):
    for i in range(len(matrix) // 2):
        _rotate_layer(matrix, i)

def _rotate_layer(m, layer):
    n = len(m)
    for i in range(layer, n-layer-1):
        aux = m[layer][i]
        
        # move from top to right border
        m[i][n-layer-1], aux = aux, m[i][n-layer-1]
        
        # move from right to bottom border
        m[n-layer-1][n-i-1], aux = aux, m[n-layer-1][n-i-1]
        
        # move from bottom to left border
        m[n-i-1][layer], aux = aux, m[n-i-1][layer]
        
        # update top
        m[layer][i] = aux


if __name__ == "__main__":
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(m)
    rotate(m)
    print(m)


