#Importing Modules
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from PIL import Image
import os
import numpy
import string
import random


img_path = input("Enter Image Path.. ") #Asking for the User file Input

def convert_and_compress(input_path, output_path, quality):
    with Image.open(input_path) as img:
        img = img.convert("RGB")
        img.save(output_path, "JPEG", quality=quality, optimize=True)
        print("DONE")

def img_compare(A, B , title): #Returns A image with 2images side by side..
    # 1. Load the images
    img1 = Image.open(A)
    img2 = Image.open(f'{title}_{B}.png')

    # --- Padding Logic Added ---
    pad = 20  # Padding size
    bg_color = (255, 255, 255) # White background
    # Calculate new width and height including padding
    # Width = img1 + img2 + 3 gaps (left, middle, right)
    new_width = img1.width + img2.width + (pad * 3)
    # Height = Max height + 2 gaps (top, bottom)
    new_height = max(img1.height, img2.height) + (pad * 2)
    # 3. Create a new image with combined width and maximum height (Updated for padding)
    dst = Image.new('RGB', (new_width, new_height), bg_color)
    # 4. Paste images side by side (Updated with offsets for padding)
    dst.paste(img1, (pad, pad))
    dst.paste(img2, (img1.width + (pad * 2), pad))

    ##Print Statements
    print("-" * 25)
    print("Orignal at the Left | New Image at the Right")
    print("-" * 25)
    print("Combing Images..Please wait!!..")
    print("-"* 10)
    # 5. Save the result
    dst.save(f'{title}_{B}_combined.png')
    print(f'New Combined Image Saved as "{title}_{B}_combined.png"..SUCCESFULLY..in the current Directory')


def save_print(A , B , title):
    plt.imsave(f'{title}_{A}.png' , B , cmap="grey")
    print(f'Image Saved as "{title}_{A}.png"..SUCCESFULLY..in the current Directory')
    print("-" * 30)
    yn = input("Do you want to compare with original? (y/n) ") 
    if yn == "y" or yn == "Y":
        img_compare(img_path, A , title)
    else:
        return

