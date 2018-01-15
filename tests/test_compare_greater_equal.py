from niveristand import decorators, RealTimeSequence
from niveristand.datatypes import Boolean, Double, Int32
from niveristand.exceptions import TranslateError, VeristandError
import pytest
from testutilities import rtseqrunner
from testutilities.test_channels import TestChannels


a = 1
b = 2


@decorators.nivs_rt_sequence
def return_constant():
    a = Double(5)
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_simple_numbers():
    a = Boolean(False)
    a.value = 5 >= 1
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_nivsdatatype_num():
    a = Boolean(False)
    a.value = Double(5) >= 2
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_num_nivsdatatype():
    a = Boolean(False)
    a.value = 5 >= Double(2)
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_nivsdatatype_nivsdatatype():
    a = Boolean(False)
    a.value = Double(5) >= Double(1)
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_nivsdatatype_nivsdatatype1():
    a = Boolean(False)
    a.value = Double(5) >= Int32(1)
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_nivsdatatype_nivsdatatype2():
    a = Boolean(False)
    a.value = Int32(5) >= Double(1)
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_nivsdatatype_nivsdatatype3():
    a = Boolean(False)
    a.value = Int32(5) >= Int32(2)
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_multiple_types():
    a = Boolean(False)
    a.value = Double(5) >= 2 >= 1.0
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_multiple_types1():
    a = Boolean(False)
    a.value = Int32(5) >= Double(4) >= 3 >= 2.0
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_use_rtseq():
    a = Boolean(False)
    a.value = 5 >= return_constant()
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_use_rtseq1():
    a = Boolean(False)
    a.value = return_constant() >= 4
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_use_rtseq2():
    a = Boolean(False)
    a.value = Double(6) >= return_constant()
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_use_rtseq3():
    a = Boolean(False)
    a.value = return_constant() >= Double(4)
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_use_rtseq4():
    a = Boolean(False)
    a.value = Int32(6) >= return_constant()
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_use_rtseq5():
    a = Boolean(False)
    a.value = return_constant() >= Int32(1)
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_with_parantheses():
    a = Boolean(False)
    a.value = 5 >= (3 >= 2)
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_variables():
    a = Double(5)
    b = Boolean(False)
    b.value = a >= 1
    return b.value


@decorators.nivs_rt_sequence
def greater_eq_variables1():
    a = Double(1)
    b = Boolean(False)
    b.value = 5 >= a.value
    return b.value


@decorators.nivs_rt_sequence
def greater_eq_variable_variable():
    a = Double(2)
    b = Double(1)
    c = Boolean(False)
    c.value = a.value >= b.value
    return c.value


@decorators.nivs_rt_sequence
def greater_eq_variable_variable1():
    a = Double(2)
    b = Double(1)
    c = Boolean(False)
    c = a >= b
    return c


@decorators.nivs_rt_sequence
def greater_eq_variable_rtseq():
    a = Double(6.0)
    b = Boolean(False)
    b.value = a.value >= return_constant()
    return b.value


@decorators.nivs_rt_sequence
def greater_eq_variable_rtseq1():
    a = Double(1)
    b = Boolean(False)
    b.value = return_constant() >= a.value
    return b.value


@decorators.nivs_rt_sequence
def greater_eq_to_channelref():
    a = Boolean(False)
    a.value = 5 >= Double(TestChannels.HP_COUNT)
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_binary_unary():
    a = Boolean(False)
    a.value = 2 >= - 1
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_with_multiple_comparators():
    a = Boolean(False)
    a.value = 5 >= 4 >= 3 >= 2
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_complex_expr():
    a = Boolean(False)
    a.value = 2 >= (1 if 2 < 3 else 4)
    return a.value


# region invalid tests
@decorators.nivs_rt_sequence
def greater_eq_invalid_variables():
    return a.value >= b


@decorators.nivs_rt_sequence
def greater_eq_invalid_variables1():
    return a.value >= b.value


@decorators.nivs_rt_sequence
def greater_eq_invalid_variables2():
    a = Boolean(0)
    b = Double(0)
    b.value = a.value >= 2
    return b


@decorators.nivs_rt_sequence
def greater_eq_to_None():
    a = Boolean(False)
    a.value = None >= 1
    return a.value


