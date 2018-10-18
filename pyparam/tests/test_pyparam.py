"""
Unit and regression test for the pyparam package.
"""

# Import package, test suite, and other packages as needed
import pyparam
import pytest
import sys

def test_pyparam_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "pyparam" in sys.modules
