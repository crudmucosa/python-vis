#!/usr/bin/env python

import os
for root, dirs, files in os.walk("data"):
	print(root, dirs, files)