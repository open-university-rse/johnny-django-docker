from django.test import TestCase
from github import Github
from django.conf import settings

class GithubReproTest(TestCase):
    def test_init(self):
        repo_folder = settings.TEST_DIR 
       
        g = Github("ad3a2b49226f3953c5a48402bf20892dab4cd750")
        repo = g.get_repo("dalmatianrex/covid-stretch")
        # print("clone_url:", repo.clone_url)
        # contents = repo.get_contents("")
        # while contents:
        #     file_content = contents.pop(0)
        #     if file_content.type == "dir":
        #         contents.extend(repo.get_contents(file_content.path))
        #     else:
        #         print(file_content)
        # commits = repro.get_commits()
        # for commit in commits:
        #     print(commit.author, commit.sha, commit.files)
        
