#!/bin/bash

wget https://github.com/hertkof/linux_stuff/blob/master/alldo/alldo.py
sudo mv alldo.py /usr/local/sbin
sudo chmod +x /usr/local/sbin/alldo.py
cp .bashrc .bashrc.bak
echo alias ad='alldo.py' >> ~/.bashrc
source ~/.bashrc
