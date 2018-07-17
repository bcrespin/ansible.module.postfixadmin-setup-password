#!/usr/bin/python

from ansible.module_utils.basic import *
import random
import time
import hashlib

def main():
       fields = { 
         "password": {"required": True, "type": "str" },
       }
       module = AnsibleModule(argument_spec=fields)
 
       myrand=str(random.randint(0, 55534)) + time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
       salt=hashlib.md5(myrand).hexdigest()
       hash=salt + ':' + hashlib.sha1(salt + ':' + module.params['password']).hexdigest()
       response = {"hash": hash }
       module.exit_json(changed=False, meta=response)


if __name__ == '__main__':
    main()