def user_func(req_inp , img, img_path=img_path):
    res = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    if req_inp == 1:
        try:
            user_inp_func_1 = int(input("By..How much you want to Increase brightness??.[5,4,2] "))
            print("-" * 40)
        except ValueError as err_val:
            print(f'ERROR!!..{err_val}')

        new_img_1 = numpy.clip(img.astype(float) + user_inp_func_1, 0, 255).astype('uint8')
        print("Working on IT!!...Increasing Brightness..")
        print("-" * 10)
        save_print(res , new_img_1 , "Brightness+")

    elif req_inp == 2:
        try:
            user_inp_func_2 = int(input("By..How much you want to Decrease brightness??.[5,4,2] "))
            print("-" * 40)
        except ValueError as err_val:
            print(f'ERROR!!..{err_val}')

        new_img_2 = numpy.clip(img.astype(float) - user_inp_func_2, 0, 255).astype('uint8')
        print("Working on IT!!...Decreasing Brightness..")
        print("-" * 10)
        save_print(res , new_img_2 , "Brightness-")

    elif req_inp == 3:
        user_inp_func_3 = input("Which colour you want to boost??..[R,G,B] ")
        if user_inp_func_3 == "R" or user_inp_func_3 == "r":
            try:
                print("-" * 30)
                user_inp_func_3_A = int(input("Boost Redness by..??.[5,4,2] "))
                print("-" * 40)
            except ValueError as err_val:
                print(f'ERROR!!..{err_val}')

            new_img_3_A = img.astype(float).copy() 

            # Apply your math
            new_img_3_A[:, :, 0] += user_inp_func_3_A
            new_img_3_A[:, :, 1] -= user_inp_func_3_A
            new_img_3_A[:, :, 2] -= user_inp_func_3_A

            # Clip the values so they stay in the 0-255 range and convert back to uint8
            new_img_3_A = numpy.clip(new_img_3_A, 0, 255).astype('uint8')
            print("Working on IT!!...Increasing Image Redness..")
            print("-" * 10)
            save_print(res , new_img_3_A , "Red_Effect+")

        elif user_inp_func_3 == "G" or user_inp_func_3 == "g":
            try:
                print("-" * 30)
                user_inp_func_3_B = int(input("Boost Grenish Colour by..??.[5,4,2] "))
                print("-" * 40)
            except ValueError as err_val:
                print(f'ERROR!!..{err_val}')

            new_img_3_B = img.astype(float).copy() 

            # math
            new_img_3_B[:, :, 0] -= user_inp_func_3_B
            new_img_3_B[:, :, 1] += user_inp_func_3_B #increase green
            new_img_3_B[:, :, 2] -= user_inp_func_3_B

            # Clip the values so they stay in the 0-255 range and convert back to uint8
            new_img_3_B = numpy.clip(new_img_3_B, 0, 255).astype('uint8')
            print("Working on IT!!...Increasing Image Grenish Colour..")
            print("-" * 10)
            save_print(res , new_img_3_B , "Green_Effect+")
            

        elif user_inp_func_3 == "B" or user_inp_func_3 == "b":
            try:
                print("-" * 30)
                user_inp_func_3_C = int(input("Boost Blueish Colour by..??.[5,4,2] "))
                print("-" * 40)
            except ValueError as err_val:
                print(f'ERROR!!..{err_val}')

            new_img_3_C = img.astype(float).copy() 

            # math
            new_img_3_C[:, :, 0] -= user_inp_func_3_C
            new_img_3_C[:, :, 1] -= user_inp_func_3_C
            new_img_3_C[:, :, 2] += user_inp_func_3_C #increase blue

            # Clip the values so they stay in the 0-255 range and convert back to uint8
            new_img_3_C = numpy.clip(new_img_3_C, 0, 255).astype('uint8')
            print("Working on IT!!...Increasing Image Blueish Colour..")
            print("-" * 10)
            save_print(res , new_img_3_C , "Blue_Effect+")
        else:
            print("Choose from the given Option..Above!!")
        
    elif req_inp == 4:
        try:
            user_inp_func_4 = int(input("Decrease image size by??.[5,4,2] "))
            print("-" * 40)
        except ValueError as err_val:
            print(f'ERROR!!..{err_val}')
        new_img_4 = img.copy()
        new_img_4 = new_img_4[::user_inp_func_4 , ::user_inp_func_4]
        print("Working on IT!!...Decreasing Image Size..")
        print("-" * 10)
        save_print(res , new_img_4 , "Decreased_Size")

    elif req_inp == 5:
        gray_img = img.astype(float).copy()

        # Math (store the result!)
        gray_img = (
            gray_img[:, :, 0] * 0.299 +
            gray_img[:, :, 1] * 0.587 +
            gray_img[:, :, 2] * 0.114
        )
        # Clip and convert
        gray_img = numpy.clip(gray_img, 0, 255).astype('uint8')
        print("Converting and Saving..Please Wait!!")
        print("-" * 15)
        save_print(res , gray_img , "Greyscale") 


while True:
    if os.path.exists(img_path):#If path is Valid
        img = mpimg.imread(img_path)
        print("-" * 50)
        print(f'Filename : {os.path.basename(img_path)}\nFileSize : {os.path.getsize(img_path)} bytes\nSize : {img.shape}\nShape : {img.size}\nDType : {img.dtype}')
        print("-" * 50)
        print(f'1 → Increase brightness\n2 → Decrease brightness\n3 → Change RGB channels\n4 → Downsample\n5 → Greyscale\n0 → Exit')
        print("-" * 50)
        try:
            req_inp = int(input("Choose from the Given Input : "))
            if req_inp == 0:
                print("-" * 15)
                print("Exiting...")
                break
            print("-" * 50)
        except ValueError as err_val:
            print(f'ERROR!!..{err_val}')
        user_func(req_inp , img)

    else:
        print("Path not specified")
        break
