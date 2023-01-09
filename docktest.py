from playwright.sync_api import sync_playwright, expect
from time import sleep

url = 'https://dock.tech/'


def test_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)

        cookies_accept = page.locator('xpath=//button[@id="onetrust-accept-btn-handler"]')
        cookies_accept.click()
        sleep(1)

        translate_btn = page.locator('xpath=//*[@id="menu-menu-principal"]/div/div/div[1]')
        translate_btn.click()
        english_translation = page.locator('xpath=//*[@id="menu-menu-principal"]/div/div/div[2]/a[1]')
        english_translation.click()

        active_acc = page.locator('xpath=//*[@id="Wrapper"]/section[2]/div/div/div[1]/h2')
        expect(active_acc).to_contain_text("70")
        expect(active_acc).to_contain_text(" MILLION ACTIVE ACCOUNTS")

        annual_growth_rate = page.locator('xpath=//*[@id="Wrapper"]/section[2]/div/div/div[4]/h2')
        expect(annual_growth_rate).to_contain_text("45%")
        expect(annual_growth_rate).to_contain_text(" CAGR SINCE 2014")

        # form filling
        page.locator('xpath=//*[@id="lb-nome"]').fill('tester')
        page.locator('xpath=//*[@id="PhoneNumber2"]').fill('99999999999')
        page.locator('xpath=//*[@id="lb-email"]').fill('test@dock.com')
        page.locator('xpath=//*[@id="lb-empresanome"]').fill('Testing at Dock')
        page.locator('xpath=//*[@id="lb-site"]').fill('http://testing.dock/')
        page.locator('xpath=//*[@id="lb-setoratuacao"]').nth(0).select_option('Bancos / Bancos digitais')
        page.locator('xpath=//*[@id="lb-faturamento"]').nth(0).select_option('Até R$10 milhões')
        page.locator('xpath=//*[@id="lb-cargo"]').nth(0).select_option('Outro')
        page.locator('//*[@id="lb-idiomapreferencial"]').nth(0).select_option('Inglês')
        page.locator('xpath=//*[@id="lb-solucao"]').nth(0).select_option('Banking')
        page.locator('xpath=//*[@id="11119step-1"]/p/button[2]').click()

        page.locator('xpath=//*[@id="lb-dbEstimativa1"]').nth(0).select_option('Estimativa de 1.000 até 5.000 contas')
        page.locator('xpath=//*[@id="lb-dbEstimativa2"]').nth(0).select_option('Estimativa de 1.000 até 5.000 cartões')
        page.locator('xpath=//*[@id="lb-dbSobrenegocio"]').fill('Hi, there! This is just a testing message')
        page.locator('xpath=//*[@id="11119step-2"]/div[6]/input').click()
        
        print("successfully printed")
        
        browser.close()
        
        
