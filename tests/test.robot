*** Settings ***
Library         test_library.TestLibrary


*** Test Cases ***
Get Car Models Test
    ${essential_params}  create list
    ${unessential_params}  create list   car_brand=奥迪  car_series=R8  car_scale=S  car_model=R8  is_car_model=False  page_num=1  page_size=1
    ${results}  auto params  ${essential_params}  ${unessential_params}
    :FOR  ${kwargs}  IN  @{results}
    \  run keyword and continue on failure  get success  &{kwargs}

*** Keywords ***
Get Success
    [Arguments]             &{kwargs}
    ${resp} =               get car models  &{kwargs}
