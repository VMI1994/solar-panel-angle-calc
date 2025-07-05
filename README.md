# solar-panel-angle-calc

![1](https://github.com/VMI1994/solar-panel-angle-calc/blob/main/solar.png)

A simple docker container to give you the proper angle for solar panels by season and zip code.  Requires docker.

Usage:

git clone https://github/com/vmi1994/solar-panel-angle-calc
cd solar-panel-angle-calc
sudo docker build -t solar .
sudo docker run -it --rm --name solar solar
