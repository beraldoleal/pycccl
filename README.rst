#############################################
Python (C)rypto (C)urrency (C)ommon (L)ibrary
#############################################

|Experimental| |Tag| |Release| |License|

*pycccl* is a library which aims to standardize access to information provided
by multiple exchanges sites.

Each exchange has a specific API with different methods to access basic
information. Using *pycccl* you have access to all supported exchanges in the
same way.

.. note::

    On the future, this library will also talk with private API methods in
    order to execute actions that requires authentication.

Quick Start
***********

Installing
==========

This project uses python3. So in order to use this software please install
python3 into your environment beforehand.

Installing via git source code:

.. code-block:: shell

   $ git clone https://github.com/beraldoleal/pycccl.git

After cloning, the installation process is done by standard `setuptools` install
procedure:

.. code-block:: shell

   $ cd pycccl
   $ sudo python3 setup.py install

If you prefer, you can install via pip command:

.. code-block:: shell

   $ sudo pip3 install pycccl


Basic Usage Example
===================

See how it is easy to get a token price at a specific exchange:

.. code-block:: python

    >>> from pycccl.exchanges.poloniex import Poloniex
    >>> polo = Poloniex()
    2017-12-17 14:22:04.690598 [Poloniex] INFO: Creating component
    >>> polo.get_last_price('BTC', 'USDT')
    18500.00000104

All exchanges classes has implemented the following methods: *get_24highest()*,
*get_24lowest()*, *get_24volume()*, *get_last_price()*, *get_ticker()*.

.. note::

    A detalied documentation API of this library will be released soon.

Exchanges Supported
===================

For now, we have support to: bitbay, bitfinex, bitstamp, blinktrade, cexio,
liqui, poloniex and yobit.

Authors
*******

For a complete list of authors, please open ``AUTHORS.rst`` file.

Contributing
************

Please feel free to open an issue or submit a PR for this project. Also let me
know if you have interest on a specific exchange support.

License
*******

This software is under *MIT-License*. For more information please read
``LICENSE`` file.


.. |Experimental| image:: https://img.shields.io/badge/stability-experimental-orange.svg
.. |Tag| image:: https://img.shields.io/github/tag/beraldoleal/pycccl.svg
   :target: https://github.com/beraldoleal/pycccl/tags
.. |Release| image:: https://img.shields.io/github/release/beraldoleal/pycccl.svg
   :target: https://github.com/beraldoleal/pycccl/releases
.. |License| image:: https://img.shields.io/github/license/beraldoleal/pycccl.svg
   :target: https://github.com/beraldoleal/pycccl/blob/master/LICENSE
