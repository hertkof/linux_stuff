#!/bin/bash

# You must run it on your local host not server
# where is not ip-address belong to.
# And also it must be run in $HOME
# So simple and easy,

echo "----------------------------------"
echo "Just press 'Enter' till next step:"
ssh-keygen -t rsa
echo "---------------------------------------------"
echo "Here is next step, now enter user@ip-address:"
read ipa
ssh $ipa mkdir -p .ssh
echo "------------------------------------------------"
echo "last step, please enter password again and wait:"
cat .ssh/id_rsa.pub | ssh $ipa 'cat >> .ssh/authorized_keys'
echo "The End! now just type 'ssh $ipa' and hit"
