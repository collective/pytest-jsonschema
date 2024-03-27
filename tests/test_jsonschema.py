def test_fixtures_available(testdir):
    """Test pytest-jsonschema fixtures exist."""
    fixtures = [
        "schema_validate",
        "schema_validate_string",
        "schema_validate_file",
    ]
    pyfile = ""
    for fixture in fixtures:
        pyfile = f"""
        {pyfile}

        def test_{fixture}_exists({fixture}):
            # Just pass the test, because if a fixture is not available,
            # it will raise an error
            assert True

        """

    testdir.makepyfile(pyfile)

    # run all tests with pytest
    result = testdir.runpytest()

    # check that all tests passed
    result.assert_outcomes(passed=len(fixtures))
