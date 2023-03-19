from asyncore import read
from pickle import FALSE
import selenium
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from datetime import datetime, timedelta
import random




activityTypes_ = ["Development","Meeting"]
activityType_ = input("Input Activity Type: ")

if activityType_ in activityTypes_:
    asdasd= 9
else:
    print(f"The string '{activityType_}' exists in the list.")
    print(f"Permisible activites are {', '.join(activityTypes_)}")
# take input from the user for an array of numbers
taskNumbers = []

while True:
    num = input("Enter task number (or press enter to stop): ")
    if num == "":
        break
    else:
        taskNumbers.append(int(num))

# create a new array of strings with the format "#number"
formatted_task_numbers = ["#" + str(num) for num in taskNumbers]

# print the formatted array
print(formatted_task_numbers)




# get the current year
current_year = datetime.now().year

# prompt the user to enter the first date
date1_str = input("Enter the START date (MM-DD): ")
# combine the first date with the current year
startDate = datetime.strptime(f"{current_year}-{date1_str}", "%Y-%m-%d")

# prompt the user to enter the second date
date2_str = input("Enter the END date (MM-DD): ")
# combine the second date with the current year
endDate = datetime.strptime(f"{current_year}-{date2_str}", "%Y-%m-%d")

# print the dates
print("First date:", startDate.date())
print("Second date:", endDate.date())





driver = webdriver.Firefox(executable_path=r'C:\\Users\\blu3s\Desktop\\PlayGround\\SeleniumPlayGround\\GeckoDriver\\geckodriver.exe')
driver.get("https://dev.azure.com/gjirafadev/AdChef/_apps/hub/7pace.Timetracker.Monthly")
wait = WebDriverWait(driver, 20)
#driver.title.__contains__("Timetracker")
driver.maximize_window()

#loginEmail = driver.find_elements_by_name("loginfmt")[0]
loginEmail = wait.until(EC.element_to_be_clickable((By.NAME, 'loginfmt')))
loginEmail.click()
loginEmail.send_keys("faton.p@gjirafa.com")
#nextbutton= driver.find_element_by_id("idSIButton9")
nextbutton= wait.until(EC.element_to_be_clickable((By.ID, 'idSIButton9')))
nextbutton.click()
#passwordField = driver.find_elements_by_name("passwd")[0]
passwordField = wait.until(EC.element_to_be_clickable((By.NAME, 'passwd')))
passwordField.click()
passwordField.send_keys("Gjirafa123?")
#elem = driver.find_element_by_class_name("selectable-day")
#nextbutton= driver.find_element_by_id("idSIButton9")
nextbutton= wait.until(EC.element_to_be_clickable((By.ID, 'idSIButton9')))
nextbutton.click()

#--laterrrrrrrrrr
##check if its asking to stay signed in 
##elements = driver.find_elements_by_class_name("text-title")
##anywherestay = False


nextbutton= wait.until(EC.element_to_be_clickable((By.ID, 'idSIButton9')))
nextbutton= driver.find_element_by_id("idSIButton9")
nextbutton.click()





