# -*- coding: utf-8 -*-
#
# IPython documentation build configuration file.

# NOTE: This file has been edited manually from the auto-generated one from
# sphinx.  Do NOT delete and re-generate.  If any changes from sphinx are
# needed, generate a scratch one and merge by hand any new fields needed.

#
# This file is execfile()d with the current directory set to its containing dir.
#
# The contents of this file are pickled, so don't put values in the namespace
# that aren't pickleable (module imports are okay, they're removed automatically).
#
# All configuration values have a default value; values that are commented out
# serve to show the default value.

import toml
import sys, os
from pathlib import Path

config = toml.load("./sphinx.toml")

# https://read-the-docs.readthedocs.io/en/latest/faq.html
ON_RTD = os.environ.get("READTHEDOCS", None) == "True"

if ON_RTD:
    tags.add("rtd")

    # RTD doesn't use the Makefile, so re-run autogen_{things}.py here.
    for name in ("config", "api", "magics", "shortcuts"):
        fname = Path("autogen_{}.py".format(name))
        fpath = (Path(__file__).parent).joinpath("..", fname)
        with open(fpath, encoding="utf-8") as f:
            exec(
                compile(f.read(), fname, "exec"),
                {
                    "__file__": fpath,
                    "__name__": "__main__",
                },
            )
import sphinx_rtd_theme

# Allow Python scripts to change behaviour during sphinx run
os.environ["IN_SPHINX_RUN"] = "True"

autodoc_type_aliases = {
    "Matcher": " IPython.core.completer.Matcher",
    "MatcherAPIv1": " IPython.core.completer.MatcherAPIv1",
}

# If your extensions are in another directory, add it here. If the directory
# is relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
sys.path.insert(0, os.path.abspath("../sphinxext"))

# We load the ipython release info into a dict by explicit execution
iprelease = {}
exec(
    compile(
        open("../../IPython/core/release.py", encoding="utf-8").read(),
        "../../IPython/core/release.py",
        "exec",
    ),
    iprelease,
)

# General configuration
# ---------------------

# Add any paths that contain templates here, relative to this directory.
templates_path = config["sphinx"]["templates_path"]
# The master toctree document.
master_doc = config["sphinx"]["master_doc"]
# General substitutions.
project = config["sphinx"]["project"]
copyright = config["sphinx"]["copyright"]
# ghissue config
github_project_url = config["sphinx"]["github_project_url"]
# The suffix of source filenames.
source_suffix = config["sphinx"]["source_suffix"]
# Exclude these glob-style patterns when looking for source files. They are
# relative to the source/ directory.
exclude_patterns = config["sphinx"]["exclude_patterns"]
# The name of the Pygments (syntax highlighting) style to use.
pygments_style = config["sphinx"]["pygments_style"]
# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = config["sphinx"]["extensions"]
# Set the default role so we can use `foo` instead of ``foo``
default_role = config["sphinx"]["default_role"]
modindex_common_prefix = config["sphinx"]["modindex_common_prefix"]

intersphinx_mapping = config["intersphinx_mapping"]
for k, v in intersphinx_mapping.items():
    intersphinx_mapping[k] = tuple(
        [intersphinx_mapping[k]["url"], intersphinx_mapping[k]["fallback"]]
    )

# numpydoc config
numpydoc_show_class_members = config["numpydoc"][
    "numpydoc_show_class_members"
]  # Otherwise Sphinx emits thousands of warnings
numpydoc_class_members_toctree = config["numpydoc"]["numpydoc_class_members_toctree"]
warning_is_error = config["numpydoc"]["warning_is_error"]

# Options for HTML output
# -----------------------
html_theme = config["html"]["html_theme"]
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = config["html"]["html_static_path"]
# Favicon needs the directory name
html_favicon = config["html"]["html_favicon"]
# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = config["html"]["html_last_updated_fmt"]
# Output file base name for HTML help builder.
htmlhelp_basename = config["html"]["htmlhelp_basename"]

# Additional templates that should be rendered to pages, maps page names to
# template names.
html_additional_pages = {}
for item in config["html"]["html_additional_pages"]:
    html_additional_pages[item[0]] = item[1]

# Options for LaTeX output
# ------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, document class [howto/manual]).
latex_documents = []
for item in config["latex"]["latex_documents"]:
    latex_documents.append(tuple(item))
# If false, no module index is generated.
latex_use_modindex = config["latex"]["latex_use_modindex"]
# The font size ('10pt', '11pt' or '12pt').
latex_font_size = config["latex"]["latex_font_size"]

# Options for texinfo output
# --------------------------
texinfo_documents = [
    (
        master_doc,
        "ipython",
        "IPython Documentation",
        "The IPython Development Team",
        "IPython",
        "IPython Documentation",
        "Programming",
        1,
    ),
]

#########################################################################
# Custom configuration
# The default replacements for |version| and |release|, also used in various
# other places throughout the built documents.
#
# The full version, including alpha/beta/rc tags.
release = "%s" % iprelease["version"]
# Just the X.Y.Z part, no '-dev'
version = iprelease["version"].split("-", 1)[0]

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = "%B %d, %Y"

rst_prolog = ""


def is_stable(extra):
    for ext in {"dev", "b", "rc"}:
        if ext in extra:
            return False
    return True


if is_stable(iprelease["_version_extra"]):
    tags.add("ipystable")
    print("Adding Tag: ipystable")
else:
    tags.add("ipydev")
    print("Adding Tag: ipydev")
    rst_prolog += """
.. warning::

    This documentation covers a development version of IPython. The development
    version may differ significantly from the latest stable release.
"""

rst_prolog += """
.. important::

    This documentation covers IPython versions 6.0 and higher. Beginning with
    version 6.0, IPython stopped supporting compatibility with Python versions
    lower than 3.3 including all versions of Python 2.7.

    If you are looking for an IPython version compatible with Python 2.7,
    please use the IPython 5.x LTS release and refer to its documentation (LTS
    is the long term support release).

"""

import logging


class ConfigtraitFilter(logging.Filter):
    """
    This is a filter to remove in sphinx 3+ the error about config traits being duplicated.

    As we autogenerate configuration traits from, subclasses have lots of
    duplication and we want to silence them. Indeed we build on travis with
    warnings-as-error set to True, so those duplicate items make the build fail.
    """

    def filter(self, record):
        if (
            record.args
            and record.args[0] == "configtrait"
            and "duplicate" in record.msg
        ):
            return False
        return True


ct_filter = ConfigtraitFilter()

import sphinx.util

logger = sphinx.util.logging.getLogger("sphinx.domains.std").logger
logger.addFilter(ct_filter)


def setup(app):
    app.add_css_file("theme_overrides.css")


# Cleanup
# -------
# delete release info to avoid pickling errors from sphinx

del iprelease
