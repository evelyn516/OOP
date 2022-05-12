import requests
from show_repo_data import Show


def fetch_repo_list(username):
        URL = (f"https://api.github.com/users/{username}/repos")
        list_of_repos = requests.get(URL).json()
        
        for repo in list_of_repos:
            Show(repo)
        
        return repo
