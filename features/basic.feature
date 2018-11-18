Feature: Basic feature

  Scenario:  A basic scenario which should pass

    When thing succeeds
    Then thing must be ok

  Scenario:  Another basic scenario which should pass

    When thing succeeds
    Then thing must be ok


  Scenario:  Another basic scenario which should not pass

    When thing fails
    Then thing must be ok


  @tagA
  Scenario:  Another basic scenario which should pass (tag A)

    When thing succeeds
    Then thing must be ok

  @tagB
  Scenario:  Another basic scenario which should pass (tag B)

    When thing succeeds
    Then thing must be ok
