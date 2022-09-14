# Contributions-Importer-For-Github/run_script.py
import sys
import git
sys.path.append("./Contributions-Importer-For-Github/")
from git_contributions_importer import Importer

# Your private repo or Bitbucket repo
repo = git.Repo("/home/fachiis/Desktop/codes/iCubefarm/icfui-next")
# Your mock repo
mock_repo = git.Repo("/home/fachiis/Desktop/codes/BitBucket2GitHub")
importer = Importer([repo], mock_repo)
# I use both my personal email and work email here,
# Since the private repo uses work email, and Github uses my personal email
importer.set_author(['zashafachii@gmail.com', 'felix@icubefarm.com'])
importer.import_repository()
