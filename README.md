# Ansible Role: Memcached

Installs and configures memcached server

## Requirements

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

    ansible_memcached_port: "11211"

Sets port for memcached.

    ansible_memcached_user: "memcached"

Sets user for memcached.

    ansible_memcached_max_conn: "1024"   

Sets max connections count per memcached instance.

    ansible_memcached_cache_size: "64"

Sets cache size for memcached. In MB.

    ansible_memcached_listen_ip: "127.0.0.1"

Sets IP for listen.

    ansible_memcached_options: "-l {{ ansible_memcached_listen_ip }}"

Sets options, by default only `listen` directive.

    ansible_memcached_open_port: false

Allow remote connections to memcached. Work only if `ansible_memcached_open_port` is not `127.0.0.1` and `firewalld` is installed. Opens both TCP and UDP.

## Dependencies


## Example Playbook

    - hosts: servers
      roles:
        - cyber01.ansible-role-memcached


## License

MIT / BSD

## Author Information

This role was created in 2019 by [Sergey Brovko](http://cyber01.ru/).
