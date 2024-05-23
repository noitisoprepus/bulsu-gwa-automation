from playwright.sync_api import sync_playwright
import getpass

# Get login credentials
username = input("Enter your username: ")
password = getpass.getpass(prompt="Enter your password: ")

weighted_grades = []
total_units = 0

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://bulsu.priisms.online/')

    # Login and go to Grades
    page.get_by_placeholder("Username").locator('visible=true').fill(username)
    page.get_by_placeholder("Password").locator('visible=true').fill(password)
    page.get_by_role("button", name="Login").click()
    page.goto('https://bulsu.priisms.online/#student/grades')

    # Iterates through each academic term
    page.wait_for_selector("#acad-year-term")
    options = page.query_selector_all("#acad-year-term option")
    no_honors = False
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
            if grade >= 2.75:
                no_honors = True
            weighted_grade = grade * units
            weighted_grades.append(weighted_grade)
            total_units += units
           
           
    


    # GWA Computation
    total_weighted_grades = 0
    for g in weighted_grades:
        total_weighted_grades += g
    computed_gwa = total_weighted_grades / total_units
    
    #Latin Honors
    honors = ''
    
    if computed_gwa <=1.2:
        honors = 'Summa Cum Laude'
    elif 1.2 <= computed_gwa <= 1.45:
        honors = 'Magna Cum Laude'
    elif 1.45 <= computed_gwa <=1.75:
        honors = 'Cum Laude'
    else:
        nt = "Better Luck Next Time :()"
    
    # Output
    print("Your GWA is ", round(computed_gwa, 4))
    if no_honors is False:
        print ("Congrats you are:", honors)
    else:
        print(nt)
    

    browser.close()