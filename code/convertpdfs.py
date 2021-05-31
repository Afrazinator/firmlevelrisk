import _helpers as h

# Change me
homedir = 'E:/RA/Isha/firmlevelrisk'

# Modules
import os
os.chdir(homedir)
import sys
if not 'code/' in sys.path:
    sys.path.append('code/')

earningscall_dir = 'input/earningscall_transcripts/'

transcripts_raw = h.load_pdf(earningscall_dir)
