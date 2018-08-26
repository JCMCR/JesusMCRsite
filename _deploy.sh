#!/bin/bash

BUILD_DIRECTORY=../build/
DEPLOYMENT_TARGET=kh562@zeus.jesus.cam.ac.uk:/societies/gradsoc/public_html

BUILD_COMMAND="jekyll build --destination $BUILD_DIRECTORY"
DEPLOY_COMMAND="rsync -avr $BUILD_DIRECTORY $DEPLOYMENT_TARGET"



read -r -p "Do you want to compile? [Y/n] " response
if [[ $response  =~ ^([nN][oO]|[nN])$ ]]; then
    echo "Skippping compilation"
    exit 1
else
    echo "Compiling..."
    if $BUILD_COMMAND; then
        echo "Compiled."
    else
        echo "Compile failed: aborting commit."
        exit 1
    fi
fi

read -r -p "Do you want to deploy? [Y/n] " response
if [[ $response  =~ ^([nN][oO]|[nN])$ ]]; then
    echo "Skippping deployment"
else
    echo "Deploying..."
    if $DEPLOY_COMMAND; then
        echo "Deployed."	
    else
        echo "Deploy failed: aborting commit."
        exit 1
    fi
fi
