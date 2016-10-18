=================
ansible-role-zuul
=================

Ansible role to manage Zuul.

* License: Apache License, Version 2.0
* Documentation: https://ansible-role-zuul.readthedocs.org
* Source: https://git.openstack.org/cgit/openstack/ansible-role-zuul
* Bugs: https://bugs.launchpad.net/ansible-role-zuul

Description
-----------

Zuul is a program that is used to gate the source code repository of a project
so that changes are only merged if they pass tests.

Requirements
------------

See `bindep.txt` for role dependencies.

Packages
~~~~~~~~

Package repository index files should be up to date before using this role, we
do not manage them.

SSH
~~~

An SSH private key will need to be installed before you can use zuul. The
contents of the private key will be used by ``zuul_config_gerrit_user`` and
should be copied to ``zuul_config_gerrit_sshkey``.

Role Variables
--------------

.. code-block:: yaml

    # Method used to install zuul. Valid values are git and pip.
    # Default: git
    zuul_install_method: git

    # Git, SSH, or HTTP(s) protocol address of the git repository.
    # Default: https://git.openstack.org/openstack-infra/zuul
    zuul_git_uri: https://git.openstack.org/openstack-infra/zuul

    # What version of the repository to check out.
    # Default: master
    zuul_git_version: master

    # Absolute path of where the repository should be checked out to.
    # Default: /opt/ansible-role-zuul/git/openstack-infra/zuul
    zuul_git_dest: /opt/ansible-role-zuul/git/openstack-infra/zuul

    # The version number to install from the Python Package Index.
    # Default: None
    zuul_pip_version:

    # Name of the user to be created.
    # Default: zuul
    zuul_user_name: zuul

    # Name of the group to be created.
    # Default: zuul
    zuul_user_group: zuul

    # Path of home directory to be created.
    # Default: /var/lib/zuul
    zuul_user_home: /var/lib/zuul

Zuul Merger Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

    # Value to pass to git config user.email.
    # Default: Empty
    zuul_config_merger_git_user_email: ""

    # Value to pass to git config user.name.
    # Default: Empty
    zuul_config_merger_git_user_name: ""

Dependencies
------------

Example Playbook
----------------

.. code-block:: yaml

    - name: Install zuul
      hosts: zuul
      roles:
        - ansible-role-zuul
