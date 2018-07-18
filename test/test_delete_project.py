import uuid
import random
from model.project import Project


def test_add_project(app):
    project = Project(name=str(uuid.uuid4()), description=str(uuid.uuid4()))
    if len(app.project.get_projects_list()) == 0:
        app.project.add_new_project(project)
    old_projects = app.project.get_projects_list()
    random_project = random.choice(old_projects)
    app.project.delete_project_by_id(random_project.id)
    new_projects = app.project.get_projects_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(random_project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
