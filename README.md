# Setup to run our implementation

### We recommend use a conda environment:

`conda create -n yolov10 python=3.9`

`conda activate yolov10`

`pip install -r requirements.txt`

### Install this version of Huggingface through conda
 `conda install -c conda-forge huggingface_hub`

### Install the YOLOv10 GitHub
 `pip install git+https://github.com/THU-MIG/yolov10.git`

### Make sure you have your Cuda drivers from:
https://www.nvidia.com/en-us/drivers/

### Install this version of torch:
`pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121`


### With that you are able to run our fire_blight.ipynb Jupyter to rain the model

#### If you get this error:
_imshow(winname.encode("unicode_escape").decode(), mat)
cv2.error: OpenCV(4.10.0) D:\a\opencv-python\opencv-python\opencv\modules\highgui\src\window.cpp:1301: error: (-2:Unspecified error) The function is not implemented. Rebuild the library with Windows, GTK+ 2.x or Cocoa support. If you are on Ubuntu or Debian, install libgtk2.0-dev and pkg-config, then re-run cmake or configure script in function 'cvShowImage'

#### If in Ubuntu use this:
`sudo apt-get update`

`sudo apt-get install -y libgtk2.0-dev pkg-config`

`sudo apt-get install -y libgl1-mesa-glx`

`sudo apt-get install -y libqt5gui5 libqt5webkit5 libqt5test5 libqt5widgets5 libqt5x11extras5 libcanberra-gtk-module`
=======
# Setup to run our implementation

### We recommend use a conda environment:

`conda create -n yolov10 python=3.9`

`conda activate yolov10`

`pip install -r requirements.txt`

### Install this version of Huggingface through conda
 `conda install -c conda-forge huggingface_hub`

### Install the YOLOv10 GitHub
 `pip install git+https://github.com/THU-MIG/yolov10.git`

### Make sure you have your Cuda drivers from:
https://www.nvidia.com/en-us/drivers/

### Install this version of torch:
`pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121`


### With that you are able to run our fire_blight.ipynb Jupyter to rain the model

#### If you get this error:
_imshow(winname.encode("unicode_escape").decode(), mat)
cv2.error: OpenCV(4.10.0) D:\a\opencv-python\opencv-python\opencv\modules\highgui\src\window.cpp:1301: error: (-2:Unspecified error) The function is not implemented. Rebuild the library with Windows, GTK+ 2.x or Cocoa support. If you are on Ubuntu or Debian, install libgtk2.0-dev and pkg-config, then re-run cmake or configure script in function 'cvShowImage'

#### If in Ubuntu use this:
`sudo apt-get update`

`sudo apt-get install -y libgtk2.0-dev pkg-config`

`sudo apt-get install -y libgl1-mesa-glx`

`sudo apt-get install -y libqt5gui5 libqt5webkit5 libqt5test5 libqt5widgets5 libqt5x11extras5 libcanberra-gtk-module`
>>>>>>> a6f8be59f3aabedc51739f18d978192a9c985c39
