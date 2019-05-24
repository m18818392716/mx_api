import yaml

def get_conf():
    with open ("config.yml", "r", encoding='utf-8') as f:
        cfg = f.read()
        dic = yaml.load(cfg)
        sender = dic['email']['sender']
        receiver = dic['email']['receiver']
        smtpserver = dic['email']['smtpserver']
        username = dic['email']['username']
        password = dic['email']['password']
        print(sender, receiver, smtpserver, username, password)
        return sender, receiver, smtpserver, username, password