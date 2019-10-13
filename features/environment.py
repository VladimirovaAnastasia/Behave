import os

from selenium import webdriver

def before_all(context):
     print("Executing before all")

def before_feature(context, feature):
     print("Before feature\n")

#Scenario level objects are popped off context when scenario exits
def before_scenario(context,scenario):
    context.browser = webdriver.Chrome(executable_path=r"C:\Users\KRASAVA\Desktop\chromedriver.exe")
    print("Before scenario\n")

def after_scenario(context, scenario):
    print("scenario status" + scenario.status)
    if scenario.status == "failed":
        if not os.path.exists("failed_scenarios_screenshots"):
            os.makedirs("failed_scenarios_screenshots")
        os.chdir("failed_scenarios_screenshots")
        context.browser.save_screenshot(scenario.name + "_failed.png")
    context.browser.quit()

def after_feature(context,feature):
     print("\nAfter feature")

def after_all(context):
     print("Executing after all")


