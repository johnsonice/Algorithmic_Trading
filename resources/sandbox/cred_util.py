#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 16:33:54 2020

@author: chengyu
"""

import json

def load_cred(cred_path):
    with open(cred_path) as f:
      data = json.load(f)
     
    return data


if __name__ == "__main__":
    cred_path = '../../credential/ini.json'
    cred = load_cred(cred_path)
    print(cred)