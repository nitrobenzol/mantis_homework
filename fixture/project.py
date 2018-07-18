from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_manage_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/manage_overview_page.php"):
            wd.find_element_by_xpath("//a[@href='/mantisbt-2.15.0/manage_overview_page.php']").click()

    def open_manage_projects(self):
        wd = self.app.wd
        self.open_manage_page()
        if not wd.current_url.endswith("/manage_proj_page.php"):
            wd.find_element_by_xpath("//a[@href='/mantisbt-2.15.0/manage_proj_page.php']").click()

    def open_adding_project(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//button[@class='btn btn-primary btn-white btn-round']").click()

    def fill_project_details(self, name, description):
        wd = self.app.wd
        # add project name
        wd.find_element_by_xpath("//input[@id='project-name']").click()
        wd.find_element_by_xpath("//input[@id='project-name']").clear()
        wd.find_element_by_xpath("//input[@id='project-name']").send_keys(name)
        # select status - for now hardcoded to 'development'
        wd.find_element_by_name("status").click()
        wd.find_elements_by_xpath("//select[@id='project-status']/option")[0].click()
        # set to inherit global categories
        wd.find_element_by_xpath("//span[@class='lbl']").click()
        # select view status
        wd.find_element_by_name("view_state").click()
        # add description
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(description)
        # save this project
        wd.find_element_by_xpath("//input[@type='submit']").click()

    def add_new_project(self, project):
        wd = self.app.wd
        # self.open_manage_page()
        self.open_manage_projects()
        self.open_adding_project()
        self.fill_project_details(project.name, project.description)

    project_cache = None

    def get_projects_list(self):
        wd = self.app.wd
        # self.open_manage_page()
        self.open_manage_projects()
        self.project_cache = []
        for element in wd.find_elements_by_xpath("//tbody/tr")[:-1]:
            cells = element.find_elements_by_tag_name("td")
            name = cells[0].text
            # status = cells[1].text
            # enabled = cells[2].text
            # view_status = cells[3].text
            description = cells[4].text
            id = cells[0].find_element_by_tag_name("a").get_attribute("href")[70:]
            self.project_cache.append(Project(name=name, description=description, id=id))
        return self.project_cache

    def delete_project_by_id(self, id):
        wd = self.app.wd
        # self.open_manage_page()
        self.open_manage_projects()
        self.select_project_by_id(id)
        self.delete_project()

    def select_project_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[contains(@href, %s) and contains(@href, 'manage_proj_edit_page.php?project_id=')]" % id).click()

    def delete_project(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()