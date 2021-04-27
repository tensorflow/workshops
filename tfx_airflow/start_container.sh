#!/bin/bash

GREEN=$(tput setaf 2)
NORMAL=$(tput sgr0)

read -p "${GREEN}Pull Docker image (2.7GB) from Docker Hub? (y/N) ${NORMAL} " -n 1 -r
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    printf "${GREEN}\nNot pulling.  You should have a copy of the image already.${NORMAL}\n\n"
else
    printf "${GREEN}\nPulling ...${NORMAL}\n"
    docker pull gcr.io/tfx-oss-public/tfx-workshop:latest
fi

printf "${GREEN}Creating directories${NORMAL}\n"
cd `dirname ${BASH_SOURCE[0]}`
pwd
rm -rf workshop
mkdir workshop
mkdir workshop/airflow
export WSHOME=$PWD/workshop

printf "${GREEN}Starting workshop container${NORMAL}\n\n"
printf "${GREEN}Next Step:${NORMAL}\n"
printf "${GREEN}When you see the prompt 'root@<hex id>:/#'${NORMAL}\n"
printf "${GREEN}Enter 'source setup_demo.sh'${NORMAL}\n\n"
printf "${GREEN}Wait for init to complete, and create a password${NORMAL}\n"
printf "${GREEN}Airflow and Jupyter will then both start:${NORMAL}\n"
printf "${GREEN}Airflow: Open a browser and go to http://localhost:8080${NORMAL}\n"
printf "${GREEN}Jupyter: Open a browser and go to http://localhost:8888${NORMAL}\n"
docker-compose -f docker-compose.yaml run --rm --service-ports tfx
