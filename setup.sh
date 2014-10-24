#!/bin/bash
rm -rf virtualenv
virtualenv virtualenv
virtualenv/bin/pip install flask==0.10.1
virtualenv/bin/pip install pytidylib
