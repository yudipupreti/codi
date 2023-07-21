import pyautogui
import time

#mouse_locations = [(619, 717), (619, 717), (450, 328) (209, 328), (455, 25), (450, 328)]  # For Followers
mouse_locations = [(619, 717), (619, 717), (209, 352), (455, 25), (450, 358), (329, 435)]  # For Like
#total_iterations = 5

delay_seconds = [0, 0, 0, 0, 1, 0]  # Time delays for each click

#for iteration in range(total_iterations):
while True:
    for location, delay in zip(mouse_locations, delay_seconds):
        pyautogui.moveTo(location[0], location[1])
        pyautogui.click()
        time.sleep(delay)