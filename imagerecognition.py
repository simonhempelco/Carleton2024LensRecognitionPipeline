import numpy as np
import cv2
import hsvtuner
import imagecropper

def get_canny_contour(img_in = cv2.imread('CarletonLiquidLensImages\IMG_1285.jpg'),    negative_in = cv2.imread('CarletonLiquidLensImages\IMG_Negative.jpg')):
    img_blur = cv2.GaussianBlur(img_in, (251,251), 0) 
    negative_blur = cv2.GaussianBlur(negative_in, (251,251), 0) 
    screw = cv2.bitwise_and(negative_blur,img_blur)
    lens = cv2.bitwise_xor(img_blur,screw)

    small_lens = cv2.resize(lens, (0,0), fx = 0.125, fy = 0.125)
    medium_lens = cv2.resize(lens, (0,0), fx = 0.25, fy = 0.25)

    threshold = hsvtuner.tune_hsv(small_lens)
    lower = threshold[0]
    upper = threshold[1]

    mask = cv2.inRange(medium_lens,lower,upper)


    img_blur = cv2.GaussianBlur(mask, (3,3), 0) 
    edges = cv2.Canny(img_blur, threshold1=100, threshold2=200) # Canny Edge Detection



    # Display Canny Edge Detection Image

    cv2.imshow("Image Stack", edges)
    cv2.waitKey(0)
 
    cv2.destroyAllWindows()
    return edges
if __name__ == '__main__':
    canny_edges = get_canny_contour()
    print("hi")
    cv2.imshow("afd", canny_edges)
    draw_line_widget = imagecropper.DrawLineWidget(canny_edges)
    should_continue = True
    while should_continue:
        cv2.imshow('image', draw_line_widget.show_image())
        key = cv2.waitKey(1)

        # Close program with keyboard 'q'
        if key == ord('q'):
            cv2.destroyAllWindows()
            should_continue = False
            