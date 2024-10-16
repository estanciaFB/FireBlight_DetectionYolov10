# Setup to run our implementation

### We recommend use a conda environment:

`conda create -n yolov10 python=3.9`

`conda activate yolov10`

or create the environment with the requirements file

`conda create --name <env> --file requirements.txt`

### Make sure you have your Cuda drivers from:
https://www.nvidia.com/en-us/drivers/

### Install this version of torch:
`pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121`


### With that you are able to run our fire_blight.ipynb Jupyter to rain the model
