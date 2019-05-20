import pytest
import os
import yaml
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

@pytest.fixture()
def AnsibleDefaults():
    with open("../../defaults/main.yml", 'r') as stream:
        return yaml.load(stream)


@pytest.mark.parametrize("files", [
    "/etc/sysconfig/memcached"
])
def test_files(host, files):
    f = host.file(files)
    assert f.exists
    assert f.is_file


def test_user(host):
    assert host.group("memcached").exists
    assert host.user("memcached").exists


def test_service(host):
    s = host.service("memcached")
    assert s.is_enabled
    assert s.is_running


def test_socket(host, AnsibleDefaults):
    listen = AnsibleDefaults['ansible_memcached_listen_ip']
    s = host.socket("tcp://" + listen + ":11211")
    assert s.is_listening
