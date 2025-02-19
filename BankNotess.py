# -*- coding: utf-8 -*-
"""
Created on 19 / 2 / 2025

"""
from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class BankNote(BaseModel):
    variance: float 
    skewness: float 
    curtosis: float 
    entropy: float