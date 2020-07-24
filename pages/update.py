import os
import re

from datetime import datetime
now = datetime.now()

from dotenv import load_dotenv
load_dotenv()
jhu_git = os.getenv("JHU_GIT")

import os


human_dt_str = now.strftime("%m/%d") + " at " + now.strftime("%I") + ":" + now.strftime("%M%p")
human_dt_str = human_dt_str.lower()
date_str = now.strftime("%m/%d/%Y")
req_str = now.strftime("%Y%m%d")


start_cwd = os.path.dirname(os.path.realpath(__file__))
print(start_cwd)
os.chdir(start_cwd)

# Update JHU git repo:
os.chdir(jhu_git)
os.system("git pull")
#exit(0)


# 91-DIVOC #1 + #4
os.chdir(start_cwd)
os.system("python jhu.py")
os.system("python ctp.py")
os.system("python owid.py")
os.system("python merged.py")

# 91-DIVOC #2
os.chdir(start_cwd)
os.chdir("./covid-by-your-locations/")
os.system("python processData.py")

# 91-DIVOC #3
os.chdir(start_cwd)
os.chdir("./coronavirus-1000-person-community/")
os.system("python processData.py")

# 91-DIVOC #5
os.chdir(start_cwd)
os.chdir("./interactive-visualziation-of-covid-19-in-illinois/sync/")
os.system("python sync.py")


# Write js
os.chdir(start_cwd)
js = f'_dateUpdated = "{date_str}";\n' +\
     f'_reqStr = "{req_str}";\n' +\
     f'\n' +\
     f'$("#jhu-updated").html("(Updated: {human_dt_str})");\n'

with open("jhu-updated.js", "w") as out:
  out.write(js)