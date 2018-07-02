## Do you have many strings in your ASP project to put in Resources?
This script makes it fast!

## HOW TO
Set the resx file path and the languages you need in the arrays:

*EXAMPLE*:
```
# resources where to look for resource keys
resources = [
    r"C:\Users\user\Documents\projects\X\src\WebSite\App_GlobalResources\Resource1.resx",
    r"C:\Users\user\Documents\projects\X\src\WebSite\App_GlobalResources\Resource2.resx",
]
# languages of other resources where to add the resources
languages = [
    "it"
]
```

Run the script (you need Python ofc):
`py script.py`
