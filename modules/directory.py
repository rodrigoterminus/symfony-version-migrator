#!/usr/bin/env python3

import os
import versions

version_structures = {
    3: (
        'app',
        'app/config',
        'bin',
        'src',
        'var',
        'web',
        'web/assets',
        'web/bundles'
    ),
    4: (
        'bin',
        'config',
        'config/packages',
        'config/routes',
        'migrations',
        'public',
        'src',
        'templates',
        'tests',
        'translations',
        'var'
    )
}


def create(project_path, target_version):
    versions.validate(target_version)
    folders = version_structures[target_version]

    print(f'\n📂 Creating directory structure for Symfony {target_version}\n\n')

    for folder in folders:
        path = f'{project_path}/{folder}'

        if os.path.isdir(path):
            print(f'🟡 Folder "{folder}" already exists')
            continue

        print(f'🟢 Creating "{folder}"')
        os.mkdir(path)
