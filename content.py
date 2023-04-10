# Contributions-Importer-For-Github/run_script.py
import sys
import git
sys.path.append("./Contributions-Importer-For-Github/")
from git_contributions_importer import Importer

# Your private repo or Bitbucket repo
repo = git.Repo("/home/fachiis/Desktop/codes/iCubefarm/icfui-next")
repo2 = git.Repo("/home/fachiis/Desktop/codes/iCubefarm/icf_upgrade")
# Your mock repo
mock_repo = git.Repo("/home/fachiis/Desktop/codes/BitBucket2GitHub")
importer = Importer([repo, repo2], mock_repo)
# I use both my personal email and work email here,
# Since the private repo uses work email, and Github uses my personal email
print("twxms")
