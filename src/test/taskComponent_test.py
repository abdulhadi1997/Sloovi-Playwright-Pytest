import base64
import random
import string

import pytest
import src.domain.loginModule as LogInModule
import src.domain.taskModule as TaskModule
from pytest_html_reporter import attach
from playwright.sync_api import expect


@pytest.fixture(scope="function", autouse=True)
def resource(page):
    page.goto("/")
    print('*****SETUP*****')
    logIn = LogInModule.LoginPage()
    task = TaskModule.TaskModule()
    logIn.logIn(page)
    page.goto('https://stage.outreach.sloovi.com/lead/lead_7e0ce02cc9854ceeb61ea58bbae3f2b6')
    expect(page.locator(task.lblComponentHeader)).to_be_visible()
    page.locator(task.btnAddTask).click()
    yield "resource"

    print('******TEARDOWN******')
    if hasattr(page, '_outcome'):
        attach(data=base64.b64encode(page.screenshot()))


# 001 - Initial Presentation
def test_initialPresentation(page):
    task = TaskModule.TaskModule()

    expect(page.locator(task.lblComponentHeader)).to_contain_text('Tasks')
    expect(page.locator(task.lblTaskDescription)).to_contain_text('Task Description')
    expect(page.locator(task.lblDate)).to_contain_text('Date')
    expect(page.locator(task.lblAssignUser)).to_contain_text('Assign User')
    expect(page.locator(task.inpTaskDescription)).to_be_visible()
    expect(page.locator(task.inpDate)).to_be_visible()
    expect(page.locator(task.inpTime)).to_be_visible()
    expect(page.locator(task.btnCancel)).to_be_visible()
    expect(page.locator(task.btnSave)).to_be_visible()


# 002 - Persistence Cancel Task Component
def test_persistenceCancel(page):
    task = TaskModule.TaskModule()
    taskDescription = __randomizeName('persistenceCancelTest')

    page.locator(task.inpTaskDescription).fill('')
    task.setTaskDescription(page, taskDescription)
    task.setDate(page, '09/30/2022')
    task.setTime(page, '01:00am')
    task.setAssignUser(page, 'Saravanan C')
    page.locator(task.btnCancel).click()
    expect(page.locator(task.lblTaskDescription)).not_to_be_visible()

    expect(page.locator(task.lblFirstTaskComponent)).not_to_contain_text(taskDescription)


# 003 - Persistence Save Task Component
def test_persistenceSave(page):
    task = TaskModule.TaskModule()
    taskDescription = __randomizeName('persistenceSaveTest')

    page.locator(task.inpTaskDescription).fill('')
    task.setTaskDescription(page, taskDescription)
    task.setDate(page, '09/30/2022')
    task.setTime(page, '01:00am')
    task.setAssignUser(page, 'Saravanan C')
    page.locator(task.btnSave).click()
    expect(page.locator(task.lblTaskDescription)).not_to_be_visible()
    expect(page.locator(task.lblFirstTaskComponent)).to_contain_text(taskDescription)


# Helper Methods

def __randomizeName(name):
    return name + "".join(random.choices(string.ascii_uppercase + string.digits, k=5))
