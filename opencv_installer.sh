#######################################################################
# Installs OpenCV on a Raspberry Pi                                   #
# See the GitHub documentation that this script is based off of:      #
# https://github.com/Tes3awy/OpenCV-3.2.0-Compiling-on-Raspberry-Pi   #
#######################################################################

#Step 1
sudo apt-get update
sudo apt-get upgrade
sudo rpi-update
sudo reboot now

#Step 2
sudo apt-get install build-essential cmake pkg-config

#Step 3
sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev

#Step 4
sudo apt-get install libgtk2.0-dev libgstreamer0.10-0-dbg libgstreamer0.10-0 libgstreamer0.10-dev libv4l-0 libv4l-dev

#Step 5
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev

#Step 6
sudo apt-get install libatlas-base-dev gfortran
sudo apt-get install python-numpy python-scipy python-matplotlib
sudo apt-get install default-jdk ant
sudo apt-get install libgtkglext1-dev
sudo apt-get install v4l-utils

#Step 7
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py

#Step 8
sudo apt-get install python2.7-dev

#Step 9
sudo pip install numpy

#Step 10
#Download OpenCV 3.2.0 and unpack it
cd ~
wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.2.0.zip
unzip opencv.zip

#Contrib Libraries (Non-free Modules)
wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.2.0.zip
unzip opencv_contrib.zip

#Step 11
#preparing the build
#JSM: I never did a cmake, but apparently these parameters will work okay as they are.
cd ~/opencv-3.2.0/
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D INSTALL_C_EXAMPLES=OFF -D INSTALL_PYTHON_EXAMPLES=ON -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.2.0/modules -D BUILD_EXAMPLES=ON -D ENABLE_NEON=ON ..

#Step 12
#takes about 3.5 to 4 hours with 3 threads.
#JSM: Rob and I ended up using 1 thread, which makes for a successful make.
#     (takes about 5 hours)
sudo make -j1
# If any errors occurs and the process fails to continue, execute
#sudo make clean

#Step 13:
#installing the build prepared in step 11
sudo make install
sudo ldconfig

#Step 14:
sudo nano /etc/ld.so.conf.d/opencv.conf
#opencv.conf will be blank, add the following line, then save and exit nano:
#(leave a blank line at the end of opencv.conf)
/usr/local/lib
#save opencv.conf by pressing ctrl+o get back again to the command line by pressing ctrl+x
sudo ldconfig
sudo nano /etc/bash.bashrc
#add the following lines at the bottom of bash.bashrc
PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig       
export PKG_CONFIG_PATH
#(leave a blank line at the end of bash.bashrc) save bash.bashrc changes (ctrl+o), then back at the command line (ctrl+x)

#Step 15: Reboot
sudo shutdown -r now

#Step 16 Last Step: verifying the installation
#Open Python 2 IDLE on RasPi Type the following lines in the python shell:
#>>> import cv2
#>>> print cv2.__version__
#the following line should appear then:
#'3.2.0'