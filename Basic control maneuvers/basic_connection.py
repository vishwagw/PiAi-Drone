# connecting the onboard computer with flightcomputer
# in this program the connection was made via USB port
# using dronekit python lib
# alternatively, pymavlink lib is also can be used

while True:
    ret, frame = cap.read()
    #frame = cv2.flip(frame, -1)
    if ret == True:
        # Filter red color
        # frame = cv2.bilateralFilter(frame,9,75,75)
        frame_hsv =cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask1 = cv2.inRange(frame_hsv, (0, 70, 50), (10, 255, 255))
        mask2 = cv2.inRange(frame_hsv, (170, 70, 50), (180, 255, 255))
        mask = mask1 + mask2
        # Edge detection
        canny_output = cv2.Canny(mask, 10, 10, 20)
        # Find the center
        pixels = np.where(canny_output == 255)
        cX = np.average(pixels[1])
        cY = np.average(pixels[0])

        # cX cY -> NaN
        cv2.circle(canny_output, (int(cX),int(cY)), 3, (255,255,255), thickness=10, lineType=8, shift=0)

        x = cX-320
        y = 240-cY
        Rsquare = math.sqrt(abs(x)**2 + abs(y)**2)/10
        print(math.degrees(math.atan(y/x)))
        degree = math.degrees(math.atan(y/x))
        print(degree, east, north, "3")
        if x <0 and y<0: # 
            degree = 27 - degree
            print(degree,east,north,"3")


        elif (x<0 and y>0): #II.Region
            degree = abs(degree-270)
            print(degree, east, north,'2')

        elif x>0 and y < 0:
            degree = 90-degree
            print(degree,east,north,"4")

        elif x>0 and y >0:
            degree = 90-degree
            print(degree,east,north,"1")

        east = math.sin(math.radians(degree))*Rsquare
        north = math.cos(math.radians(degree))*Rsquare

        #initializing the goto function:
        goto(north, east)

        condition_yaw(degree, False)
        cv2.imshow("contours", canny_output)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
