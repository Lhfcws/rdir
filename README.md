## rdir
More powerful recursive dir. Support HTML pretty view in tree structure.

Pypi page: [https://pypi.python.org/pypi/rdir](https://pypi.python.org/pypi/rdir)

**0.40 Change Logs:**

1. User defined output path.
2. Tree pretty view in HTML supported!
3. Ignore the builtin types.


**Installation:**

You can install it in `pip` / `easy_install` now

        sudo pip install rdir
        sudo easy_install rdir

**Usage:**
  
Refer to `test.py` for example.
 
    rdir.rdir(obj_path_name, limit_deep = 2)
    
    
> Recursively show docs and structure of any object in the given module.

> rdir function will ignore protected or private members which start with "_".

    Args:
        name: string type, full name invocation like "pyquery.PyQuery.eq" or module "pyquery"
        limit_deep: int type, search deep limit, default is 2. -1 for unlimited.
        print_mode:
                TERM: it'll print out to your terminal with color;
                FILE: it'll print out to a file without color;
                # JAVADOC: it'll generate a Javadoc-style webpages;
                TREE: it'll generate a single webpage with tree structure to show the module;
                RETURN: it'll return an internal class RDirNode (not suggested).
        output: The output file path. Only works in mode FILE, TREE, JAVADOC.
                Default: current directory: '{$name}.rdir'
    Returns:
        RETURN mode: Return a root node of RDirNode.
        Others: nothing return.
