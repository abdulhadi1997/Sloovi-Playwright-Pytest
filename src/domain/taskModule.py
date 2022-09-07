class TaskModule:

    btnAddTask = '//button[@data-testid="add-task"]'
    lblTaskDescription = '//*[@for=":r1:"]/span'
    lblFirstTaskComponent = '(//div[@class="Task__description"])[1]'
    inpTaskDescription = '//input[@id=":r1:"]'
    lblDate = '//label[@for=":r0:"]'
    inpDate = '//input[@name="task_date"]'
    inpTime = '//input[@name="task_time"]'
    lblComponentHeader = '//h2[text()="Tasks"]'
    lblAssignUser = '//span[text()="Assign User"]'
    edpAssignUser = '//input[@id="assigned_user"]'
    btnCancel = '//button[@class="btn btn-link cancel-edit"]'
    btnSave = '//button[@class="btn btn-primary"]'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setTaskDescription(self, page, taskDescription):
        page.locator(self.inpTaskDescription).fill(taskDescription)

    def setDate(self, page, date):
        page.locator(self.inpDate).fill(date)

    def setTime(self, page, time):
        page.locator(self.inpTime).fill(time)

    def setAssignUser(self, page, user):
        page.locator(self.edpAssignUser).fill(user)
