# Created by KRASAVA at 13.10.2019
Feature: Checking reaction of wrong data
    Scenario: Open website
      Given I open lkssau website
      Then I print the title of website
    Scenario: Type wrong data on enter
      Given I type wrong data
      Then I see error message