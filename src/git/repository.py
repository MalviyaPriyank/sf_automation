import git 
import os 

clone_dir = "/Users/priyankmalviya/snowchain/agentic/repo"

# Repo URL
repo_url = "https://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@github.com/MalviyaPriyank/Snowchain.git"

class Repository:
    def __init__(self):
        self.url=repo_url
        self.local_dir=clone_dir

    def clone_repo(self):
        if not os.path.exists(self.local_dir):
        # Directory doesn't exist → clone fresh
            self.repo = git.Repo.clone_from(self.url, self.local_dir)
        else:
            # If directory exists but already has a git repo
            self.repo = git.Repo(self.local_dir)
    def instantiate_repo(self):
        repo = git.Repo(self.local_dir)
        self.repo=repo
    
    def write_file_to_local(self,filepath,content):
        full_path = os.path.join(self.local_dir, filepath)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w") as f:
            f.write(content)
    
    def add_file_for_push(self,filepath,commit_msg):
        full_path = os.path.join(self.local_dir, filepath)
        self.repo.index.add([full_path])   
        self.repo.index.commit(commit_msg)

    def push_file_to_remote(self):
        origin=self.repo.remote(name='origin')
        origin.push()
