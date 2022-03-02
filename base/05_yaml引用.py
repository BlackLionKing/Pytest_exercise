import yaml
with open('../data/test_yaml.yml') as f:
    print(yaml.safe_load(f))


"""
    输出
        defaults
            IP: 172.168.6.102
            Host: 8888
        dev
            IP: 172.168.6.102
            Host: 8888
            database: dev_db
        test
            IP: 172.168.6.102
            Host: 8888
            database: test_db
"""
