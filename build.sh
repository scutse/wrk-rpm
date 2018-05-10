#!/bin/bash

rm -rf *.rpm
spectool -g wrk.spec
mock -r epel-7-x86_64 --spec=wrk.spec --sources=. --resultdir=. --buildsrpm
mock -r epel-7-x86_64 --rebuild --resultdir=. *.src.rpm 
