config = {
    "serverName": "Dash Multi-App Server",
    "debug": True,
    "otherLinkName": None,
    "otherLinkHref": "#",
    "apps": [
        {
            "name": "app1",
            "title": "Application 1",
            "path": "app-one",
            "description": "This is a simple example application."
        }
    ],
    "auth": {
        "required": False,
        "validPairs": [
            ["admin", "admin"],
            ["username", "password"]
        ]
    }
}