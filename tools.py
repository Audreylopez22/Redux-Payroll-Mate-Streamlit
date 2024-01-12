import streamlit as st
import datetime
from openpyxl.styles import NamedStyle
from streamlit.web.server.websocket_headers import _get_websocket_headers 
from urllib.parse import unquote
from datetime import datetime

def log_message(message):
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    st.text(f"[{formatted_time}] {message}")
    
def get_or_create_money_style(workbook):
    money_style_name = 'money'
    
    # # Check if the 'money' style already exists
    for style in workbook._named_styles:
        if style.name == money_style_name:
            return style

    # If it does not exist, create and add the style 'money'.
    money_style = NamedStyle(name=money_style_name, number_format='"$"#,##0.00')
    workbook.add_named_style(money_style)
    
    return money_style

def get_all_cookies():
    headers = _get_websocket_headers()
    if headers is None:
        return {}
    
    if 'Cookie' not in headers:
        return {}
    
    cookie_string = headers['Cookie']
    cookie_kv_pairs = cookie_string.split(';')
    
    cookie_dict = {}

    for kv in cookie_kv_pairs:
        k_and_v = kv.split('=')
        k = k_and_v[0].strip()
        v = k_and_v[1].strip()
        cookie_dict[k] = unquote(v) 
        
    return cookie_dict

