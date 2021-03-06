#-----------------------------------------------------------------------------
# Copyright (c) 2012 - 2020, Anaconda, Inc., and Bokeh Contributors.
# All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Boilerplate
#-----------------------------------------------------------------------------
import pytest ; pytest

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Module under test
import bokeh.util.dependencies as dep # isort:skip

#-----------------------------------------------------------------------------
# Setup
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# General API
#-----------------------------------------------------------------------------

class Test_detect_phantomjs(object):

    def test_detect_phantomjs_success(self) -> None:
        assert dep.detect_phantomjs() is not None

    def test_detect_phantomjs_bad_path(self, monkeypatch) -> None:
        monkeypatch.setenv("BOKEH_PHANTOMJS_PATH", "bad_path")
        with pytest.raises(RuntimeError):
            dep.detect_phantomjs()

    def test_detect_phantomjs_bad_version(self) -> None:
        with pytest.raises(RuntimeError) as e:
            dep.detect_phantomjs('10.1')
        assert str(e.value).endswith("PhantomJS version to old. Version>=10.1 required, installed: 2.1.1")

    def test_detect_phantomjs_default_required_version(self) -> None:
        assert dep.detect_phantomjs.__defaults__ == ('2.1',)

class Test_import_optional(object):

    def test_success(self) -> None:
        assert dep.import_optional('sys') is not None

    def test_fail(self) -> None:
        assert dep.import_optional('bleepbloop') is None

class Test_import_required(object):

    def test_success(self) -> None:
        assert dep.import_required('sys', 'yep') is not None

    def test_fail(self) -> None:
        with pytest.raises(RuntimeError) as excinfo:
            dep.import_required('bleepbloop', 'nope')
        assert 'nope' in str(excinfo.value)

#-----------------------------------------------------------------------------
# Dev API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Private API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------
