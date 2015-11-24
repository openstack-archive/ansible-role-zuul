=================
ansible-role-zuul
=================

Ansible role to manage Zuul

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

Packages
~~~~~~~~

Package repository index files should be up to date before using this role, we
do not manage them.

Role Variables
--------------

Dependencies
------------

Example Playbook
----------------

.. code-block:: yaml

    - name: Install zuul
      hosts: zuul
      roles:
        - ansible-role-zuul