@decorators.nivs_rt_sequence
def greater_eq_invalid_rtseq_call():
    a = Boolean(False)
    a.value = return_constant >= 1
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_simple_numbers():
    a = Boolean(False)
    a.value = 1 >= 1
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_num_nivsdatatype():
    a = Boolean(True)
    a.value = Double(1) >= 2
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_nivsdatatype_nivsdatatype():
    a = Boolean(False)
    a.value = Double(1) >= Double(1)
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_nivsdatatype_nivsdatatype1():
    a = Boolean(0)
    a.value = Double(1) >= Int32(1)
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_nivsdatatype_nivsdatatype2():
    a = Boolean(0)
    a.value = Int32(1) >= Double(1)
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_nivsdatatype_nivsdatatype3():
    a = Boolean(0)
    a.value = Int32(1) >= Int32(2)
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_multiple_types():
    a = Boolean(0)
    a.value = Double(1) >= 1 >= 1.0
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_multiple_types1():
    a = Boolean(0)
    a.value = Int32(1) >= Double(2) >= 3.0 >= 4
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_use_rtseq():
    a = Boolean(0)
    a.value = 5 >= return_constant()
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_use_rtseq1():
    a = Boolean(0)
    a.value = return_constant() >= 5
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_use_rtseq2():
    a = Boolean(0)
    a.value = Double(5) >= return_constant()
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_use_rtseq3():
    a = Boolean(0)
    a.value = return_constant() >= Double(5)
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_use_rtseq4():
    a = Boolean(0)
    a.value = Int32(1) >= return_constant()
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_use_rtseq5():
    a = Boolean(0)
    a.value = return_constant() >= Int32(1)
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_with_parantheses():
    a = Boolean(True)
    a.value = 1 >= (2 >= 3)
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_with_parantheses1():
    a = Boolean(True)
    a.value = 0 >= (Double(2) >= Int32(2))
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_variables():
    a = Double(1)
    b = Boolean(0)
    b.value = a >= 1
    return b.value


@decorators.nivs_rt_sequence
def gt_equal_variables1():
    a = Double(1)
    b = Boolean(0)
    b.value = a.value >= 1
    return b.value


@decorators.nivs_rt_sequence
def gt_equal_variable_variable():
    a = Double(1)
    b = Double(2)
    c = Boolean(True)
    c.value = a.value >= b.value
    return c.value


@decorators.nivs_rt_sequence
def gt_equal_variable_variable1():
    a = Double(2)
    b = Double(2)
    c = Boolean(False)
    c.value = a.value >= b.value
    return c.value


@decorators.nivs_rt_sequence
def gt_equal_variable_variable2():
    a = Double(2)
    b = Double(2)
    c = Boolean(False)
    c = a >= b
    return c


@decorators.nivs_rt_sequence
def gt_equal_variable_rtseq():
    a = Boolean(1)
    b = Double(0)
    b.value = a.value >= return_constant()
    return b.value


@decorators.nivs_rt_sequence
def gt_equal_variable_rtseq1():
    a = Boolean(1)
    b = Double(0)
    b.value = return_constant() >= a.value
    return b.value


@decorators.nivs_rt_sequence
def gt_equal_to_channelref():
    a = Boolean(0)
    a.value = 1 >= Double(TestChannels.HP_COUNT)
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_binary_unary():
    a = Boolean(0)
    a.value = 2 >= - 1
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_with_multiple_comparators():
    a = Boolean(True)
    a.value = 1 >= 2 >= 3 >= 4
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_complex_expr():
    a = Boolean(0)
    a.value = 1 >= (1 if 2 < 3 else 4)
    return a.value


# region invalid tests
@decorators.nivs_rt_sequence
def gt_equal_invalid_variables():
    return a.value >= b


@decorators.nivs_rt_sequence
def gt_equal_invalid_variables1():
    return a.value >= b.value


@decorators.nivs_rt_sequence
def gt_equal_invalid_variables2():
    a = Boolean(0)
    b = Double(0)
    b.value = a.value >= 2
    return b


@decorators.nivs_rt_sequence
def gt_equal_to_None():
    a = Boolean(0)
    a.value = None >= 1  # noqa: E711 the identity operator "is" is not being tested here.
    return a.value


@decorators.nivs_rt_sequence
def gt_equal_invalid_rtseq_call():
    a = Boolean(0)
    a.value = return_constant >= 1
    return a.value

# end region