def getHourRanges():
    if activityType_ == "Meeting":
     ranges=[]
     now = datetime.now()
     time_string_from = "09:20 AM"
     time_string_to = "09:30 AM"
     time_obj_from = datetime.strptime(time_string_from, '%I:%M %p').time()
     time_obj_to = datetime.strptime(time_string_to, '%I:%M %p').time()
     # combine the date and time objects into a single datetime object
     date_time_obj_from = datetime.combine(now.date(), time_obj_from)
     date_time_obj_to = datetime.combine(now.date(), time_obj_to)
     ranges.append((date_time_obj_from, date_time_obj_to))
     return ranges
    # Set the date to generate time ranges for
    date_str = datetime.now().strftime("%Y-%m-%d")# input("Enter date (YYYY-MM-DD): ")
    date = datetime.strptime(date_str, "%Y-%m-%d")
    
    # Define the start and end times of the schedule
    schedule_start = datetime.combine(date, datetime.strptime("09:30", "%H:%M").time())
    schedule_end = datetime.combine(date, datetime.strptime("17:00", "%H:%M").time())
    
    # Define the start and end times of the break
    break_start = datetime.combine(date, datetime.strptime("11:00", "%H:%M").time())
    break_end = datetime.combine(date, datetime.strptime("11:45", "%H:%M").time())
    
    # Generate a list of possible start times
    possible_starts = []
    current_time = schedule_start
    while current_time < schedule_end:
        if current_time < break_start or current_time >= break_end:
            possible_starts.append(current_time)
        current_time += timedelta(minutes=15)
    
    # Randomly choose 3-4 start times until we fill the entire schedule
    num_ranges = random.randint(3, 4)
    ranges = []
    while len(ranges) < num_ranges and possible_starts:
        start_time = random.choice(possible_starts)
        possible_starts.remove(start_time)
        end_time = start_time + timedelta(minutes=random.randint(30, 150))
        if end_time >= break_start and start_time < break_end:
            end_time = break_start
        elif end_time > schedule_end:
            end_time = schedule_end
        ranges.append((start_time, end_time))
    
    # Sort the ranges by start time
    ranges.sort(key=lambda x: x[0])
    
    # Print the generated time ranges
    for start_time, end_time in ranges:
        print("{0} - {1}".format(start_time.strftime("%I:%M %p"), end_time.strftime("%I:%M %p")))
    return ranges



def getDateTaskPairing(tasks,startDate,endDate):
   
   # Sample range of consecutive dates
   start_date = startDate#date(2023, 2, 1)  # Start date (inclusive)
   end_date = endDate#date(2023, 2, 9)  # End date (inclusive)
   
   # Calculate number of days in the range
   num_days = (end_date - start_date).days + 1
   
   # Initialize list of dates
   dates_unfiltered = [start_date + timedelta(days=i) for i in range(num_days)]
   dates = [date for date in dates_unfiltered if date.weekday() not in [5, 6]]
   # Initialize dictionary to store pairs of tasks and dates
   task_date_pairs = {}
   
   # Assign tasks to consecutive dates
   current_task = 0
   for date in dates:
       task = tasks[current_task]
       if task not in task_date_pairs:
           task_date_pairs[task] = [date]
       else:
           task_date_pairs[task].append(date)
       current_task = (current_task + 1) % len(tasks)
   
   # Print task-date pairs
   """for task, dates in task_date_pairs.items():
       for date in dates:
           print(task + ': ' + str(date))"""
   return task_date_pairs








# dayElement = driver.find_elements_by_class_name("selectable-day")
# day112= driver.find_element_by_class_name("selectable-day")
#dd=driver.find_element_by_css_selector('.month-calendar-column.month-calendar-week-day.selectable-day[data-m="2"][data-d="1"]')

tasksDatesPairings = getDateTaskPairing(taskNumbers,startDate,endDate);

frameget=wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'external-content--iframe')))
driver.switch_to.frame(frameget)
wait = WebDriverWait(driver, 30)

