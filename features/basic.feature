Feature: Basic feature
  Scenario:  Log on to the CLI

    When we open the cli with a directory 'test'
    Then we should see the prompt 'test%'

