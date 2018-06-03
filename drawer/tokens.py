"""
tokens.py: Enum module for available functions to use in formulas and aliases for them
"""

import math

TOKENS = {
    "acos": "acos(x)\nReturn the arc cosine (in radians) of x.",
    "acosh": "acosh(x)\nReturn the inverse hyperbolic cosine of x.",
    "asin": "asin(x)\nReturn the arc sine (in radians) of x.",
    "asinh": "asinh(x)\nReturn the inverse hyperbolic sine of x.",
    "atan": "atan(x)\nReturn the arc tangent (in radians) of x.",
    "atanh": "atanh(x)\nReturn the inverse hyperbolic tangent of x.",
    "ceil": "ceil(x)\nReturn the ceiling of x",
    "cos": "cos(x)\nReturn the cosine of x (in radians).",
    "cosh": "cosh(x)\nReturn the hyperbolic cosine of x",
    "degrees": "degrees(x)\nConvert angle x from radians to degrees.",
    "exp": "exp(x)\nReturn e raised to the power of x",
    "factorial": "factorial(x)\nFind x!",
    "hypor": "hypot(x, y)\nReturn sqrt(x*x + y*y)",
    "log": "log(x[, base]\nReturn the logarithm of x to the given base or natural logarithm if base is not specified",
    "pow": "pow(x, y)\nReturn x to the power of y",
    "sin": "sin(x)\nReturn the sine of x (in radians)",
    "sinh": "sinh(x)\nReturn the hyperbolic sine of x",
    "sqrt": "sqrt(x)\nReturn the square root of x",
    "tan": "tan(x)\nReturn the tangent of x (in radians)",
    "tanh": "tanh(x)\nReturn the hyperbolic tangent of x",
}

ALIASES = {
    "ch": "cosh",
    "sh": "sinh",
    "tg": "tan",
    "th": "tanh",
    "ctg": "1/tan"
}
