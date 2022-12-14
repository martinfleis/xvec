# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

import sphinx_autosummary_accessors


sys.path.insert(0, os.path.abspath("../xvec/"))

import xvec  # noqa

project = "Xvec"
copyright = "2022, Xvec developers"
author = "Martin Fleischmann, Benoît Bovy"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "numpydoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "myst_nb",
    "sphinx_copybutton",
    "sphinx_autosummary_accessors",
]

templates_path = [
    "_templates",
    sphinx_autosummary_accessors.templates_path,
]
exclude_patterns = []

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "shapely": ("https://shapely.readthedocs.io/en/latest/", None),
    "pyproj": ("https://pyproj4.github.io/pyproj/latest/", None),
    "xarray": ("https://docs.xarray.dev/en/latest/", None),
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]

html_theme_options = {
    "github_url": "https://github.com/martinfleis/xvec",
}
nb_execution_mode = "off"
autodoc_typehints = "none"
