# Copyright 2018 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import pytest


def _get_user_and_group(host):
    user = 'zuul'
    group = 'zuul'
    if host.file('/etc/ci/mirror_info.sh').exists:
        user = 'zuul-test'
        group = 'zuul-test'

    return user, group


def test_zuul_user(host):
    user, group = _get_user_and_group(host)

    u = host.user(user)
    assert u.exists
    assert u.name == user
    assert u.group == group
    assert u.home == '/var/lib/zuul'

    f = host.file('/var/lib/zuul')
    assert f.exists
    assert f.is_directory
    assert f.user == user
    assert f.group == group
    # TODO(pabelanger): Validate mode


def test_zuul_config(host):
    user, group = _get_user_and_group(host)

    f = host.file('/etc/zuul')
    assert f.exists
    assert f.is_directory
    assert f.user == user
    assert f.group == group
    # TODO(pabelanger): Validate mode


def test_zuul_logs_directory(host):
    user, group = _get_user_and_group(host)

    f = host.file('/var/log/zuul')
    assert f.exists
    assert f.is_directory
    assert f.user == user
    assert f.group == group
    assert f.mode == 0o755


def test_zuul_executor_logging_config(host):
    user, group = _get_user_and_group(host)

    f = host.file('/etc/zuul/executor-logging.conf')
    assert f.exists
    assert f.is_file
    assert f.user == user
    assert f.group == group
    assert f.mode == 0o644


def test_zuul_executor_service_config(host):
    f = host.file('/etc/systemd/system/zuul-executor.service')
    assert f.exists
    assert f.is_file
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o644
    del f

    f = host.file('/etc/systemd/system/zuul-executor.service.d')
    assert f.exists
    assert f.is_directory
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o755
    del f

    f = host.file(
        '/etc/systemd/system/zuul-executor.service.d/override.conf')
    assert f.exists
    assert f.is_file
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o644


@pytest.mark.skip_if_docker()
def test_zuul_executor_service(host):
    service = host.service('zuul-executor')
    assert service.is_running
    assert service.is_enabled


def test_zuul_fingergw_logging_config(host):
    user, group = _get_user_and_group(host)

    f = host.file('/etc/zuul/fingergw-logging.conf')
    assert f.exists
    assert f.is_file
    assert f.user == user
    assert f.group == group
    assert f.mode == 0o644


def test_zuul_fingergw_service_config(host):
    f = host.file('/etc/systemd/system/zuul-fingergw.service')
    assert f.exists
    assert f.is_file
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o644
    del f

    f = host.file('/etc/systemd/system/zuul-fingergw.service.d')
    assert f.exists
    assert f.is_directory
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o755
    del f

    f = host.file(
        '/etc/systemd/system/zuul-fingergw.service.d/override.conf')
    assert f.exists
    assert f.is_file
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o644


@pytest.mark.skip_if_docker()
def test_zuul_fingergw_service(host):
    service = host.service('zuul-fingergw')
    assert service.is_running
    assert service.is_enabled


def test_zuul_merger_logging_config(host):
    user, group = _get_user_and_group(host)

    f = host.file('/etc/zuul/merger-logging.conf')
    assert f.exists
    assert f.is_file
    assert f.user == user
    assert f.group == group
    assert f.mode == 0o644


def test_zuul_merger_service_config(host):
    f = host.file('/etc/systemd/system/zuul-merger.service')
    assert f.exists
    assert f.is_file
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o644
    del f

    f = host.file('/etc/systemd/system/zuul-merger.service.d')
    assert f.exists
    assert f.is_directory
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o755
    del f

    f = host.file(
        '/etc/systemd/system/zuul-merger.service.d/override.conf')
    assert f.exists
    assert f.is_file
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o644


@pytest.mark.skip_if_docker()
def test_zuul_merger_service(host):
    service = host.service('zuul-merger')
    assert service.is_running
    assert service.is_enabled


def test_zuul_scheduler_logging_config(host):
    user, group = _get_user_and_group(host)

    f = host.file('/etc/zuul/scheduler-logging.conf')
    assert f.exists
    assert f.is_file
    assert f.user == user
    assert f.group == group
    assert f.mode == 0o644


def test_zuul_scheduler_service_config(host):
    f = host.file('/etc/systemd/system/zuul-scheduler.service')
    assert f.exists
    assert f.is_file
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o644
    del f

    f = host.file('/etc/systemd/system/zuul-scheduler.service.d')
    assert f.exists
    assert f.is_directory
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o755
    del f

    f = host.file(
        '/etc/systemd/system/zuul-scheduler.service.d/override.conf')
    assert f.exists
    assert f.is_file
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o644


@pytest.mark.skip_if_docker()
def test_zuul_scheduler_service(host):
    service = host.service('zuul-scheduler')
    assert service.is_running
    assert service.is_enabled


def test_zuul_web_logging_config(host):
    user, group = _get_user_and_group(host)

    f = host.file('/etc/zuul/web-logging.conf')
    assert f.exists
    assert f.is_file
    assert f.user == user
    assert f.group == group
    assert f.mode == 0o644


def test_zuul_web_service_config(host):
    f = host.file('/etc/systemd/system/zuul-web.service')
    assert f.exists
    assert f.is_file
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o644
    del f

    f = host.file('/etc/systemd/system/zuul-web.service.d')
    assert f.exists
    assert f.is_directory
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o755
    del f

    f = host.file(
        '/etc/systemd/system/zuul-web.service.d/override.conf')
    assert f.exists
    assert f.is_file
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o644


@pytest.mark.skip_if_docker()
def test_zuul_web_service(host):
    service = host.service('zuul-web')
    assert service.is_running
    assert service.is_enabled
