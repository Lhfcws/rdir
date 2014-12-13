## TODO: version 1.0 route map

### Current problems
 
> Sorted in priority
 
 1. The code is not so flexible.
 2. It should supports more than module, that is, working like `dir` to support any python objects.
 3. If I want to see more members in the deep layers, it is difficult or impossible due to the limited buffer of terminal.
 4. Give user a option to decide whether ignoring built-in modules or not (like os, sys, time, etc.).
  

### Todo

> Problem 3 in some way can be paralleled with Problem 1 and Problem 2.

 1. Fix Problem 1: change the POP code into OOP code (Lhfcws)
 2. Fix Problem 2: modify some internal codes to add the function. (Lhfcws)
 3. Fix Problem 3: write a HTML generator and templates (LY)
 4. Fix Problem 4: define a internal module list, try to cache the list, and modify some codes. (Whoever firstly finish the tasks above)

### Data Format

rdir save the module's doc and structure as a dict (tree-structure), so HTML generator may need to parse the dict.

key: name of object, i.e. "urllib2"
value: RdirNode



### Templates

> Both Javadoc-style and tree-style are needed to be done, but we may release a version first with any one of them is finished. 

 1. JavaDoc-like html.One page only contains the direct members and functions of the object(module, type, class ...) itself, and then user can click the object link to redirect to another object page
 2. Tree structure. Users are sometimes more likely to see a overview of the module. I suggest that just making a pretty print of the dict is fine. 

### Other requirments

> Code style: Google style  
> Code model: OOP  
> Write some annotations if necessary, at least those of a class or a module.  
