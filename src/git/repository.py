import git 
import os 

clone_dir = "/Users/priyankmalviya/snowchain/agentic/repo"

# Repo URL
repo_url = "https://github.com/MalviyaPriyank/Snowchain.git"

class Repository:
    def __init__(self):
        self.url=repo_url
        self.local_dir=clone_dir

    def clone_repo(self):
        if not os.path.exists(self.local_dir):
            repo = git.Repo.clone_from(self.url, self.local_dir)
        self.repo=repo
    
    def instantiate_repo(self):
        repo = git.Repo(self.local_dir)
        self.repo=repo
    
    def write_file_to_local(self,filepath,content):
        with open(f"{self.local_dir}/{filepath}","w") as f:
            f.write(content)
    
    def add_file_for_push(self,filepath,commit_msg):
        self.repo.add(filepath)
        self.repo.index.commit(commit_msg)

    def push_file_to_remote(self):
        origin=self.repo.remote(name='origin')
        origin.push()
