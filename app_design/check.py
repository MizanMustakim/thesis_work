import subprocess
import pkg_resources
import sys
import torch
import platform


def check_dependency():

    pip_msg = ""

    if torch.cuda.is_available():
        # Get the number of available GPUs
        num_gpus = torch.cuda.device_count()
        pip_msg += f"Number of available GPUs: {num_gpus}\n"

        # Get information about each GPU
        for i in range(num_gpus):
            gpu_name = torch.cuda.get_device_name(i)
            gpu_memory = torch.cuda.get_device_properties(
                i).total_memory / 1e9  # in GB
            pip_msg += f"GPU {i}: {gpu_name}, Memory: {gpu_memory} GB\n"
    else:
        pip_msg += "CUDA is not available. Using CPU for computations.\n\n"
        cpu_info = {
            'Brand': platform.processor(),
            'Architecture': platform.machine(),
            'System': platform.system(),
        }

        # Print CPU information
        for key, value in cpu_info.items():
            pip_msg += f"{key}: {value}\n"

        pip_msg += "\n\nIt is recommended to choose only image for detection."

    # read requirements file
    # with open('K:/thesis_project/yolov7/requirements.txt') as f:
    #     requirements = f.read().splitlines()

    # # check if each requirement is installed
    # missing = []
    # for requirement in requirements:
    #     try:
    #         pkg_resources.require(requirement)
    #     except pkg_resources.DistributionNotFound:
    #         missing.append(requirement)

    # install missing packages
    # if missing:
    #     subprocess.check_call([sys.executable, '-m', 'pip', 'install',
    #                           '-r', 'K:/thesis_project/yolov7/requirements.txt'])
    #     print("Installed missing packages:", missing)
    #     pip_msg += "Installed missing packages:\n"
    #     for lib in missing:
    #         pip_msg += '* '+lib+'\n'
    # else:
    #     print("All required packages are already installed.")
    #     pip_msg += "All required packages are already installed."

    return pip_msg


def test_model(source):
    path = source.replace('\\', '/')
    if torch.cuda.is_available():
        process = subprocess.Popen(
            'python ./yolov7/detect.py --weights ./exp1.pt --device 0 --source {} --img-size 640 --no-trace'.format(path), shell=True, stdout=subprocess.PIPE)
    else:
        process = subprocess.Popen(
            'python ./yolov7/detect.py --weights ./exp1.pt --source {} --img-size 640 --no-trace'.format(path), shell=True, stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode('utf-8')


    

# def test_model(source):
#     path = source.replace('\\', '/')
#     if torch.cuda.is_available():
#         process = subprocess.Popen(
#             'python K:/thesis_project/yolov7/detect.py --weights K:/thesis_project/exp1.pt --device 0 --source {} --img-size 640 --no-trace'.format(path), shell=True, stdout=subprocess.PIPE)
#     else:
#         process = subprocess.Popen(
#             'python K:/thesis_project/yolov7/detect.py --weights K:/thesis_project/exp1.pt --source {} --img-size 640 --no-trace'.format(path), shell=True, stdout=subprocess.PIPE)
#     output, error = process.communicate()
#     return output.decode('utf-8')



