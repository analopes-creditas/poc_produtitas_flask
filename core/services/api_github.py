import os
import json
import requests


class ApiGitHub:

    def __init__(self):
        self.url_prefix = 'https://api.github.com'
        self.headers = {
            'Authorization': f"Bearer {os.getenv('GH_PERSONAL_TOKEN', '')}",
            'Content-Type': 'application/json'
        }


    def create_org_repos(self, org: str, body: dict) -> dict:
        """ Create an organization repository.

            Parameters:
                org (str): The organization name.
                body (dict): Data to create the repository.
        """

        url = f'{self.url_prefix}/orgs/{org}/repos'
        response = requests.request('POST', url, data=json.dumps(body), headers=self.headers, verify=False)
        return json.loads(response.text)


    def create_repos_template(self, template_owner: str, template_repo: str, body: dict) -> dict:
        """ Create a repository using a template.
        
            Parameters:
                template_owner (str): The account owner of the repository template.
                template_repo (str): The name of the repository template.
                body (dict): Data to create the repository.
        """

        url = f'{self.url_prefix}/repos/{template_owner}/{template_repo}/generate'
        response = requests.request('POST', url, data=json.dumps(body), headers=self.headers, verify=False)
        return json.loads(response.text)
