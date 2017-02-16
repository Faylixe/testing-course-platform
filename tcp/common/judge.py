#!/usr/bin/python

""" """

def clone(repository):
    """
    :param repository:
    """
    # TODO : Clone created fork locally.
    return None

def commit_and_push(repository):
    """
    """
    """
    :param repository:
    """
    # TODO : Commit forked repository.
    return False

class Judge(object):
    """
    """

    def __init__(self, credentials, target_url):
        """
        :param credentials:
        :param target_url:
        """
        self.client = Github(credentials[0], credentials[1])
        self.target_url = target_url
    
    def with_fork(self, fork_consumer):
        """

        :param fork_consumer:
        """
        repository = self.client.get_repo(self.target_url)
        user = self.client.get_user()
        fork = user.create_fork(repository)
        path = clone(fork.clone_url)
        fork_consumer(path)
        if commit_and_push(path):
            repository.create_pull(title='', body='', base='', head='') # TODO : Fill info.

    def score(self, evaluator):
        """
        """
        path = clone(self.target_url)
        score = evaluator(path)
        # TODO : REMOVE PATH.
        return score