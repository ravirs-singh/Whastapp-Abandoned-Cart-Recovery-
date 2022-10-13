import pyautogui as pg
import webbrowser as web
import time
import pandas as pd
data = pd.read_csv('leads.csv')
data_dict = data.to_dict('list')
leads = data_dict['LeadNumber']
messages = data_dict['Message']
mes2 = data_dict['mes2']
mes3 = data_dict['mes3']
mes4 = data_dict['mes4']
combo = zip(leads,messages,mes2,mes3,mes4)
first = True
for lead,message,mes2,mes3,mes4 in combo:
    time.sleep(4)
    web.open("https://web.whatsapp.com/send?phone="+lead+"&text="+message +"           "+mes2+"             "+mes3+"           "+mes4)
    if first:
        time.sleep(2)
        first=False
    width,height = pg.size()
    pg.click(width/2,height/2)
    time.sleep(8)
    pg.press('enter')
    time.sleep(2)
    pg.hotkey('ctrl', 'w')
