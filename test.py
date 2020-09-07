def test_get_region_arguments():
    arguments = argparse.Namespace(region='arguments-region', role_arn=None, source_profile=None, target_profile_name='myrole')
    config = {}
    profiles = {
        'default': {
            'aws_access_key_id': 'AKIAXUQ34KE64G7ZZAWY',
            'aws_secret_access_key': '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',
            'region': 'default-region',
        },
        'myuser': {
            'aws_access_key_id': 'AKIAXUQ34KE64G7ZZAWY',
            'aws_secret_access_key': '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',
            'region': 'myuser-region',
        },
        'myrole': {
            'role_arn': 'arn:aws:iam:S3:role/role_name',
            'region': 'myrole-region',
        },
    }
    assert profile.get_region(profiles, arguments, config) == 'arguments-region'
