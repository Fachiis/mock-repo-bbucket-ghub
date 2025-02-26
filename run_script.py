# Contributions-Importer-For-Github/run_script.py
import sys
import git
sys.path.append("./Contributions-Importer-For-Github/")
from git_contributions_importer import Importer

# Your private repo or Bitbucket repo
repo = git.Repo("/Users/fachiizasha/Code/iCUBEFARM/icfui-next")
repo2 = git.Repo("/Users/fachiizasha/Code/iCUBEFARM/icf_upgrade")
repo3 = git.Repo("/Users/fachiizasha/Code/Poblysh/poblysh-frontend")
# Your mock repo
mock_repo = git.Repo("/Users/fachiizasha/Code/mock-repo-bbucket-ghub")
importer = Importer([repo, repo2, repo3], mock_repo)
# I use both my personal email and work email here,
# Since the private repo uses work email, and Github uses my personal email
importer.set_author(['zashafachii@gmail.com', 'felix@icubefarm.com', 'felix@poblysh.com',])
importer.import_repository()
