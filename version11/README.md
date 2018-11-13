# Bazaar v0.09

## File Structure

'common.py' is where we define variables that need to be shared between modules. Namely, the number of agents, the size of the screens (needed for both agent calculations and initializing windows), etc.

'agent.py' is where we define the behavior of the agents movement, and what functions to call when they enter each others' interaction radii.

'data.py' is where we handle the bulk of the data being given back to us by our agents, and begin drawing graphs, formatting trade agreements, etc.

'name.py' is the module for generating names.

'resources.py' handles importing files.

'util.py' and 'vector2.py' contain a few key functions we need for calculating movement and distance between agents.

'main.py' draws on all of these to execute the main gameloop.

## Importing Packages

There are many different ways to import packages in python:

```python
import package.a           # Absolute import
import package.a as a_mod  # Absolute import bound to different name
from package import a      # Alternate absolute import
import a                   # Implicit relative import (deprecated, py2 only)
from . import a            # Explicit relative import
```