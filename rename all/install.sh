#!/bin/bash

reset
wget https://github.com/hertkof/linux_stuff/blob/master/rename%20all/rename_all.py
reset
echo 'Write your root password to change premession of script and move it to /usr/local/sbin folder:'
sudo mv rename_all.py /usr/local/sbin; sudo chmod +x /usr/local/sbin/rename_all.py
echo rn='rename_all.py' >> ~/.bashrc; source ~/.bashrc
echo 'Have fun :)'

