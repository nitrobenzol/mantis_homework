def test_add_project(app):
    # getting list of all projects (old_projects)
    old_projects = app.project.get_projects_list()
    print(old_projects)
    # app.project.add_new_project(name="Kekwoodsky", description="Kekogradsky")
    # getting list of all projects (new_projects)
    # assert!
