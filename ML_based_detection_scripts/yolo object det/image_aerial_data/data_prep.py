
import cv2 
   
def FrameCapture(path): 
      
     
    vidObj = cv2.VideoCapture(path) 
  
    # Used as counter variable 
    count = 0
  
    # checks whether frames were extracted 
    success = 1
  
    while success: 
  
        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read()
        count += 1

        if count%40==0:
  
        # Saves the frames with frame-count 
            cv2.imwrite("frame%d.jpg" % count, image) 
  
        
        if count>10000:
            success = 0
# Driver Code 
if __name__ == '__main__': 
  
    # Calling the function 
    FrameCapture("arieal_vid.mp4") 
