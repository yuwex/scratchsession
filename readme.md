# scratchsession
*The easy way to set up scratch session objects.*


scratchsession allows you to set up a scratch HTTP session the right way. With just a single function, you never have to worry about unnecesary parsing times or bad request order. It does not use any RegEx or read HTML—just pure requests!

## Installing / Using

scratchsession can be installed via PyPI:

```
python -m pip install scratchsession
```

It can also just be copy/pasted into your own code. Make sure to copy all of the `prepare_session` function and import `requests` if you do this!

## Example
```python
from scratchsession import prepare_session

session = prepare_session("your_username_here", "your_password_here")

# Print your account navigation info:
resp = session.get("https://scratch.mit.edu/fragment/account-nav.json")
print(resp.text)
```

## Questions? Ask here:
 * Nothing here yet!
 * Still nothing :(
