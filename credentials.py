import os


class MisConfiguration(Exception):
    pass


def get_env_var(env_var):
    """
    Returns environment variables

    :param env_var:
    :return:
    """

    try:
        return os.environ[env_var]
    except KeyError as exc:
        error_msg = f'{exc}. Set the {env_var} environment variable'
        raise MisConfiguration(error_msg)


# Oauth2 configuration
# Expected issuer of the token
EXPECTED_ISSUER = get_env_var('EXPECTED_ISSUER')

# The /certs endpoint of the Oauth2 provider
OAUTH2_PROVIDER_URL = get_env_var('OAUTH2_PROVIDER_URL')

# The expected role of the Oauth2 user
EXPECTED_ROLE = get_env_var('EXPECTED_ROLE')

CLIENT_ID = get_env_var('CLIENT_ID')

# SMTP server configuration
SMTP_SERVER = get_env_var('SMTP_SERVER')
SMTP_SERVER_PORT = get_env_var('SMTP_SERVER_PORT')
