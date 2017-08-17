.. _create_env:

*************************************
Project-specific Program Environments
*************************************

Progams change. Nothing is as frustrating as coming back to a project after a long time and spending the first {hours, days} updating your code to work with the new version. Same for debugging errors because your coauthor uses a slightly different setup.

The solution is to have isolated environments on a per-project basis. `Conda environments <http://conda.pydata.org/docs/using/envs.html>`_ allow you to do precisely this. This page describes them a little bit and explains the scripts that come as part of the templates in order to install them in an automated way.


Basic steps
===========

The templates come with a script which handles creating, activating and updating of environments. After cloning and changing to the project directory, you can run **(Mac, Linux)**::

    source set-env.sh

or **(Windows)**::

	set-env.bat

in your shell to create a new environment with the same name as your project folder.

The script will look at the *.environment.OPERATINGSYSTEM.yml* file, where the OS is your current OS, for conda and pip packages and install those in the newly created python environment. Once created, you activate your environment in the same way: **(Mac, Linux)**::

      source set-env.sh

or **(Windows)**::
	set-env.bat


Updating packages
=================

Make sure you activated the environment by ``source set-env.sh`` / ``set-env.bat``. Then use conda or pip directly: 

#. ``conda update [package]`` or ``pip install -U [package]``

For updating conda all packages, replace ``[package]`` by ``--all``.


Installing additional packages
==============================

To list installed packages, type


#. ``conda list``

If you want to add a package to your environment, run


#. ``conda install [package]`` or ``pip install [package]``

**Choosing between conda and pip**

Generally it is recommended to use *conda* whenever possible (necessary for most scientific packages, they are usually not pure-Python code and that is all that pip can handle, roughtly speaking). For pure-Python packages, we sometimes fall back on *pip*.


Saving your environment
=======================

After updating or changing your environment you have to save the status in the respective *environment.OPERATINGSYSTEM.yml* file to avoid version conflictsmaintain environment coherence in a project with multiple collaborators.

Run for **(Windows)**::

    conda env export > environment.windows.yml

Or for **(Mac)**::

    conda env export > environment.osx.yml

After exporting, manually delete the last line in the environment file, as it is system specific.


Information about your conda environments
=========================================

For listing your installed conda environments, type:

    conda info --envs

The currently activated one will be marked.


