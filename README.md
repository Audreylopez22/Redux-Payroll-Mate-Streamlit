# Welcome to Redux Payroll Mate

**Table of Contents**

#Introduction
The Excel file processing application is a tool designed to streamline the manipulation of data contained in Excel files. It utilizes Streamlit for the user interface and Openpyxl for data processing.

##Streamlit
Streamlit is an open-source framework that makes it easy to create web applications for data analysis and interactive prototypes. With Streamlit, developers can effortlessly turn Python scripts into web applications.

###  Key Features of Streamlit
**1. Simplicity:** With just a few Python commands, it's possible to create interactive interfaces without the need for web development expertise.
**2. Dynamic Updates: **Interface elements automatically update when data or parameters change.
**3. Easy Integration**: Easily integrates with popular libraries such as Pandas, Plotly, and Matplotlib for data visualization.

##Openpyxl
Openpyxl is a Python library that allows reading and writing Excel files in xlsx format. With Openpyxl, it's possible to programmatically manipulate spreadsheets, cells, and data.

###  Key Features of Openpyxl
**1. Read and Write:** Enables reading and writing of data in Excel files.
**2. Spreadsheet Manipulation:** Facilitates the creation, duplication, and deletion of spreadsheets.
**3. Cell Formatting:** Allows formatting cells, such as styles, colors, and formulas.

#System Requirements
This application requires the following libraries in the following versions to operate.

`$ npm install streamlit==1.29.0`

`$ npm install openpyxl==3.1.2`

`$ npm install plotly==5.18.0`

`$ npm install formulas==1.2.7`

`$ npm install streamlit-authenticator==0.1.5`


It is crucial to note that version 0.1.5 of streamlit-authenticator should be used, as an issue with authentication has been identified when using the latest version (version="0.2.3") in the online application. In the event of considering a future update, it is recommended to test the new version beforehand to ensure that any issues associated with the latest version have been resolved.

#Docker prerequisites
NodeJS: 19.6.0

#Create Docker containers on Windows

Run the following commands in PowerShell from the root of the repository.

`$Env:DATE=$(get-date -Format "yyyyMMdd")`
`docker compose -f docker/docker-compose.yml --project-directory $(pwd) up -d`

###End
