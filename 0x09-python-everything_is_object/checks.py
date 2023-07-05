#!/usr/bin/python3
import sys

a = "SCHL"
ref_count = sys.getrefcount(a)
print(ref_count - 1)
