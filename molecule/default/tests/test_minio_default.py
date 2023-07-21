import os
import yaml
import pytest
import testinfra.utils.ansible_runner


"""Role testing files using testinfra."""

# Check if host file exists
def test_hosts_file(host):
    """Validate /etc/hosts file."""
    f = host.file("/etc/hosts")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

# check if minio service has started
def test_minio_service(host):

    s = host.service('minio')
    assert s.is_running
    assert s.is_enabled