run_tests = [
    (return_constant, (), 5),
    (greater_eq_simple_numbers, (), True),
    (greater_eq_nivsdatatype_num, (), True),
    (greater_eq_nivsdatatype_nivsdatatype, (), True),
    (greater_eq_nivsdatatype_nivsdatatype1, (), True),
    (greater_eq_nivsdatatype_nivsdatatype2, (), True),
    (greater_eq_nivsdatatype_nivsdatatype3, (), True),
    (greater_eq_with_parantheses, (), True),
    (greater_eq_variables, (), True),
    (greater_eq_variables1, (), True),
    (greater_eq_variable_variable, (), True),
    (greater_eq_variable_variable1, (), True),
    (greater_eq_complex_expr, (), True),
    (gt_equal_simple_numbers, (), True),
    (gt_equal_num_nivsdatatype, (), False),
    (gt_equal_nivsdatatype_nivsdatatype, (), True),
    (gt_equal_nivsdatatype_nivsdatatype1, (), True),
    (gt_equal_nivsdatatype_nivsdatatype2, (), True),
    (gt_equal_nivsdatatype_nivsdatatype3, (), False),
    (gt_equal_with_parantheses, (), True),
    (gt_equal_with_parantheses1, (), False),
    (gt_equal_variables, (), True),
    (gt_equal_variables1, (), True),
    (gt_equal_variable_variable, (), False),
    (gt_equal_variable_variable1, (), True),
    (gt_equal_variable_variable2, (), True),
    (gt_equal_complex_expr, (), True),
]

skip_tests = [
    (greater_eq_num_nivsdatatype, (), "Builtins as the left comparer can't be overriden"),
    (greater_eq_use_rtseq, (), "RTSeq call not implemented yet."),
    (greater_eq_use_rtseq1, (), "RTSeq call not implemented yet."),
    (greater_eq_use_rtseq2, (), "RTSeq call not implemented yet."),
    (greater_eq_use_rtseq3, (), "RTSeq call not implemented yet."),
    (greater_eq_use_rtseq4, (), "RTSeq call not implemented yet."),
    (greater_eq_use_rtseq5, (), "RTSeq call not implemented yet."),
    (greater_eq_variable_rtseq, (), "RTSeq call not implemented yet."),
    (greater_eq_variable_rtseq1, (), "RTSeq call not implemented yet."),
    (greater_eq_to_channelref, (), "Channel ref transform not yet implemented."),
    (greater_eq_binary_unary, (), "Unary operator not implemented."),
    (greater_eq_to_None, (), "Name transformer doesn't raise an exception for NoneType with python 2.7."),
    (greater_eq_invalid_rtseq_call, (), "RTSeq call not implemented yet."),
    (greater_eq_multiple_types, (), "Cascading comparators untested in VM"),
    (greater_eq_multiple_types1, (), "Cascading comparators untested in VM"),
    (greater_eq_with_multiple_comparators, (), "Cascading comparators untested in VM"),
    (gt_equal_use_rtseq, (), "RTSeq call not implemented yet."),
    (gt_equal_use_rtseq1, (), "RTSeq call not implemented yet."),
    (gt_equal_use_rtseq2, (), "RTSeq call not implemented yet."),
    (gt_equal_use_rtseq3, (), "RTSeq call not implemented yet."),
    (gt_equal_use_rtseq4, (), "RTSeq call not implemented yet."),
    (gt_equal_use_rtseq5, (), "RTSeq call not implemented yet."),
    (gt_equal_variable_rtseq, (), "RTSeq call not implemented yet."),
    (gt_equal_variable_rtseq1, (), "RTSeq call not implemented yet."),
    (gt_equal_to_channelref, (), "Channel ref transform not yet implemented."),
    (gt_equal_binary_unary, (), "Unary operator not implemented."),
    (gt_equal_to_None, (), "Name transformer doesn't raise an exception for NoneType with python 2.7."),
    (gt_equal_invalid_rtseq_call, (), "RTSeq call not implemented yet."),
    (gt_equal_multiple_types, (), "Cascading comparators untested in VM"),
    (gt_equal_multiple_types1, (), "Cascading comparators untested in VM"),
    (gt_equal_with_multiple_comparators, (), "Cascading comparators untested in VM"),
]

fail_transform_tests = [
    (greater_eq_invalid_variables, (), TranslateError),
    (greater_eq_invalid_variables1, (), TranslateError),
    (greater_eq_invalid_variables2, (), TranslateError),
    (gt_equal_invalid_variables, (), TranslateError),
    (gt_equal_invalid_variables1, (), TranslateError),
    (gt_equal_invalid_variables2, (), TranslateError),
]


def idfunc(val):
    return val.__name__


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    try:
        RealTimeSequence(func_name)
    except expected_result:
        pass
    except VeristandError as e:
        pytest.fail('Unexpected exception raised:' +
                    str(e.__class__) + ' while expected was: ' + expected_result.__name__)
    except Exception as exception:
        pytest.fail('ExpectedException not raised: ' + exception)


@pytest.mark.parametrize("func_name, params, reason", skip_tests, ids=idfunc)
def test_skipped(func_name, params, reason):
    pytest.skip(func_name.__name__ + ": " + reason)