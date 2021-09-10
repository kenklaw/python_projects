import Jetson.GPIO as GPIO
import time
import shutil
import os
import cv2

# Thermal modes duty_cycles
# Represents how long a clock signal is on, which controls which thermal mode is active
WHITE = 5
GREEN = 7.5
RED = 10

# Signals for the thermal camera
START = 10
STOP = 5

# For hardware, mostly voltages

def run(running_ops):

    GPIO.cleanup()    

    GPIO.setwarnings(False)

    # Prime GPIO to read input.
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(33, GPIO.OUT)
    GPIO.setup(32, GPIO.OUT) 

    # Instantiate PWM variables.
    color_pwm = GPIO.PWM(32, 50)
    record_pwm = GPIO.PWM(33, 50)

    # Initiate PWM
    color_pwm.start(5)
    record_pwm.start(5)

    # Get mode
    if running_ops.is_thermal_white():
        color_pwm.ChangeDutyCycle(WHITE)

    elif running_ops.is_thermal_green():
        color_pwm.ChangeDutyCycle(GREEN)

    elif running_ops.is_thermal_red():
        color_pwm.ChangeDutyCycle(RED)

    # Start Recording
    record_pwm.ChangeDutyCycle(START)

    # Delay
    time.sleep(3)

    # Stop Recording
    record_pwm.ChangeDutyCycle(STOP)

    # Must have 10 second delay because device is hidden when recording begins
    # Cannot access the device sd card if recording.
    time.sleep(5)

    source_dir = ("/media/spring2021/6FB0-5C39")
    #source_dir = ("/media/usb")
   
    index = 0

    folderArr = []

    numframes = 1
    counter = 0

    for folder in os.listdir(source_dir):

        dir = os.path.join(source_dir, folder)
        if counter >= numframes:
            break
        folderArr.append(folder)

        if os.path.isdir(dir):
            folderStr = "Folder {}".format(index)
            #print(folderStr)
            #print(dir)
            index += 1
            latest_video = index - 1 

    #was 3

    folder_arr_size = len(folderArr) - 3
        
    new_directory = "/media/spring2021/6FB0-5C39/{}".format(folderArr[folder_arr_size])

    #new_directory = "/media/usb/{}".format(folderArr[folder_arr_size])
   
    current_dir = os.path.dirname(os.path.realpath(__file__))
    
    target_dir = "/home/spring2021/Desktop/Capstone/fire_scout_system/drone_station/thermal_vid"

    #list all files from sourse_dir to be accessed
    file_names = os.listdir(new_directory)
    #print(file_names)

    #look for files in the dir with .mov format move those files to thermal folder    
    for file_name in file_names:
        if file_name.endswith(".mov"):
            shutil.move(os.path.join(new_directory, file_name), target_dir)

    #testing
    print("File has been moved to desktop")

    # Post-data processing; cleanup
    GPIO.cleanup()

    time.sleep(5)



#####################################################################33
#this is where we need to parse the video file to get a jpg
#######################################################################

    img_source_dir = ('/home/spring2021/Desktop/Capstone/fire_scout_system/drone_station/thermal_vid')

    img_index = 0

    img_folderArr = []

    img_numframes = 1
    img_counter = 0

    for folder in os.listdir(img_source_dir):

        dir = os.path.join(img_source_dir, folder)
        if img_counter >= img_numframes:
            break
        img_folderArr.append(folder)

        if os.path.isdir(dir):
            folderStr = "Folder {}".format(img_index)
            img_index += 1
    

    img_arr_size = len(img_folderArr) - 1

    #img_output_file = '/home/spring2021/Desktop/Capstone_Prototype/fire_scout_system/drone_station/test_images/ThermalFrame_%s.jpg'

    #timestr = time.strftime("%Y-%m-%d-%H-%M-%S")
    img_output_file = ('/home/spring2021/Desktop/Capstone/fire_scout_system/drone_station/test_images/Thermal/thermal_0.jpg')

    img_frames = 1
    img_counter = 0

    # Read the video from specified path 
    cap = cv2.VideoCapture("/home/spring2021/Desktop/Capstone/fire_scout_system/drone_station/thermal_vid/{}".format(img_folderArr[img_arr_size]))
    img_success, img_image = cap.read()

    print('file has been moved to thermalimages')

    while img_success:
        cv2.imwrite((img_output_file), img_image)
        img_success, img_image = cap.read()
        
        img_counter += 1

        if(img_counter >= img_frames):
            break

    vid_directory = ("/home/spring2021/Desktop/Capstone/fire_scout_system/drone_station/thermal_vid/")

    #list all files from sourse_dir to be accessed
    vid_file_names = os.listdir(vid_directory)
   

    #look for files in the dir with .mov format move those files to thermal folder    
    for video in vid_file_names:
        if video.endswith(".mov"):
            os.remove(os.path.join(vid_directory, video))

            print("file has been deleted")

    running_ops.thermal_off()