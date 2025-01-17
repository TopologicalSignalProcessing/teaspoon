teaspoon: Topological Signal Processing in Python
=================================================


The emerging field of topological signal processing brings methods from Topological Data Analysis (TDA) to create new tools for signal processing by incorporating aspects of shape.
This python package, teaspoon for tsp or topological signal processing, brings together available software for computing persistent homology, the main workhorse of TDA, with modules that expand the functionality of teaspoon as a state-of-the-art topological signal processing tool.
These modules include methods for incorporating tools from machine learning, complex networks, information, and parameter selection along with a dynamical systems library to streamline the creation and benchmarking of new methods.
All code is open source with up to date documentation, making the code easy to use, in particular for signal processing experts with limited experience in topological methods.

.. image:: figures/takens_embedding_gif_v2.gif
  :width: 600 px


Table of Contents
*******************


.. toctree::
   :maxdepth: 2
   :numbered:

   Getting Started <installation/index.rst>
   Modules <modules/index.rst>
   Example Notebooks <notebooks/index.rst>
   Contributing <contributing.rst>
   License <license.rst>
   Citing <citing.rst>

Modules
*******


.. image:: figures/tspPipeline.png
   :alt: The basic pipeline of a TSP project aligned with the modules of teaspoon.

Many topological signal processing projects can be fit into the pipeline shown above; and this pipeline aligns with the five submodules of ``teaspoon``. 
We start with input time series data. In ``teaspoon``, the `MakeData`_ module provides methods for creating synthetic data sets for testing purposes, including the `DynSysLib`_ submodule with an extensive array of dynamical systems. 
The `ParameterSelection`_ modules provides tools for determining best parameters for transforming the time series into a delay coordinate (sometimes called Takens') embedding. This includes standard tools such as false nearest neighbors and mutual information function as well as newly developed tools. The Signal Processing (`SP`_) module does the conversion from a time series to a topological input. This includes the standard delay coordinate embedding, as well as network representations of time series. This topological input can be converted to a topological signature, in most cases a persistence diagram, using the `TDA`_ module. These persistence diagrams can then be used in a machine learning pipeline using the vectorization tools from the `ML`_ module. Our newest module, Data Assimilation and Forecasting (`DAF`_),provides tools for generating data driven models for dynamical systems and optimally updating the models using persistent homology. 

.. _MakeData: https://teaspoontda.github.io/teaspoon/modules/MakeData/index.html
.. _DynSysLib: https://teaspoontda.github.io/teaspoon/modules/MakeData/DynSysLib/index.html
.. _ParameterSelection: https://teaspoontda.github.io/teaspoon/modules/ParamSelection/index.html
.. _SP: https://teaspoontda.github.io/teaspoon/modules/SP/index.html
.. _TDA: https://teaspoontda.github.io/teaspoon/modules/TDA/index.html
.. _ML: https://teaspoontda.github.io/teaspoon/modules/ML/index.html
.. _DAF: https://teaspoontda.github.io/teaspoon/modules/DAF/index.html


Collaborators
***************

The code is a compilation of work done by `Elizabeth Munch <http://www.elizabethmunch.com>`_ and `Firas Khasawneh <http://www.firaskhasawneh.com/>`__ along with their students and collaborators.  People who have contributed to teaspoon include:

- `Audun Myers <https://www.audunmyers.com>`_
- `Melih Yesilli <https://www.melihcanyesilli.com>`_
- `Sarah Tymochko <https://www.sarahtymochko.com/home>`_
- `Danielle Barnes <https://github.com/barnesd8>`_
- `Ismail Guzel <https://ismailguzel.github.io>`_
- `Max Chumley <https://www.maxchumley.com>`_




Contact Information
********************
- `Liz Munch <http://www.elizabethmunch.com>`_: `muncheli@msu.edu <mailto:muncheli@msu.edu>`_
- `Firas Khasawneh <https://www.firaskhasawneh.com>`__: `khasawn3@egr.msu.edu <mailto:khasawn3@egr.msu.edu>`_
