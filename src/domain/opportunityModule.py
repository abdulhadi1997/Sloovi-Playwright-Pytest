import time

from playwright.sync_api import expect


class OpportunityModule:
    btnAddOpportunity = '//div[contains(@class,"Opportunities")]//*[@data-testid="add-undefined"]'
    btnCancel = '//button[@class="Button btn btn-link"]'
    btnSave = '//button[@class="Button btn btn-primary"]'
    lblOpportunityHeader = '//div[contains(@class,"Opportunities")]//h2'
    lblStatus = '//span[text()="Status"]'
    inpStatus = '//div[@class="OpportunityEditForm_status"]//input'
    lblEstimatedClose = '//span[text()="Estimated Close"]'
    inpEstimatedClose = '//div[@class="OpportunityEditForm_shrinkItem"]//div[@class="InputField__fieldContainer"]//input'
    lblConfidence = '//span[@class="RangeInput_FormikRangeInput_label_1e0"]'
    valueConfidence = '//span[@class="RangeInput_FormikRangeInput_perc_845"]'
    scrollerConfidence = '//input[@name="confidence"]'
    lblValue = '//span[text()="Value"]'
    inpValue = '//input[@name="value"]'
    edpValue = '//div[@class="EditForm_valuePeriod__iTfOV"]//input[@type="search"]'
    lblContact = '//span[text()="Contact"]'
    edpContact = '//div[@class="InputField InputField--small"]//input[@placeholder="None"]'
    lblUser = '//span[text()="User"]'
    inpUser = '(//div[@class="InputField InputField--small"]//input[@type="search"])[2]'
    lblNotes = '//label[@for="msg"]/span'
    inpNote = '//textarea[@id="msg"]'

    lblStatusListName = '//small[@class="Select__selectedGroup"]'
    lblStatusSubListName = '//div[@class="OpportunityEditForm_status"]//span[@class="Select__selectedText"]'

    btnListOptionBoost = '//div[text()="boost"]/following-sibling::span'
    btnListOptionBaddo = '//div[text()="baddo"]/following-sibling::span'
    btnListOptionSales = '//div[text()="Sales"]/following-sibling::span'

    subListOptionBads = '//div[text()="bads"]'
    subListOptionName = '//div[text()="name"]'
    subListoptionDemoCompleted = '//div[text()="Demo Completed"]'

    lblOpportunityName = '//div[@class="Opportunity__name"]'
    lblOpportunityDate = '//div[@class="Opportunity__confidenceAndDate"]'
    lblOpportunityStatus = '//span[@class="Opportunity__statusText"]'
    lblOpportunityNote = '//div[@class="Opportunity__detail"]'
    lblOpportunityContact = '//div[@class="Opportunity__contactName"]'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def resetStatusComponent(self, page):
        if page.is_visible(self.subListOptionBads):
            time.sleep(0.5)
            page.locator(self.btnListOptionBoost).click()

        if page.is_visible(self.subListOptionName):
            time.sleep(0.5)
            page.locator(self.btnListOptionBaddo).click()

        if page.is_visible(self.subListoptionDemoCompleted):
            time.sleep(0.5)
            page.locator(self.btnListOptionSales).click()

    def setConfidence(self, page, confidence):
        slider = page.locator(self.scrollerConfidence)
        # self.driver.execute_script("arguments[0].setAttribute('value','" + confidence + "')", slider)

    def setStatus(self, page, listOption, subListOption):
        page.locator(self.inpStatus).click()
        self.resetStatusComponent(page)

        page.locator('//div[text()="' + listOption + '"]/following-sibling::span').click()
        page.locator('//div[text()="' + subListOption + '"]').click()

        expect(page.locator(self.lblStatusListName)).to_contain_text(listOption)
        expect(page.locator(self.lblStatusSubListName)).to_contain_text(subListOption)

    def setEstimatedClose(self, page, dayOfCurrentMonth):
        page.locator(self.inpEstimatedClose).click()
        page.locator("[aria-label=\"Friday\\, September " + dayOfCurrentMonth + "\\, 2022\"]").click()

    def setValue(self, page, amount, duration):
        page.locator(self.inpValue).fill('')
        page.locator(self.inpValue).fill(amount)

        page.locator(self.edpValue).click()
        page.locator('//li[@id="listId" and text()="' + duration + '"]').click()

    def setContact(self, page, contact):
        page.locator(self.edpContact).click()
        page.locator('//li[@id="listId" and text()="' + contact + '"]').click()

    def setUser(self, page, user):
        page.locator(self.inpUser).click()
        page.locator('//li[@id="listId"]/img[@alt="' + user + '"]').click()

    def setNote(self, page, note):
        page.locator(self.inpNote).fill(note)
