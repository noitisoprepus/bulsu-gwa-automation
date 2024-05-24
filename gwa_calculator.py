from playwright.sync_api import sync_playwright
import sys
import getpass

def login_and_scrape(username, password):
    grades = []
    weighted_grades = []
    total_units = 0

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://bulsu.priisms.online/auth/login')

        # Login
        page.get_by_placeholder("Username").locator('visible=true').fill(username)
        page.get_by_placeholder("Password").locator('visible=true').fill(password)
        page.get_by_role("button", name="Login").click()
        
        try:
            page.wait_for_selector(".tiles", timeout=5000)
        except Exception as e:
            print("An error has occured during Login. Make sure your username and password are correct.")
            browser.close()
            sys.exit("Terminating... Please try again.")
        
        # Scraping
        page.goto('https://bulsu.priisms.online/#student/grades')
        page.wait_for_selector("#acad-year-term")
        options = page.query_selector_all("#acad-year-term option")
        # Iterates through each academic term
        for option in options:
            term_value = option.get_attribute("value")
            page.select_option("#acad-year-term", value=term_value)
                
            # Fetch all grades and units per subject
            page.wait_for_selector("table.table")
            rows = page.query_selector_all("table.table tbody tr")
            for row in rows:
                subject_code = row.query_selector(":nth-match(td, 2)").text_content().strip()
                # PE and NSTP grades are not counted in the GWA
                if "PE" in subject_code or "NSTP" in subject_code:
                    continue
                units = int(row.query_selector(":nth-match(td, 4)").text_content().strip())
                grade = float(row.query_selector(":nth-match(td, 9)").text_content().strip())
                grades.append(grade)
                weighted_grades.append(grade * units)
                total_units += units

        browser.close()
        return grades, weighted_grades, total_units

def calculate_gwa(weighted_grades, total_units):
    # GWA Computation
    total_weighted_grades = sum(weighted_grades)
    computed_gwa = total_weighted_grades / total_units
    return computed_gwa

def check_latin_honors(computed_gwa, grades):
    honors = None
    if all(g <= 2 for g in grades) and computed_gwa <= 1.2:
        honors = "Summa Cum Laude"
    elif all(g <= 2.25 for g in grades) and 1.2 < computed_gwa <= 1.45:
        honors = "Magna Cum Laude"
    elif all(g <= 2.5 for g in grades) and 1.45 < computed_gwa <= 1.75:
        honors = "Cum Laude"
    return honors

if __name__ == "__main__":
    username = input("Enter your username: ")
    password = getpass.getpass(prompt="Enter your password: ")

    grades, weighted_grades, total_units = login_and_scrape(username, password)
    computed_gwa = calculate_gwa(weighted_grades, total_units)
    honors = check_latin_honors(computed_gwa, grades)

    # Output
    print("Your GWA is", round(computed_gwa, 4))
    if honors is not None:
        print("Congratulations! You are qualified for", honors)
    else:
        print("You're not qualified for Latin honors. Better luck next time :)")