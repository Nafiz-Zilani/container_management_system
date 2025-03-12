from src.command import *
import os

# Create a compose file for the user Docker image file----------------------------
def create_file_with_content(file: str):
    
    os.chdir('./Docker/')
    # print(subprocess.run("pwd", shell=True, capture_output=True, text=True))
    

    filename = file + "-compose.yml"

    content = """version: '3'

services:
  """+file+""":
    image: """+file+"""-imagefile:latest
    container_name: """+file+"""
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers."""+file+""".rule=Host(`"""+file+""".localhost`)"
      - "traefik.docker.network=my-network"
    networks:
      - my-network

networks:
  my-network:
    driver: bridge
"""

    with open(filename, 'w') as file:
        file.write(content)

    return filename

# Create a Docker file to create the user image-----------------------------------
def create_image_file(file: str):
    
    filename = file + "-imagefile"

    content = """FROM nginx:latest

WORKDIR /usr/src/app

RUN rm -rf /usr/share/nginx/html/*
COPY ./main/index.html /usr/share/nginx/html/

RUN apt-get update && apt-get install -y
RUN apt install zsh -y
"""

    with open(filename, 'w') as file:
        file.write(content)
    
    return filename

# Create a folder for the user project-------------------------------------------
def user_project_folder_create(user_folder_name: str):
    print("1: ", os.getcwd())
    if os.path.exists('User_Projects'):
        print("2: ", os.getcwd())
        os.chdir('User_Projects')
        os.mkdir(user_folder_name)
        os.chdir(user_folder_name)
        os.mkdir('main')
        print("3: ", os.getcwd())
    else:
        os.chdir('../')
        if not os.path.exists('User_Projects'):
            os.mkdir('User_Projects')
            print("4: ", os.getcwd())
            user_project_folder_create(user_folder_name)
        else:
            print("4: ", os.getcwd())
            user_project_folder_create(user_folder_name)

# Find the user folder and run the command---------------------------------------
def user_project_folder_finder(user_name: str):

    if os.path.exists('User_Projects'):
        # os.chdir('../')
        print("1: ", os.getcwd())
        os.chdir('User_Projects')
        os.chdir(user_name)
        build_image(create_image_file(user_name))
        print("2: ", os.getcwd())
    else:
        os.chdir('../')
        print("3: ", os.getcwd())
        # user_project_folder_create(user_name)
        user_project_folder_finder(user_name)


