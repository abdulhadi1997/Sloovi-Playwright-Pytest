import base64

import pytest
from pytest_html_reporter import attach
from playwright.sync_api import expect

import src.domain.loginModule as LoginModule


@pytest.fixture(scope="function", autouse=True)
def resource(page):
    page.goto("/")
    print('*****SETUP*****')
    yield "resource"
    print('******TEARDOWN******')
    if hasattr(page, '_outcome'):
        attach(data=base64.b64encode(page.screenshot()))


# 001 - Initial Presentation
def test_initialPresentation(page):
    loginPage = LoginModule.LoginPage()

    page.locator(loginPage.btnCreateAccount).is_visible()
    page.locator(loginPage.btnSignIn).is_visible()
    page.locator(loginPage.inpEmail).is_visible()
    page.locator(loginPage.inpPassword).is_visible()
    page.locator(loginPage.lblEmail).is_visible()
    page.locator(loginPage.lblLogInPrompt).is_visible()
    page.locator(loginPage.lblPassword).is_visible()
    page.locator(loginPage.lnkForgotPassword).is_visible()


# 002 - Forgot Password
def test_ForgotPassword(page):
    loginPage = LoginModule.LoginPage()

    page.locator(loginPage.lnkForgotPassword).click()

    expect(page.locator(loginPage.lblForgotPassword)).to_contain_text('Forgot your password?')


# 003 - Click Create Account Button
def test_createAccount(page):
    loginPage = LoginModule.LoginPage()
    txtHeader = 'Sloovi Outreach more deals.'
    txtFooter = 'By signing up, you agree to our Terms of Service and Privacy Notice.This page is\nprotected by reCAPTCHA and the Google Privacy Policyand Terms of Service apply.'

    page.locator(loginPage.btnCreateAccount).click()

    expect(page.locator(loginPage.lblCreateAccountHeader)).to_contain_text(txtHeader)
    expect(page.locator(loginPage.lblCreateAccountFooter)).to_contain_text(txtFooter)


# 004 - Submit With Incorrect Email Address
def test_submitIncorrectEmail(page):
    loginPage = LoginModule.LoginPage()

    page.locator(loginPage.btnSignIn).click()

    expect(page.locator(loginPage.lblUserNameOnDashboard)).not_to_be_visible()

    page.locator(loginPage.inpUsername).fill('smithwills1989')
    page.locator(loginPage.btnSignIn).click()

    expect(page.locator(loginPage.lblUserNameOnDashboard)).not_to_be_visible()

    page.locator(loginPage.inpUsername).fill('smithwills1989@')
    page.locator(loginPage.btnSignIn).click()

    expect(page.locator(loginPage.lblUserNameOnDashboard)).not_to_be_visible()


# 005- Submit With Incorrect Password
def test_submitIncorrectPassword(page):
    loginPage = LoginModule.LoginPage()

    page.locator(loginPage.inpUsername).fill('smithwills1989@gmail.com')
    page.locator(loginPage.btnSignIn).click()

    expect(page.locator(loginPage.lblUserNameOnDashboard)).not_to_be_visible()

    page.locator(loginPage.inpPassword).fill('87654321')
    page.locator(loginPage.btnSignIn).click()

    expect(page.locator(loginPage.lblUserNameOnDashboard)).not_to_be_visible()
    expect(page.locator(loginPage.lblValidationError)).to_contain_text("The email address or password was incorrect.")


# 006 - Log In To Dashboard
def test_submitCorrectCredentials(page):
    loginPage = LoginModule.LoginPage()

    page.locator(loginPage.inpUsername).fill('smithwills1989@gmail.com')
    page.locator(loginPage.inpPassword).fill('12345678')
    page.locator(loginPage.btnSignIn).click()
    page.locator(loginPage.lblUserNameOnDashboard).is_visible()
