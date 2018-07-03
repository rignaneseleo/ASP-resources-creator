## Do you have many strings in your ASP project to put in Resources?
This script makes it fast!

## HOW TO
Set the resx file path and the languages you need in the arrays:

### Setup
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

### Execution
+ Run the script (you need Python ofc):

`py script.py`

+ Insert the string you want to add:

![alt text][1]

+ The camelcase key is creted:

![alt text][2]

+ Since the key is not already in the file, it asks you where you want to add the string:

![alt text][3]

+ The string is added and some useful snippets are provided:

![alt text][4]

+ In visual studio with ResX Manager you can see the added resource:

![alt text][5]

#########################################

+ If you try to add again the string, it founds the string in the resources and gives you only the snippets to use it:

![alt text][6]

[1]: https://raw.githubusercontent.com/rignaneseleo/ASP-resources-creator/master/screen/1.PNG "Give an input string"
[2]: https://raw.githubusercontent.com/rignaneseleo/ASP-resources-creator/master/screen/2.PNG "ResourceKey"
[3]: https://raw.githubusercontent.com/rignaneseleo/ASP-resources-creator/master/screen/3.PNG "Choose the resource"
[4]: https://raw.githubusercontent.com/rignaneseleo/ASP-resources-creator/master/screen/4.PNG "Snippets"
[5]: https://raw.githubusercontent.com/rignaneseleo/ASP-resources-creator/master/screen/5.PNG "ResX Manager check"
[6]: https://raw.githubusercontent.com/rignaneseleo/ASP-resources-creator/master/screen/6.PNG "Resource already present"


## Possible Improvements
1. If you give a long string input, it generates a long resource key as well
2. It could also search by the given string (and not only by the resource key)
