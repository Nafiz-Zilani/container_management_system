import subprocess
import os

def run_command(user_name):
    # os.chdir('Docker/')
    commands = ["pwd", "docker-compose -f "+user_name+" up -d"]

    for command in commands:
        subprocess.run(command, shell=True, capture_output=True, text=True)
        # print(f"Output of {command}:\n", result.stdout)
        # print(f"Error of {command}:\n", result.stderr)

def build_image(image_name):
    commands = ["pwd", "docker build -f "+image_name+" -t "+image_name+":latest ."]
    # docker build -f Ghostdockerfile -t my-custom-image .

    for command in commands:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print(f"Output of {command}:\n", result.stderr)
        print(f"Error of {command}:\n", result.stderr)