from behave import given, when, then, step
import pexpect

@when("we open the cli with a directory '{dirname}'")
def step_impl(context, dirname):
    context.cli_child = pexpect.spawn ('./tester.py %s' % (dirname))

@then("we should see the prompt '{prompt}'")
def step_impl(context, prompt):
    try:
        context.cli_child.expect(prompt, timeout=2)
    except Exception as err:
        assert False, 'Expected prompt %s\n%s' % (prompt, err.value.split('\n')[0])

@then("we should NOT see the prompt '{prompt}'")
def step_impl(context, prompt):
    try:
        context.cli_child.expect(prompt, timeout=2)
        assert False, "Did not expect to see %s\n" % (prompt)
    except Exception as err:
        pass
