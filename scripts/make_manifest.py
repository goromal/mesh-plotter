import os
import json

versionRaw = {}
root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
with open(os.path.join(root, 'mesh_plotter', '__version__.py')) as f:
    exec(f.read(), versionRaw)

versionInfo = {
    'pname': versionRaw['__title__'],
    'version': versionRaw['__version__']
}

print(json.dumps(versionInfo, indent=4))
