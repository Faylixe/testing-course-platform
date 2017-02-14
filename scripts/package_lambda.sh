#!/bin/bash

BASEDIR=$1
NAME=$2
FILE=`$BASEDIR/lambda/$NAME.py`
PACKAGE="$NAME.zip"
CHMOD 755 $FILE
zip -r9 $PACKAGE model common # TODO : Add dependencies.
cd lambda
zip -r9 ../$PACKAGE $FILE
cd ..