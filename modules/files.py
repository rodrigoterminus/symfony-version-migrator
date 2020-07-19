#!/usr/bin/env python3

import urllib.request
import versions

files_by_version = {
    4: (
        {
            'path': 'bin/console',
            'source_url': 'https://raw.githubusercontent.com/symfony/recipes/master/symfony/console/4.4/bin/console'
        },
        {
            'path': 'public/index.php',
            'source_url': 'https://raw.githubusercontent.com/symfony/recipes/master/symfony/framework-bundle/4.4/public/index.php'
        }
    )
}


def fetchContent(source_url):
    with urllib.request.urlopen(source_url) as response:
        return response.read()


def create(project_path, target_version):
    versions.validate(target_version)

    print(f'\n📄 Creating files for Symfony {target_version}\n\n')
    files = files_by_version[target_version]

    for file in files:
        relative_path = file['path']
        absolute_path = f'{project_path}/{relative_path}'

        try:
            urllib.request.urlretrieve(file['source_url'], absolute_path)
            print(f'🟢 {relative_path}')
        except:
            print(f'🔴 Unable to create "{relative_path}"')
            
