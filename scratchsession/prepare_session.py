import requests

def prepare_session(username: str, password: str, user_agent: str = 'python') -> requests.Session:
    """A function that creates a `requests.Session` object ready for use with 
    
    :param username: The account username
    :type username: str
    :param password: The account password
    :type password: str
    :param user_agent: A useragent string used to identify information about the session. Default, python
    :type user_agent: str

    How does this work?

    Using prepare_session is very easy! In your own code, simply use the following code::

        from scratchsession import prepare_session
        
        session = prepare_session("your_username_here", "your_password_here")

        # Print your account navigation info:
        resp = session.get("https://scratch.mit.edu/fragment/account-nav.json")
        print(resp.text)
    """
    
    
    # Reference: https://github.com/yuwex/scratchcloud/blob/main/scratchcloud/client.py#L362

    # Cookie header isn't needed
    headers = {
        "X-CSRFToken": "None",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://scratch.mit.edu",
        "User-Agent": f"{user_agent}",
    }

    # Create session
    session = requests.Session()
    session.headers = headers

    # Get a new CSRF token.
    resp = session.get("https://scratch.mit.edu/csrf_token/", headers=headers)

    # Set the CSRF from the response.
    csrf_token = resp.cookies.get("scratchcsrftoken")

    # Update headers to include real CSRF
    session.headers["X-CSRFToken"] = csrf_token

    # Prepare login payload
    payload = {
        "username": username,
        "password": password,
    }

    # Log in with CSRF Token, username, and password.
    resp = session.post(
        "https://scratch.mit.edu/login/",
        json=payload,
    )

    # Update headers to include authentication token. This allows the session to use many restricted API endpoints.
    token = resp.json()[0]["token"]
    session.headers["X-Token"] = token

    code = resp.status_code

    if code == 200:
        return session
    else:
        raise ConnectionError(
            f"Got status code {code}. Maybe you entered invalid login information?"
        )



