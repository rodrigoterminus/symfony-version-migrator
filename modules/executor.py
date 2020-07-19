#!/usr/bin/env python3

import versions
import directory

def migrate(project_path, current_version, target_version):
    versions.validate(current_version, target_version)
    directory.create(project_path, target_version)


def main():
    migrate('/Users/rodrigoduarte/dev/rodrigoterminus/between', 3, 4)


if __name__ == "__main__":
    main()
