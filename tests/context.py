'''
adding parent directory to PYTHONPATH so test modules can import application
by using 'from .context import immogarantie_backend'
'''
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import app
