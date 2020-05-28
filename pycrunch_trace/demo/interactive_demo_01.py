from datetime import datetime
from time import sleep

from pycrunch_trace.client.api import trace

from pycrunch_trace.demo.interactive_demo_02 import method_in_another_file
from pycrunch_trace.demo.interactive_demo_03 import show_me_how_to_navigate_using_graph
from pycrunch_trace.demo.interactive_demo_04 import alternative_ways_to_trace


@trace('interactive_demo')
def method_you_want_to_trace(some_number: int, some_string: str):
    # Take a look at the inspector panel.
    # Variable you passed, are recorded there.
    print('Press down arrow on keyboard to step into next line')
    print('You can also use toolbar button (↓) near slider')

    print('Lets now change value of some_number.')
    some_number -= 1
    print('Notice that now, inspector recorded value to be 2.')
    print('Any time you can step to previous line using Up Arrow or [↑] button.')

    print('Now, to the function calls.')
    print('Press Right Arrow on keyboard or [→] button to step into the next method')
    # You can always go back using Left Arrow
    from_external_method = method_in_another_file(some_number)

    print("If you haven't open graph yet, press G")
    print("All toolbars can be accessed using settings button in the top right corner")

    print("Use [→] to `step into` next method")
    sleep(0.1)
    we_need_to_go_deeper()
    alternative_ways_to_trace()

    print('You can start this tutorial again by dragging slider to the beginning')

    print("That's it. Start tracing now by installing:")
    print("  pip install pycrunch-trace")

    return str(datetime.utcnow())


def we_need_to_go_deeper():
    print("Sometimes insignificant call time makes it hard to navigate the graph")

    print("Lets take factorial for instance")
    sleep(0.1)

    print("Click at `we_need_to_go_deeper` method in the graph, holding Command key")
    # or (Control key on Windows)
    factorial = recursive_factorial(6)

    print("You can scope even deeper in call tree.")
    print("  By clicking with the mouse while holding Command")

    print("Entire call stack is drawn under the method you scoped to")

    print("You can exit from the scope same way:")
    print(" By holding Command and clicking on outer method")

    # Right arrow [→]
    show_me_how_to_navigate_using_graph()


def recursive_factorial(num: int):
    sleep(0.005)
    if num == 1:
        return num
    else:
        return num * recursive_factorial(num - 1)


method_you_want_to_trace(3, 'Welcome To PyTrace')
