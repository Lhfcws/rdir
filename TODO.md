## TODO: version 0.50 route map

### Current problems (since 0.42)

1. PyDoc-style (LY)
2. Tree-style: more humanic UI (Lhfcws) 
3. Prompt a window with webkit to directly show the html.


### Data Format

rdir save the module's doc and structure as a tree-structure, so HTML generator may need to parse the structure.

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
