# Created by vaishnavisethuraman at 14/07/22
Feature: Amazon Product Search Test


  Scenario: User can search for a product
    Given Open amazon page
    When Search for word coffee on amazon
    Then Results for coffee shown