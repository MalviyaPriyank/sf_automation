import git 
import os 

clone_dir = "/Users/priyankmalviya/snowchain/agentic/repo"

# Repo URL
repo_url = "https://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@github.com/MalviyaPriyank/Snowchain.git"
#repo_url="https://github.com/MalviyaPriyank/gyrusdemo.git"
#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

class Repository:
    def __init__(self,logger):
        self.url=repo_url
        self.local_dir=clone_dir
        self.logger=logger.getChild(self.__class__.__name__)

    def __clone_repo(self):
        if not os.path.exists(self.local_dir):
        # Directory doesn't exist → clone fresh
            self.repo = git.Repo.clone_from(self.url, self.local_dir)
        else:
            # If directory exists but already has a git repo
            self.repo = git.Repo(self.local_dir)
        self.logger.info("EXITTING: __clone_repo")
    def __instantiate_repo(self):
        self.logger.info("Instantiating repo")
        repo = git.Repo(self.local_dir)
        self.repo=repo
        self.logger.info("EXITTING: __instantiate_repo")
    
    def __write_file_to_local(self,filepath,content):
        self.logger.info(f"Write {content} to {filepath} in local at {self.local_dir}")
        full_path = os.path.join(self.local_dir, filepath)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w") as f:
            f.write(content)
        self.logger.info("EXITING: __write_file_to_local")
    
    def __add_file_for_push(self,filepath,commit_msg):
        self.logger.info(f"add {filepath} {commit_msg} for push")
        full_path = os.path.join(self.local_dir, filepath)
        self.repo.index.add([full_path])   
        self.repo.index.commit(commit_msg)
        self.logger.info("EXITING: __add_file_for_push")

    def __push_file_to_remote(self):
        self.logger.info(f"push file to remote")
        origin=self.repo.remote(name='origin')
        origin.push()
        self.logger.info("EXITING: __push_file_to_remote")

    def sync_repo(self,filepath,qry,commit_msg):
        self.logger.info("BEGIN: sync_repo ")
        self.__clone_repo()
        self.__instantiate_repo()
        self.__write_file_to_local(filepath=filepath,content=qry)
        self.__add_file_for_push(filepath=filepath,commit_msg=commit_msg)
        self.__push_file_to_remote()
        self.logger.info("EXITING: sync_repo")