*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***
${INITIAL URL}      https://www.google.com
${BROWSER}        Chrome

*** Test Cases ***
Search on Google
    Open Browser To Initial Url
    Input Text      css:input[type=text]    Robot Framework
    Press Keys      css:input[type=text]    RETURN
    ${input_text} =     Get Element Attribute     css:input[type=text]      value
    Should Contain  ${input_text}   Robot
    Should Not Contain  ${input_text}   Nightwatch

*** Test Cases ***
Feeling lucky
    Open Browser To Initial Url
    Wait Until Element Is Visible   css:.FPdoLc input[name=btnI]
    Click Element      css:.FPdoLc input[name=btnI]
    Wait Until Element Is Visible    bla

*** Keywords ***
Open Browser To Initial Url
    Open Browser       ${INITIAL URL}    ${BROWSER}
    Title Should Be    Google
