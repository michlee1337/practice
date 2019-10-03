from collections import defaultdict

def buildOrder(projects, dependencies):
    # build hash map (dict) of dependencies
    dependency_dictionary = defaultdict(list)
    for dependency in dependencies:
        dependency_dictionary[projects.index(dependency[1])].append(projects.index(dependency[0])) # store by index for easy manipulation

    # bit vector to track installed projects and processed projects
    installed = [0 for _ in enumerate(projects)]
    processed = [0 for _ in enumerate(projects)]

    # install order to return
    install_order = []

    for project, _ in enumerate(projects):
        # install all dependencies
        if installed[project] == 0:
            sub_order, installed, processed = installProject(project, dependency_dictionary, processed, installed)
            install_order += sub_order

    # return order translated back to projects
    return([projects[i] for i in install_order])

def installProject(project, dependency_dictionary, processed, installed):
    processed[project] = 1
    install_order = []
    for dependency in dependency_dictionary[project]:
        if installed[dependency]:
            pass
        elif processed[dependency]:
            raise ValueError('Dependency loop exists. Cannot be installed.')
        else:
            sub_order, installed, processed = installProject(dependency, dependency_dictionary, processed, installed)
            install_order += sub_order
    install_order.append(project)
    installed[project] = 1
    return(install_order, installed, processed)

if __name__=="__main__":
    print(buildOrder(['a','b','c','d','e','f'], [('a','d'),('f','b'),('b','d'),('f','a'),('d','c')]))
