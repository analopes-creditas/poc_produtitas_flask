import os


class BodyGit:

    def create_org_repos(self, data: dict) -> dict:
        return {
            'org': data['org'], # required
            'name': data['name'].replace(' ', '_'), # required
            'description': data['description'] if data['description'] else '',
            'homepage': data['homepage'],
            'private': data['private'], # Padrão: false
            'visibility': data['visibility'], # public, private, internal
            'has_issues': data['has_issues'], # Padrão: true
            'has_projects': data['has_projects'], # Padrão: true
            'has_wiki': data['has_wiki'], # Padrão: true
            'is_template': data['is_template'], # Padrão: false
            'team_id': data['team_id'],
            'auto_init': data['auto_init'], # Padrão: false
            'gitignore_template': data['gitignore_template'],
            'license_template': data['license_template'],
            'allow_squash_merge': data['allow_squash_merge'], # Padrão: true
            'allow_merge_commit': data['allow_merge_commit'], # Padrão: true
            'allow_rebase_merge': data['allow_rebase_merge'] # Padrão: true
        }


    def create_repos_template(self, data: dict) -> dict:
        return {
            'owner': data['owner'],
            'name': data['name'].replace(' ', '_'), # required
            'description': data['description'] if data['description'] else '',
            'include_all_branches': True, # Padrão: false
            'private': True # Padrão: false
        }


    def update_repos(self, data: dict) -> dict:
        return {
            'owner': data['owner'], # required
            'repo': data['repo'], # required
            'name': data['name'].replace(' ', '_'),
            'description': data['description'],
            'homepage': data['homepage'],
            'private': data['private'], # Padrão: false
            'visibility': data['visibility'], # public, private, internal
            'has_issues': data['has_issues'], # Padrão: true
            'has_projects': data['has_projects'], # Padrão: true
            'has_wiki': data['has_wiki'], # Padrão: true
            'is_template': data['is_template'], # Padrão: false
            'default_branch': data['default_branch'],
            'allow_squash_merge': data['allow_squash_merge'], # Padrão: true
            'allow_rebase_merge': data['allow_rebase_merge'] # Padrão: true
        }


    def delete_repos(self, data: dict) -> dict:
        return {
            'owner': data['owner'], # required
            'repo': data['repo'] # required
        }
