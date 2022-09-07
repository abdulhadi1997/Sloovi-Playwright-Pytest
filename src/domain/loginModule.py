from playwright.sync_api import expect


class LoginPage:
    btnCreateAccount = '//a[@class="btn"]'
    btnSignIn = '//button[@class="btn btn-primary"]'
    inpEmail = '//input[@type="email"]'
    inpPassword = '//input[@type="password"]'
    lblEmail = '//span[text()="Email Address"]'
    lblLogInPrompt = '//h2[text()="Please log in to your account"]'
    lblPassword = '//span[text()="Password"]'
    lnkForgotPassword = '//a[@href="/forgot"]'
    inpUsername = '//input[@type="email"]'
    lblUserNameOnDashboard = '//span[@class="OrganizationDropdown_organizationName"]'
    lblForgotPassword = '//h2[text()="Forgot your password?"]'
    lblCreateAccountHeader = '//h2[@class="Login__title"]'
    lblCreateAccountFooter = '//div[@class="terms"]'
    lblValidationError = '//div[@class="Message-danger alert alert-block alert-danger Message--withMargin"]'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def logIn(self, page):
        page.locator(self.inpUsername).fill('smithwills1989@gmail.com')
        page.locator(self.inpPassword).fill('12345678')
        page.locator(self.btnSignIn).click()
        expect(page.locator(self.lblUserNameOnDashboard)).to_be_visible()
