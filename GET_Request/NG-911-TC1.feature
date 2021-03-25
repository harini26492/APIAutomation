#Place a call .  Observe Call Identifier and Incident Identifier appears on call at PSAP.
# Call should appear with queue URI in Route header (Queue Identifier).

  Feature: NG9-1-1 Standardize Identifiers
    Scenario Outline: To Verify the call with Queue URI in Route Header
      Given User place a call to PSAP
      When <Call Identifier> and <Incident Identifier> appears on Call at PSAP
      And PSAP receives the call
      Then Check the queue URI in Route Header

      Examples: | Call Identifier| Incident Identifier|
