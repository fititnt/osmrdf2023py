from contextlib import redirect_stdout
import io
import os
import sys
import osmrdf2023
# import osmrdf2023 as osmrdf
# import osmrdf2023
# from osmrdf2023 import *
# from osmrdf2023 import *
# from osmrdf2023 import osmrdf_xmldump2_ttl_v2


test_dir = os.path.dirname(os.path.realpath(__file__))


def test_node_ttl():
    io_catpure = io.StringIO()
    with redirect_stdout(io_catpure):
        osmrdf2023.osmrdf_xmldump2_ttl_v2(test_dir + '/data/node-1.xml')
        # osmrdf_xmldump2_ttl_v2(test_dir + '/data/node-1.xml')
    result = io_catpure.getvalue()

    # print(result)
    # assert False

    assert isinstance(result, str)
    assert result.find(
        'PREFIX osmt: <https://wiki.openstreetmap.org/wiki/Key:>') > -1
    assert result.find(
        'osmnode:1') > -1
    # assert result.


def test_way_ttl():

    io_catpure = io.StringIO()
    with redirect_stdout(io_catpure):
        osmrdf2023.osmrdf_xmldump2_ttl_v2(test_dir + '/data/way-100.xml')
        # osmrdf_xmldump2_ttl_v2(test_dir + '/data/way-100.xml')
    result = io_catpure.getvalue()

    # print(result)
    # assert False

    assert isinstance(result, str)
    assert result.find(
        'PREFIX osmway: <https://www.openstreetmap.org/way/>') > -1
    assert result.find(
        'osmway:100') > -1


def test_relation_ttl():

    io_catpure = io.StringIO()
    with redirect_stdout(io_catpure):
        osmrdf2023.osmrdf_xmldump2_ttl_v2(
            test_dir + '/data/relation-10000.xml')
        # osmrdf_xmldump2_ttl_v2(
        #     test_dir + '/data/relation-10000.xml')
    result = io_catpure.getvalue()

    # print(result)
    # assert False

    assert isinstance(result, str)
    assert result.find(
        'PREFIX osmrel: <https://www.openstreetmap.org/relation/>') > -1
    assert result.find(
        'osmrel:10000') > -1
