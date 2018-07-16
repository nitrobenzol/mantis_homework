class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_manage_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[@href='/mantisbt-2.15.0/manage_overview_page.php']").click()

    def open_manage_projects(self):
        wd = self.app.wd
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

    def add_new_project(self, name, description):
        wd = self.app.wd
        self.open_manage_page()
        self.open_manage_projects()
        self.open_adding_project()
        self.fill_project_details(name, description)