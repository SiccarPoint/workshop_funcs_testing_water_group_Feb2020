# workshop_funcs_testing_water_group_Feb2020

This holds resources for a simple Python course on functions and testing, beginning 5/2/20,
for the Cardiff Water discussion group. It is intended as 2, ~one-hour sessions.

This repo contains a Powerpoint presentation, and associated Python file resources.

These resources include versions of the code shown in the presentation, but also a set of
scripts ("SC_....py") designed for users to modify as an exercise to use the ideas
presented in the ppt.

SC_script.py presents a "typical" quick-and-dirty script to do some averaging processes on
some arbitrary data.

SC_script_funcs.py illustrates one way of function-ising those processes.

SC_script_funcs_examples.py presents a version of those functions that partly implements
some doctesting. It is left to the user to devise doctests for the other functions.

tests/test_SCs.py is a unit testing file that implements some elementary tests on the
weighted_mean func in SC_script_funcs_examples. It is left to the user to enhance this set.
