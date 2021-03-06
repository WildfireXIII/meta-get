# meta.api.pkg_managers.pacman.py

# Copyright (C) 2018 Nathan Martindale <nathanamartindale@gmail.com>
# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""API for accessing pacman functionality."""

import logging

import meta.current
import meta.shell


def install(*pkgs, silent=False):
    """Installs the given packages with the ``pacman -S`` command.

    :param str *pkgs: String(s) of packages to install
    :param bool silent: Whether to suppress console output of the command or not
    :returns: A string of everything written to stdout and stderr by the shell

    .. note::
        ``*pkgs`` is a variable length set of arguments, meaning this function can be called with
        multiple string arguments, and it will install the package named in each one.

        >>> meta.api.pkg_managers.pacman.install("vim", "python")

    """

    pkg_list = " ".join(pkgs)
    logging.info("Pacman API requested to install packages %s", pkg_list)

    output = meta.shell.execute("sudo pacman -S {0}".format(pkg_list), silent=silent)

    # add to autotracker
    for pkg in pkgs:
        meta.current.PACKAGE_AUTOTRACKER.packages.append(
            {"name": pkg, "pkg_manager": "pacman"}
        )

    return output


def uninstall(pkg, silent=False):
    """Installs the given package with the ``pacman -R`` command.

    :param str pkg: String of package to uninstall
    :param bool silent: Whether to suppress console output of the command or not
    :returns: A string of everything written to stdout and stderr by the shell
    """

    logging.info("Pacman API request to uninstall package %s", pkg)

    output = meta.shell.execute("sudo pacman -R {0}".format(pkg), silent=silent)
    return output
