from behave import when, then, step


@when("thing fails")
def step_impl(context):
    context.success = False


@when("thing succeeds")
def step_impl(context):
    context.success = True


@then("thing must be ok")
def step_impl(context):
    if not context.success:
        raise ValueError("thing is not ok")
