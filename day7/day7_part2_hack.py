import re
with open("day7input") as open_file:
  data = open_file.read().splitlines()

node_map = {}
node_values = {}
for line in data:
    p_node = re.match(r'[\w]+', line).group(0)
    node_value = re.search(r'[\d]+', line).group(0)
    node_values[p_node] = int(node_value)
    if re.search(r'->', line):
        nodes = re.search(r'-> (?P<nodes>[\w, ]+)', line).group('nodes').replace(' ', '').split(',')
        node_map[p_node] = nodes


def child_values(node):
    children = node_map[node]
    supports = []
    for child in children:
        if child in node_map.keys():
            child_support = child_values(child)
            value = sum(child_support) + node_values[child]
        else:
            value = node_values[child]
        supports.append(value)   
    if len(set(supports)) != 1:
        print ('Imbalance detected on {}, due to children {}, weighing {}'.format(node, node_map[node], supports))
    return supports 
child_values('gynfwly')