for task, dates in tasksDatesPairings.items():
    for date in dates:
        timeRanges = getHourRanges()
        ## d4d=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-m="2"][data-d="1"][data-y="2022"]')))

        locatedLoad1 = driver.find_elements_by_xpath( "//*[@id='ajaxLoaderLoader'][@style='display: none;']")
        if locatedLoad1:
         jj=0
        else :
         aaaaaaawait= wait.until_not(EC.presence_of_element_located((By.XPATH, "//*[@id='ajaxLoaderLoader'][not(@style='display: none;')]")))

        aaaaaaawait= wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'month-calendar-week')))
        elements = driver.find_elements_by_class_name("month-calendar-week")
        specificDay = driver.find_element_by_css_selector(f"div[data-m='{date.month}'][data-d='{date.day}'][data-y='{date.year}']")
        hover = ActionChains(driver).move_to_element(specificDay)
        hover.perform()
        clickToAddTime = specificDay.find_elements_by_class_name("ms-Icon--Add")
        specificDay.click()
        for start_time, end_time in timeRanges:
            locatedLoad = driver.find_elements_by_xpath( "//*[@id='ajaxLoaderLoader'][@style='display: none;']")
            if locatedLoad:
             jj=0
            else :
             aaaaaaawait= wait.until_not(EC.presence_of_element_located((By.XPATH, "//*[@id='ajaxLoaderLoader'][not(@style='display: none;')]")))
            aaaaaaawait= wait.until(EC.element_to_be_clickable((By.ID, 'btnAddCurrent')))
            element = driver.find_element_by_id("btnAddCurrent")
            element.click()

            ##modal operations 
            aaaaaaawait= wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'add-time-dialog')))
            modal  = driver.find_element_by_class_name("add-time-dialog")
            ## add the task number -> wait for it to appear in dropdown -> click it 
            tasknumberfield = modal.find_element_by_class_name("wi-search-input")
            ##tasknumberfield.click()
            tasknumberfield.send_keys(f"{task}")

            aaaaaaawait= wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ms-Suggestions-container')))
            aaaaaaawait= wait.until(EC.presence_of_element_located((By.XPATH, f"//span[contains(text(), '#{task}')]")))
            
            taskNumber = modal.find_element_by_xpath(f"//span[contains(text(), '#{task}')]")
            taskButton = taskNumber.find_element_by_xpath("./ancestor::button")
            taskNumber.click()


            ##time from 
            timeFrom = modal.find_element_by_class_name("timeframe-from")
            timeFrom.clear()
            timeFrom.click()

            #timeFrom.send_keys(start_time.strftime("%I:%M %p"))

            timeFrom.send_keys(Keys.ARROW_LEFT)
            timeFrom.send_keys(Keys.ARROW_LEFT)
            timeFrom.send_keys(start_time.strftime("%I"))

            timeFrom.send_keys(Keys.ARROW_LEFT)
            timeFrom.send_keys(Keys.ARROW_LEFT)
            timeFrom.send_keys(Keys.ARROW_RIGHT)
            timeFrom.send_keys(start_time.strftime("%M"))

            timeFrom.send_keys(Keys.ARROW_LEFT)
            timeFrom.send_keys(Keys.ARROW_LEFT)
            timeFrom.send_keys(Keys.ARROW_RIGHT)
            timeFrom.send_keys(Keys.ARROW_RIGHT)
            timeFrom.send_keys(start_time.strftime("%p"))
            

            ##time to 
            timeTo= modal.find_element_by_class_name("timeframe-to")
            timeTo.clear()
            timeTo.click()


            timeTo.send_keys(Keys.ARROW_LEFT)
            timeTo.send_keys(Keys.ARROW_LEFT)
            timeTo.send_keys(end_time.strftime("%I"))

            timeTo.send_keys(Keys.ARROW_LEFT)
            timeTo.send_keys(Keys.ARROW_LEFT)
            timeTo.send_keys(Keys.ARROW_RIGHT)
            timeTo.send_keys(end_time.strftime("%M"))

            timeTo.send_keys(Keys.ARROW_LEFT)
            timeTo.send_keys(Keys.ARROW_LEFT)
            timeTo.send_keys(Keys.ARROW_RIGHT)
            timeTo.send_keys(Keys.ARROW_RIGHT)
            timeTo.send_keys(end_time.strftime("%p"))


            #timeTo.send_keys(end_time.strftime("%I:%M %p"))#'10:01 PM')
            ##activity type 



            activityDropDown = modal.find_element_by_class_name("activity-type-selected")
            activityDropDown.click()
            aaaaaaawait= wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'add-time-activity-type-dropdown')))
            dropDownOptionsContainer = modal.find_element_by_class_name("add-time-activity-type-dropdown")
            aaaaaaawait= wait.until(EC.presence_of_element_located((By.XPATH, f"//span[contains(text(), '{activityType_}')]")))
            optionText = dropDownOptionsContainer.find_element_by_xpath(f"//button//span[contains(text(), '{activityType_}')]")
            option = optionText# optionText.find_element_by_xpath("./ancestor::button[1]")
            option.click()
            ##click save 
            savebutton = modal.find_element_by_class_name("ms-Icon--Save")
            savebutton.click()

            ## wait for modal to disappear 
            aaaaaaawait= wait.until_not(EC.presence_of_element_located((By.CLASS_NAME, 'add-time-dialog')))

















