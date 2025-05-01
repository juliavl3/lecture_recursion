import matplotlib.pyplot as plt
import numpy as np

def flood_fill(img_array,x_pos, y_pos ):
    #out of range
    if x_pos < 0 or y_pos < 0 or x_pos >= img_array.shape[0] or y_pos >= img_array.shape[1]:
        return img_array
    #skips the pixels that are already filled and skips the pixels that cannot be filled
    if img_array[x_pos, y_pos] == 0 or img_array[x_pos, y_pos] == 2:
        return img_array

    img_array[x_pos,y_pos] = 2

    img_array = flood_fill(img_array, x_pos + 1, y_pos)
    img_array = flood_fill(img_array, x_pos - 1, y_pos)
    img_array = flood_fill(img_array, x_pos, y_pos + 1)
    img_array = flood_fill(img_array, x_pos, y_pos - 1)

    return  img_array

def main():
    #img = plt.imread("files/img0.png")[:, :, 0]
    #img = plt.imread("files/img1.png")[:, :, 0]
    img = plt.imread("files/img2.png")[:, :, 0]

    img = flood_fill(img, 0, 0)

    plt.imshow(img, cmap="gray")
    plt.show(block=False)
    plt.pause(5)
    plt.clf()


if __name__ == "__main__":
    main()
