Feature: Test the features of the command line test console

  Scenario:  Log on to the CLI

    When we open the cli with a directory 'test'
    Then we should see the prompt 'test%'
