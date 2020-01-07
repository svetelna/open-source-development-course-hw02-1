#!/bin/bash

find ossdev/tests/ -name \*.py -type f -print0 | xargs -0 python
