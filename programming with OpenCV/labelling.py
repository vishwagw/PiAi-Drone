# labelling process:
import cv2
         
# change the image to gray image
img_color = cv2.imread("F:/AIDrone/Real OpenCV/SourceCode/Ch15/15.3/test.jpg", cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY) 
cv2.imshow("result", img_gray )
cv2.waitKey(0)
         
# detect Edge
# detected Edge is white
img_edge = cv2.Canny(img_gray, 50, 150)
cv2.imshow("result", img_edge )
cv2.waitKey(0)
         
# The object of interest should be white, so invert it
img_edge = cv2.bitwise_not(img_edge)
cv2.imshow("result", img_edge )
cv2.waitKey(0) 
         
# Finds contours and reinforces outlines
contours = cv2.findContours(img_edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img_edge, contours[0], -1, (0, 0, 0), 1)
cv2.imshow("result", img_edge )
cv2.waitKey(0) 
         
# Label the white areas
nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(img_edge)

for i in range(nlabels):
    # exclude the background
    if i < 2:
        continue
# Get information about the size, center coordinates, and outer rectangle of the white area
area = stats[i, cv2.CC_STAT_AREA]
center_x = int(centroids[i, 0])
center_y = int(centroids[i, 1]) 
left = stats[i, cv2.CC_STAT_LEFT]
top = stats[i, cv2.CC_STAT_TOP]
width = stats[i, cv2.CC_STAT_WIDTH]
height = stats[i, cv2.CC_STAT_HEIGHT]
 
if area > 50: 
    # Displays a rectangle outside the area
    cv2.rectangle(img_color, (left, top), (left + width, top + height), (0, 0, 255), 1)
    # Draws a circle at the coordinates of the center of an area
    cv2.circle(img_color, (center_x, center_y), 5, (255, 0, 0), 1)
    # Displays the label number.
    cv2.putText(img_color, str(i), (left + 20, top + 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3);


cv2.imshow("result", img_color)
cv2.waitKey(0)

