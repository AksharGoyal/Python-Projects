# import the module for navigating through the desktop
import os

def main():
    path = input("Input the destination folder path: ") # folder containing the files
    path = path + "\\"
    extension = input("Enter the extension name (.jpg, .py, etc.): ")
    
    try:
        i = 0
        for filename in os.listdir(path):               # get the list of files
            image_name = "img" + str(i) + extension     # setting up the new filename
            old_source = path + filename                # getting the old filename
            new_image_name = path + image_name          # new filename has now a path
            os.rename(old_source, new_image_name)       # new filename has been setup
            print(f"Filename is now: {image_name}.")
            i-= -1                                      # fancy way of incrementing a variable
    except:
        print("Sorry, folder doesn't exist! Exiting!")  # if the folder doesn't exist
        exit()
        
if __name__ == '__main__':
    main()