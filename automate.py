import win32com.client
from time import sleep

ie = win32com.client.Dispatch("InternetExplorer.Application") #An object is created
ie.Visible = 1
ie.navigate("https://www.google.com/")

while ie.ReadyState != 4: # Wait for browser to finish loading
    sleep(1)
print("Webpage Loaded")  #web page loaded
ie.Visible =1
ie.navigate("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

page = ie.Document 

links = page.links
