import re
import os
import unidecode
import sys
from html import escape  # python 3.x


def get_camel_case_string(string):
    # I use @foo@ to mark variables inside strings
    string = re.sub("<[^>]*>", "", string.replace("@", ""))
    string = ''.join(e for e in string if e.isalnum() | e.isspace())
    return unidecode.unidecode(''.join(x for x in string.title() if not x.isspace()))


def get_file_name_from_path(string):
    return os.path.splitext(os.path.basename(string))[0]


def read_content_from_path(path):
    my_file = open(path, "r", encoding="utf8")
    file_content = my_file.read()
    my_file.close()
    return file_content


def add_content_to_file(path, file_content, content_to_add):
    # append the content before the </root> tag
    text = file_content.replace(
        "</root>", content_to_add + "\r\n</root>")
    my_file = open(path, "w", encoding="utf8")
    my_file.write(text)
    my_file.close()


resources_content = {}
# resources where to look for resource keys
resources = [
    r"C:\Users\lrignanese\Documents\Progetti\Aeroporto\branches\4_2_0\src\WebSite\App_GlobalResources\AeroportoResources.resx",
    r"C:\Users\lrignanese\Documents\Progetti\Aeroporto\branches\4_2_0\src\WebSite\App_GlobalResources\Validation.resx"
]
# languages of other resources where to add the resources
languages = [
    "it"
]

while 1:
    resource_name = ""

    # read the content of resources files
    for resource in resources:
        resources_content[resource] = read_content_from_path(resource)

    # get the string to replace
    string_to_replace = input('String to convert in a resource: ')
    resource_key = get_camel_case_string(string_to_replace)

    print()
    print("Generated resource key: '{0}' → {1}".format(
        string_to_replace, resource_key))

    # check if the resource key is present in any of the resources files
    for resource_path, resource_content in resources_content.items():
        if '"' + resource_key + '"' in resource_content:
            # it exists
            # save the resource file path
            resource_name = get_file_name_from_path(resource_path)
            print()
            print("Resource already present in " + resource_name)

    print()
    # if there is not, add it
    if resource_name is "":
        # chose in which one
        print("Where do you want to add this resource? ")
        for i in range(0, len(resources)):
            print(str(i) + ")   " + resources[i])
        i_resource_chosen = int(input('Index of resource: '))
        print()

        # if the index is valid
        if 0 <= i_resource_chosen < len(resources):
            # add the resource key in the main resource
            content_to_add = """\r\n<data name="{0}" xml:space="preserve"><value>{1}</value></data>""".format(
                resource_key, escape(string_to_replace))
            add_content_to_file(
                resources[i_resource_chosen], resources_content[resources[i_resource_chosen]], content_to_add)
            print("Resource correctly added in the main resource file.")

            # add the resource key in other resources
            for language in languages:
                other_resource = resources[i_resource_chosen].replace(
                    ".resx", ".{0}.resx".format(language))
                content_to_add = """\r\n<data name="{0}" xml:space="preserve"><value>#{1}#</value><comment>TODO: Translate</comment></data>""".format(
                    resource_key, escape(string_to_replace))
                content = read_content_from_path(other_resource)
                add_content_to_file(other_resource, content, content_to_add)
                print(
                    "Resource correctly added in the {0} resource file.".format(language))

            # save the resource file path
            resource_name = get_file_name_from_path(
                resources[i_resource_chosen])
        else:
            print("Error")
    print()

    if resource_name is not "":
        # here I wrote some way to get and use a resource
        print("You can get this resource using one of this snippets:")
        print()
        print("""\t<%$ Resources:{0}, {1} %>""".format(
            resource_name, resource_key))
        print()
        print("""\t<asp:Localize runat="server" Text="<%$ Resources:{0}, {1} %>" />""".format(
            resource_name, resource_key))
        print()
        print("""\t{0}.{1}""".format(resource_name, resource_key))
        print()
        print("""\t<%= Resources.{0}.{1}.Replace("@@",) %>""".format(
            resource_name, resource_key))

    print()
    print("******************************")
    print()
