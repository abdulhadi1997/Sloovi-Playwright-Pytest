import base64
import random
import string
import time

import pytest

import src.domain.loginModule as LogInModule
import src.domain.opportunityModule as OpportunityModule
import src.domain.taskModule as TaskModule
from pytest_html_reporter import attach
from playwright.sync_api import expect


@pytest.fixture(scope="function", autouse=True)
def resource(page):
    page.goto("/")
    print('*****SETUP*****')
    logIn = LogInModule.LoginPage()
    opportunity = OpportunityModule.OpportunityModule()

    logIn.logIn(page)
    page.goto('https://stage.outreach.sloovi.com/lead/lead_7e0ce02cc9854ceeb61ea58bbae3f2b6')
    expect(page.locator(opportunity.lblOpportunityHeader)).to_be_visible()
    page.locator(opportunity.btnAddOpportunity).click()
    page.mouse.wheel(0, 750)
    yield "resource"

    print('******TEARDOWN******')
    if hasattr(page, '_outcome'):
        attach(data=base64.b64encode(page.screenshot()))


# 001 - Initial Presentation
def test_initialPresentation(page):
    opportunity = OpportunityModule.OpportunityModule()

    expect(page.locator(opportunity.lblOpportunityHeader)).to_contain_text('Opportunities')
    expect(page.locator(opportunity.lblStatus)).to_contain_text('Status')
    expect(page.locator(opportunity.lblEstimatedClose)).to_contain_text('Estimated Close')
    expect(page.locator(opportunity.lblConfidence)).to_contain_text('Confidence')
    expect(page.locator(opportunity.lblValue)).to_contain_text('Value')
    expect(page.locator(opportunity.lblContact)).to_contain_text('Contact')
    expect(page.locator(opportunity.lblUser)).to_contain_text('User')
    expect(page.locator(opportunity.lblNotes)).to_contain_text('Notes')

    expect(page.locator(opportunity.inpStatus)).to_be_visible()
    expect(page.locator(opportunity.inpEstimatedClose)).to_be_visible()
    expect(page.locator(opportunity.scrollerConfidence)).to_be_visible()
    expect(page.locator(opportunity.inpValue)).to_be_visible()
    expect(page.locator(opportunity.edpValue)).to_be_visible()
    expect(page.locator(opportunity.edpContact)).to_be_visible()
    expect(page.locator(opportunity.inpUser)).to_be_visible()
    expect(page.locator(opportunity.inpNote)).to_be_visible()


# 002 - Persistence Cancel Opportunity Component
def test_persistenceCancel(page):
    opportunity = OpportunityModule.OpportunityModule()
    note = __randomizeString('Notes: ')

    opportunity.setStatus(page, 'baddo', 'name')
    opportunity.setEstimatedClose(page, '30')
    opportunity.setValue(page, '100000', 'Annual')
    opportunity.setContact(page, 'Saravanan')
    opportunity.setUser(page, 'Sundar Pichai')
    opportunity.setNote(page, __randomizeString(note))
    page.locator(opportunity.btnCancel).click()
    expect(page.locator(opportunity.lblStatus)).not_to_be_visible()
    expect(page.locator('//div[@class="Opportunity__detail" and contains(text(),"' + note + '")]')).not_to_be_visible()


# 003 - Persistence Save Opportunity Component
def test_persistenceSave(page):
    opportunity = OpportunityModule.OpportunityModule()
    note = __randomizeString('Notes: ')

    opportunity.setStatus(page, 'baddo', 'name')
    opportunity.setEstimatedClose(page, '30')
    opportunity.setValue(page, '100000', 'Annual')
    opportunity.setContact(page, 'Saravanan')
    opportunity.setUser(page, 'Sundar Pichai')
    opportunity.setNote(page, __randomizeString(note))
    page.locator(opportunity.btnSave).click()
    expect(page.locator(opportunity.lblStatus)).not_to_be_visible()
    expect(page.locator('//div[@class="Opportunity__detail" and contains(text(),"' + note + '")]')).to_be_visible()


# Helper Methods

def __randomizeString(name):
    return name + "".join(random.choices(string.ascii_uppercase + string.digits, k=5))
