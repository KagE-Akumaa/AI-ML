
# Python String Functions -- Quick Reference

## 1. `.split()` -- Convert a string into a list

Breaks a string into parts using a separator.

**Examples:** - `"10.0.0.5".split(".")` → `['10', '0', '0', '5']` -
`"a b  c".split()` → `['a', 'b', 'c']` (splits on any whitespace)

**Key Points:** - Default separator = whitespace - Returns a list of
substrings - Optional argument: `maxsplit`

------------------------------------------------------------------------

## 2. `.strip()` -- Remove leading & trailing whitespace

Used to clean input or text from files.

**Examples:** - `"  hello  ".strip()` → `'hello'` -
`"  test   ".strip()` → `'test'`

**Key Points:** - Removes spaces, tabs, newlines at both ends - Use
`.lstrip()` or `.rstrip()` for one side only

------------------------------------------------------------------------

## 3. `.replace()` -- Replace parts of a string

Creates a new string because strings are immutable.

**Examples:** - `"hello world".replace("world", "python")` →
`'hello python'` - `"1-1-1".replace("-", ".")` → `'1.1.1'`

**Key Points:** - Replaces all occurrences unless `count` is given -
Original string is unchanged

------------------------------------------------------------------------

## 4. `.lower()` -- Convert to lowercase

**Example:** `"HELLO".lower()` → `'hello'`

Use for: - Case-insensitive comparison - Normalizing user input

------------------------------------------------------------------------

## 5. `.upper()` -- Convert to uppercase

**Example:** `"hello".upper()` → `'HELLO'`

Use for: - Normalizing text - Creating uniform formatting

------------------------------------------------------------------------

## 6. f-strings -- Insert variables inside strings

**Example:**

    name = "Mukul"
    age = 21
    msg = f"My name is {name} and I am {age}."

**Key Points:** - Cleanest and fastest formatting method - Supports
expressions: `f"{10 + 5}"` → `'15'` - Functions also work:
`f"{name.upper()}"`

------------------------------------------------------------------------

## Quick Summary Table

  ----------------------------------------------------------------------------------------------------------
  Feature               Purpose                    Example
  --------------------- -------------------------- ---------------------------------------------------------
  `.split()`            Break string into list     `"a,b".split(",")`

  `.strip()`            Remove outer whitespace    `" hi ".strip()`

  `.replace()`          Replace substring          `"a-b".replace("-", "_")`

  `.lower()`            Convert to lowercase       `"Hi".lower()`

  `.upper()`            Convert to uppercase       `"Hi".upper()" | | f-strings | Insert variables |`f"IP:
                                                   {ip}"\`
  ----------------------------------------------------------------------------------------------------------
