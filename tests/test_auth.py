"""Unit tests for myskoda.auth."""

from collections import OrderedDict
from pathlib import Path
from unittest.mock import patch
from urllib.parse import urlencode

import aiohttp
import pytest
from aioresponses import aioresponses

from myskoda.auth.authorization import Authorization, random_nonce
# from myskoda.const import BASE_URL_IDENT, CLIENT_ID

FIXTURES_DIR = Path(__file__).parent.joinpath("fixtures")


def fixture(filename: str) -> str:
    with FIXTURES_DIR.joinpath(filename).open() as file:
        return file.read()


# @pytest.mark.asyncio
@pytest.mark.usefixtures("verifier")
@pytest.mark.usefixtures("nonce")
@patch(
    "myskoda.auth.authorization.random_nonce", return_value="f0a57298-a276-4b3f-8bc1-c5f97f23d681"
)
def test_get_info(responses: aioresponses) -> None:
    assert random_nonce() == "f0a57298-a276-4b3f-8bc1-c5f97f23d681"
    # query = urlencode(
    #     OrderedDict(
    #         client_id=CLIENT_ID,
    #         code_challenge="abcdefghabcdefgh",
    #         code_challenge_method="s256",
    #         nonce="f0a57298-a276-4b3f-8bc1-c5f97f23d681",
    #         prompt="login",
    #         redirect_uri="myskoda://redirect/login/",
    #         response_type="code+id_token",
    #         scope="address+badge+birthdate+cars+driversLicense+dealers+email+mileage+mbb+nationalIdentifier+openid+phone+profession+profile+vin",
    #     )
    # )
    # relay_state = "d865b506bd6759b20e832c8c692c5ca2669ebd27"
    # user_id = "b8bc126c-ee36-402b-8723-2c1c3dff8dec"
    # hmac = "575452461e126b1873f4655918e14d0ba1a40622b768438fe4dd6d9579bc170c"
    # print(f"{BASE_URL_IDENT}/oidc/v1/authorize?{query}")

    # responses.get(
    #     url=f"{BASE_URL_IDENT}/oidc/v1/authorize?{query}",
    #     status=200,
    #     body=fixture("auth/signin.html"),
    # )
    # responses.post(
    #     url=f"{BASE_URL_IDENT}/signin-service/v1/{CLIENT_ID}/login/authenticate",
    #     status=301,
    #     headers={
    #         "Location": "{BASE_URL_IDENT}/oidc/v1/oauth/sso?clientId={CLIENT_ID}&relayState={relay_state}&userId={user_id}&HMAC={hmac}",
    #         "LOL": " LOL"
    #     }
    # )
    # # responses.post(
    # #     url=f"{BASE_URL_IDENT}/oidc/v1/oauth/sso?clientId={CLIENT_ID}&relayState={relay_state}&userId={user_id}&HMAC={hmac}",
    # #     status=301,
    # #     headers={
    # #         "Location": "{BASE_URL_IDENT}/signin-service/v1/consent/users/{user_id}/{CLIENT_ID}?scopes=address%20badge%20birthdate%20cars%20driversLicense%20dealers%20email%20mileage%20mbb%20nationalIdentifier%20openid%20phone%20profession%20profile%20vin&relayState={relay_state}&callback={BASE_URL_IDENT}/oidc/v1/oauth/client/callback&hmac={hmac}"
    # #     }
    # # )
    # # responses.post(
    # #     url=f"{BASE_URL_IDENT}/signin-service/v1/consent/users/{user_id}/{CLIENT_ID}?scopes=address%20badge%20birthdate%20cars%20driversLicense%20dealers%20email%20mileage%20mbb%20nationalIdentifier%20openid%20phone%20profession%20profile%20vin&relayState={relay_state}&callback={BASE_URL_IDENT}/oidc/v1/oauth/client/callback&hmac={hmac}",
    # #     status=301,
    # #     headers={
    # #         "Location": "{BASE_URL_IDENT}/oidc/v1/oauth/client/callback/success?user_id={user_id}&client_id={CLIENT_ID}&scopes=address%20badge%20birthdate%20cars%20driversLicense%20dealers%20email%20mileage%20mbb%20nationalIdentifier%20openid%20phone%20profession%20profile%20vin&consentedScopes=address%20badge%20birthdate%20cars%20driversLicense%20dealers%20email%20mileage%20mbb%20nationalIdentifier%20openid%20phone%20profession%20profile%20vin&relayState={relay_state}&hmac={hmac}"
    # #     }
    # # )

    # session = aiohttp.ClientSession()
    # authorization = Authorization(session)

    # await authorization.authorize("test@example.com", "example")
