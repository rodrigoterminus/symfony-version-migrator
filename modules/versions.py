#!/usr/bin/env python3


available = (3, 4)

def validate(*args):
    for version in args:
        if version not in available:
            raise ValueError(f'Version {version} is not implemented')
