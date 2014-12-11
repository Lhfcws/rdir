## rdir

Recursively look up python module and documents.

You can install it in `pip` / `easy_install` now

        sudo pip install rdir
        sudo easy_install rdir

Refer to `test.py` for example.

**Usage:**  
 
    rdir.rdir(module.__name__, limit_deep = 2)
    
    
> Recursively show module's doc and structure.  
> This method will ignore built-in arttribute which start with "__".

Args:  
>        module: string type, module.__name__ like "sys" or "pyquery"  
>        limit_deep: int type, search deep limit, default is 3. -1 for unlimited.  

Returns:  
>        void.  
>        The content will be print to terminal.  