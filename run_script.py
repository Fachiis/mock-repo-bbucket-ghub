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
repo = git.Repo(os.getenv('PROJ_ONE'))
repo2 = git.Repo(os.getenv('PROJ_TWO'))
repo3 = git.Repo(os.getenv('PROJ_THREE'))

# Your mock repo
mock_repo = git.Repo(os.getenv('MOCK_REPO_PATH'))
importer = Importer([repo, repo2, repo3], mock_repo)

# Get author emails from environment variables and split by comma
author_emails = os.getenv('AUTHOR_EMAILS').split(',')
importer.set_author(author_emails)
importer.import_repository()
