---
name: debug-plain-javascript
description: "Use when debugging plain JavaScript or vanilla JS code, including browser scripts, DOM behavior, event handlers, fetch requests, runtime errors, unexpected values, async failures, and failing JavaScript tests. Applies to .js files without TypeScript or a frontend framework."
argument-hint: "Describe the JavaScript bug, error, failing behavior, or files to investigate"
user-invocable: true
disable-model-invocation: false
---

# Debug Plain JavaScript

Debug plain JavaScript using concrete runtime evidence and the smallest change
that fixes the root cause.

## When to Use

Use this skill for:

- Vanilla JavaScript in `.js` files
- Browser console errors and stack traces
- Incorrect DOM updates or event handling
- Failed `fetch` requests and response parsing
- Promise, `async`, and `await` problems
- Scope, coercion, mutation, and control-flow bugs
- JavaScript tests that fail or produce unexpected values

Do not assume TypeScript, React, Vue, Angular, or another framework unless the
repository clearly uses it.

## Procedure

1. Identify the exact failing behavior, expected behavior, and reproduction
   steps.
2. Start from the reported file, stack-trace location, failing test, or affected
   UI action.
3. Read the surrounding function and its direct callers before exploring
   unrelated code.
4. Check the browser or runtime console for the first relevant error.
5. Trace inputs and state through the controlling code path.
6. Form one falsifiable hypothesis about the root cause.
7. Choose the cheapest check that could disprove that hypothesis, such as:
   - A focused existing test
   - A minimal runtime reproduction
   - A temporary breakpoint or inspected value
   - A network response or DOM-state check
8. Apply the smallest root-cause fix consistent with nearby code.
9. Run the focused check immediately after the edit.
10. Test the affected behavior plus one relevant edge or failure case.
11. Remove temporary logging or debugging statements before finishing.

## Debugging Checks

Pay particular attention to:

- Missing or incorrect script loading order
- `null` results from DOM selectors
- Handlers attached before elements exist
- Incorrect event names, targets, or default browser behavior
- Accidental global variables
- Confusion between `==` and `===`
- String values used where numbers or booleans are expected
- Mutation of shared arrays or objects
- Missing `return` or `await`
- Rejected promises that are not handled
- `fetch` responses used without checking `response.ok`
- JSON parsing assumptions
- Closures capturing stale or changing values
- Off-by-one conditions and incorrect loop termination
- Code paths that behave differently for empty or missing values

## Validation

Prefer validation in this order:

1. Reproduce the originally failing behavior.
2. Run the narrowest relevant JavaScript test.
3. Run the repository's JavaScript lint or test command.
4. Exercise the affected browser workflow.
5. Run broader tests when the change affects shared behavior.

Report the root cause, changed behavior, validation performed, and any remaining
uncertainty.