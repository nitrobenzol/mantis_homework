import uuid
from model.project import Project


def test_add_project(app):
    project = Project(name=str(uuid.uuid4()), description=str(uuid.uuid4()))
    old_projects = app.project.get_projects_list()
    app.project.add_new_project(project)
    new_projects = app.project.get_projects_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)