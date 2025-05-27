import sys
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Add the contributions importer to the Python path
sys.path.append("./Contributions-Importer-For-Github/")
from git_contributions_importer import Importer
import git

# Get repository paths from environment variables
repo = git.Repo(os.getenv('ICF_UI_NEXT_PATH'))
repo2 = git.Repo(os.getenv('ICF_UPGRADE_PATH'))
repo3 = git.Repo(os.getenv('POBLYSH_FRONTEND_PATH'))

# Your mock repo
mock_repo = git.Repo(os.getenv('MOCK_REPO_PATH'))
importer = Importer([repo, repo2, repo3], mock_repo)

# Get author emails from environment variables and split by comma
author_emails = os.getenv('AUTHOR_EMAILS').split(',')
importer.set_author(author_emails)
importer.import_repository()
