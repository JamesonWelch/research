
import json

print('Select data point to sort by: ')
sel = str(input('\'a\' for 30 days\n\'b\' for 90 days\n\'c\' for 365 days: '))
sel = sel.lower()
if sel == 'a':
    day = '30d'
elif sel == 'b':
    day = '90d'
elif sel == 'c':
    day = '365d'

def install_sort(package):
    return package['analytics'][day]

with open('package_info.json', 'r') as f:
    data = json.load(f)

# Sort by description
# data = [item for item in data if 'video' in item['desc']]
data.sort(key=install_sort, reverse=True)

data_str = json.dumps(data[:5], indent=2)
print(data_str)
