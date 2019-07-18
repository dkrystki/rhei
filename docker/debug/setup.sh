#!/usr/bin/env bash

apt-get update && apt-get install -y openssh-server supervisor sudo

addgroup --gid 1000 "$1"
adduser --disabled-password --disabled-login --gecos "" --uid 1000 --gid 1000 "$1"
echo "su "$1"" >> /root/.bashrc

usermod -aG sudo "$1"

mkdir /var/run/sshd
echo ""$1":password" | chpasswd
echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
echo "AllowUsers "$1"" >> /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

export NOTVISIBLE="in users profile"
echo "export VISIBLE=now" >> /etc/profile

# uncomment aliases and colors
echo 'force_color_prompt=yes' >> /home/"$1"/.bashrc
echo "alias ll='ls -la'" >> /home/"$1"/.bashrc
echo "alias la='ls -A'" >> /home/"$1"/.bashrc

cp ./docker/motd/motd /etc/motd
echo "echo -e \"`cat /etc/motd`\"" >> /home/"$1"/.bashrc

cp ./docker/supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
